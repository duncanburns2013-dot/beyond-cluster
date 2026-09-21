"""Re-derive every published figure in the beyond-cluster repo from primary sources.
Nothing here reads a cached value; every expectation is checked against a fresh query."""
import csv, json, re, sys
from soda import q, f

REPO = "E:/beyond-cluster/"
README = open(REPO + "README.md", encoding="utf-8").read()
HTML = open(REPO + "index.html", encoding="utf-8").read()

SIX = ["ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR", "ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE",
       "BEYOND HEALTHCARE AGENCY LLC", "BEYOND INDEPENDENT LIVING LLC", "BEYOND HEATHCARE AGENCY",
       "GREATER BOSTON HOME HEALTH CARE LLC"]
IN = "vendor in(%s)" % ",".join("'%s'" % v for v in SIX)
BHA = ["ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR", "ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE",
       "BEYOND HEALTHCARE AGENCY LLC", "BEYOND HEATHCARE AGENCY"]
IN_BHA = "vendor in(%s)" % ",".join("'%s'" % v for v in BHA)

results = []
def chk(label, expected, actual, tol=0.005):
    if isinstance(expected, float) or isinstance(actual, float):
        ok = abs(float(expected) - float(actual)) <= tol
    else:
        ok = expected == actual
    results.append((ok, label, expected, actual))
    print("%-5s %-58s published=%-22s live=%s" % ("PASS" if ok else "FAIL", label, expected, actual))

def one(where, sel="count(1) as n,sum(amount) as total"):
    r = q(select=sel, where=where)[0]
    return int(r["n"]), (f(r["total"]) if r.get("total") is not None else 0.0)

print("=" * 118)
print("A. HEADLINE TOTALS")
print("=" * 118)
n, t = one(IN);                                             chk("grand total, all time", 105956006.17, round(t, 2)); chk("grand total, payment count", 7380, n)
n, t = one(IN + " AND date <= '2026-01-21'");               chk("total as of the post date", 102287219.14, round(t, 2))
n, t = one(IN + " AND date >= '2016-01-01'");               chk("total since 2016-01-01", 62897038.88, round(t, 2))
n, t = one(IN + " AND date > '2026-01-21'");                chk("paid since the post", 3608847.42, round(t, 2))
r = q(select="max(date) as l,min(date) as f,min(amount) as mn", where=IN)[0]
chk("latest payment date", "2026-09-17", r["l"][:10]); chk("earliest payment date", "2011-05-25", r["f"][:10])
chk("smallest payment in the group", 0.21, f(r["mn"]))
neg = q(select="count(1) as n", where=IN + " AND amount < 0")[0]["n"]
chk("negative lines (recoupments)", "0", neg)

print("\n" + "=" * 118)
print("B. THE SIX VENDOR ROWS (README table)")
print("=" * 118)
pub = {"ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR": (1432, 63247375.74),
       "BEYOND INDEPENDENT LIVING LLC":            (4038, 32404181.08),
       "BEYOND HEALTHCARE AGENCY LLC":             (1391, 5868134.35),
       "ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE": (424,  4385632.99),
       "GREATER BOSTON HOME HEALTH CARE LLC":      (83,   47203.01),
       "BEYOND HEATHCARE AGENCY":                  (12,   3479.00)}
rowsum = 0.0; rown = 0
for v, (en, et) in pub.items():
    n, t = one("vendor='%s'" % v)
    chk("%s n" % v[:34], en, n); chk("%s $" % v[:34], et, round(t, 2))
    rowsum += t; rown += n
chk("six rows sum to the stated total", 105956006.17, round(rowsum, 2))
chk("six rows sum to the stated count", 7380, rown)

print("\n" + "=" * 118)
print("C. THE THREE LOAD-BEARING FINDINGS")
print("=" * 118)
n, t = one(IN_BHA + " AND date > '2023-12-29' AND date < '2024-09-20'")
chk("paid while dissolved, $", 643388.39, round(t, 2)); chk("paid while dissolved, payments", 153, n)
n, t = one("vendor='BEYOND INDEPENDENT LIVING LLC' AND date > '2025-06-30'")
chk("paid after nonprofit dissolution, $", 5908174.45, round(t, 2)); chk("paid after nonprofit dissolution, n", 778, n)
n, t = one(IN_BHA)
chk("entity 271533104 lifetime total", 73504622.08, round(t, 2))

print("\n" + "=" * 118)
print("D. THE CLAIMS CHECKED AGAINST THE ORIGINAL POST")
print("=" * 118)
n, t = one("vendor='BEYOND INDEPENDENT LIVING LLC' AND budget_fiscal_year >= 2017 AND date <= '2026-01-21'")
chk("BIL FY2017+ at the post date", 28730378.83, round(t, 2))
n, t = one(IN + " AND date='2025-01-16'")
chk("payments on 2025-01-16 (post claims one)", 0, n)
hits = q(select="count(1) as n", where="amount = 121728.16")[0]["n"]
chk("rows anywhere in CTHRU with amount 121728.16", "0", hits)
n, t = one("vendor='BEYOND INDEPENDENT LIVING LLC' AND date='2026-01-16'")
chk("2026-01-16 BIL $", 172708.26, round(t, 2)); chk("2026-01-16 BIL payments", 13, n)
n, t = one(IN + " AND date='2026-01-16'")
chk("2026-01-16 whole-group $", 190165.88, round(t, 2))

print("\n" + "=" * 118)
print("E. THE EXCLUSIONS (must stay out of the total)")
print("=" * 118)
for v, en, et in [("BEYOND ADULT DAY HEALTH CENTER, LLC", 616, 2048436.95),
                  ("BEYOND TRANSPORTATION LLC", 157, 124799.78),
                  ("MEDICAL COMMUNITY PSYCHOTHERAPY LLC", 56, 10851.69)]:
    n, t = one("vendor='%s'" % v)
    chk("%s $" % v[:34], et, round(t, 2)); chk("%s n" % v[:34], en, n)

print("\n" + "=" * 118)
print("F. THE README FISCAL-YEAR TABLE, ROW BY ROW")
print("=" * 118)
pubfy = {2011: (2, 875), 2012: (13, 3444), 2013: (152, 4654499), 2014: (207, 13229976),
         2015: (202, 17473028), 2016: (286, 13811313), 2017: (451, 9209113), 2018: (534, 7202340),
         2019: (516, 5290282), 2020: (546, 4123965), 2021: (628, 4522195), 2022: (679, 4904932),
         2023: (706, 5015271), 2024: (662, 5044840), 2025: (722, 5139962), 2026: (888, 5157241),
         2027: (186, 1172732)}
live = {int(r["budget_fiscal_year"]): (int(r["n"]), f(r["total"]))
        for r in q(select="budget_fiscal_year,count(1) as n,sum(amount) as total", where=IN,
                   group="budget_fiscal_year", order="budget_fiscal_year", limit=50)}
chk("fiscal years present", sorted(pubfy), sorted(live))
for y in sorted(pubfy):
    en, et = pubfy[y]; n, t = live.get(y, (0, 0.0))
    chk("FY%d n" % y, en, n); chk("FY%d $ (rounded)" % y, et, round(t), tol=0.51)
chk("FY table sums to the grand total", 105956006.17, round(sum(v[1] for v in live.values()), 2))

print("\n" + "=" * 118)
print("G. THE ENTITY REGISTER")
print("=" * 118)
ents = list(csv.DictReader(open(REPO + "data/entities.csv", encoding="utf-8")))
os_ = {e["soc_id"] for e in ents if e["filed_under"] in ("Osagiede", "both")}
eg_ = {e["soc_id"] for e in ents if e["filed_under"] in ("Egah", "both")}
chk("entity rows in the CSV", 45, len(ents))
chk("unique SoC ids (no duplicate rows)", 45, len({e["soc_id"] for e in ents}))
chk("Osagiede-listed", 20, len(os_)); chk("Egah-listed", 26, len(eg_))
chk("true overlap", 1, len(os_ & eg_))
chk("union", 45, len(os_ | eg_))
chk("with an involuntary dissolution", 27, sum(1 for e in ents if e["involuntary_dissolution"].strip()))
chk("ceased by conversion", 3, sum(1 for e in ents if e["ceased_by_conversion"].strip()))
chk("HTML register table rows", 45, HTML.count('<tr><td>') + HTML.count('<tr class="paid"><td>'))
for sid, fld, val in [("271533104", "involuntary_dissolution", "2023-12-29"), ("271533104", "revived", "2024-09-20"),
                      ("001309461", "involuntary_dissolution", "2025-06-30"), ("001421873", "organized", "2020-01-22"),
                      ("462941036", "ceased_by_conversion", "2017-02-21"), ("462612399", "involuntary_dissolution", "2017-06-30")]:
    row = next(e for e in ents if e["soc_id"] == sid)
    chk("%s %s" % (sid, fld), val, row[fld])

print("\n" + "=" * 118)
print("H. CHART DATA vs LIVE (the SVGs are hand-built, so the numbers in them must be re-checked)")
print("=" * 118)
GROUPS = {"Beyond Healthcare Agency": BHA, "Beyond Independent Living": ["BEYOND INDEPENDENT LIVING LLC"],
          "Greater Boston Home Health Care": ["GREATER BOSTON HOME HEALTH CARE LLC"]}
c1live = {}
for name, vs in GROUPS.items():
    w = "vendor in(%s)" % ",".join("'%s'" % v for v in vs)
    for r in q(select="budget_fiscal_year,sum(amount) as total", where=w, group="budget_fiscal_year", order="budget_fiscal_year", limit=40):
        c1live.setdefault(int(r["budget_fiscal_year"]), {})[name] = f(r["total"])
# chart 1 prints a rounded total above each bar; re-derive those labels
def money(v):
    return "$%.1fM" % (v / 1e6) if v >= 1e6 else ("$%.0fK" % (v / 1e3) if v >= 1e3 else "$%.0f" % v)
bad = []
for y in range(2013, 2028):
    lab = money(sum(c1live.get(y, {}).values()))
    if ">%s</text>" % lab not in HTML: bad.append((y, lab))
chk("chart 1 bar labels all match live data", [], bad)
# chart 2 in-window note
n2, t2 = one(IN_BHA + " AND date > '2023-12-29' AND date < '2024-09-20'")
m = re.search(r'>\$([\d,]+) paid across (\d+) payments while the company had no legal existence<', HTML)
chk("chart 2 note figure", "%,d" % round(t2) if False else format(round(t2), ","), m.group(1) if m else "NOT FOUND")
chk("chart 2 note payment count", str(n2), m.group(2) if m else "NOT FOUND")
# chart 3 counts
import collections
form = collections.Counter(); diss = collections.Counter()
for e in ents:
    if e["organized"].strip(): form[int(e["organized"][:4])] += 1
    if e["involuntary_dissolution"].strip(): diss[int(e["involuntary_dissolution"][:4])] += 1
chk("chart 3 formations total (2013-2026)", 43, sum(v for k, v in form.items() if 2013 <= k <= 2026))
chk("chart 3 dissolutions total", 27, sum(diss.values()))
chk("chart 3 peak dissolution year", 2025, max(diss, key=diss.get))
chk("chart 3 peak dissolution count", 10, max(diss.values()))

print("\n" + "=" * 118)
print("I. INTERNAL CONSISTENCY OF THE PROSE")
print("=" * 118)
for doc, nm in [(README, "README"), (HTML, "index.html")]:
    chk("%s states 45 entities" % nm, True, "45" in doc and "44 entit" not in doc)
    chk("%s states the grand total" % nm, True, "105,956,006" in doc)
    chk("%s keeps the auditor's wording" % nm, True, "appear to be unallowable" in doc)
    chk("%s carries the no-fraud-alleged line" % nm, True,
        ("no wrongdoing" in doc.lower()) or ("None of this establishes fraud" in doc))
    chk("%s carries the batch-dissolution caveat" % nm, True,
        ("batch" in doc.lower()) or ("scheduled sweep" in doc.lower()))

print("\n" + "=" * 118)
print("J. THE FEDERAL RECORD (IRS revocations, NPPES, and the two null searches)")
print("=" * 118)
import ssl, urllib.request, io, zipfile
_CTX = ssl.create_default_context(); _CTX.check_hostname = False; _CTX.verify_mode = ssl.CERT_NONE
def _get(u, raw=False, timeout=600):
    rq = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(rq, timeout=timeout, context=_CTX) as fh:
        d = fh.read()
    return d if raw else json.loads(d.decode())

# --- the seven federal billing numbers, re-queried live
npis = list(csv.DictReader(open(REPO + "data/npi-registry.csv", encoding="utf-8")))
chk("NPI rows on file", 7, len(npis))
for row in npis:
    live = _get("https://npiregistry.cms.hhs.gov/api/?version=2.1&number=%s" % row["npi"], timeout=180)
    if not live.get("results"):
        chk("NPI %s resolves" % row["npi"], True, False); continue
    b = live["results"][0]["basic"]
    off = (b.get("authorized_official_first_name", "") + " " + b.get("authorized_official_last_name", "")).strip()
    chk("NPI %s status still active" % row["npi"], "A", b.get("status"))
    chk("NPI %s not deactivated" % row["npi"], "", b.get("deactivation_date") or "")
    chk("NPI %s authorized official" % row["npi"], row["authorized_official"], off)
    chk("NPI %s in the page" % row["npi"], True, row["npi"] in HTML)

# --- IRS automatic revocations, re-downloaded and re-scanned
rev = list(csv.DictReader(open(REPO + "data/irs-revocations.csv", encoding="utf-8")))
chk("IRS revocation rows on file", 8, len(rev))
chk("distinct EINs revoked", 7, len({r["ein"] for r in rev}))
chk("rows with no reinstatement", 6, sum(1 for r in rev if not r["reinstatement_date"].strip()))
try:
    z = zipfile.ZipFile(io.BytesIO(_get("https://apps.irs.gov/pub/epostcard/data-download-revocation.zip", raw=True)))
    txt = z.read(z.namelist()[0]).decode("latin-1").splitlines()
    chk("IRS revocation file line count as published", 1247140, len(txt), tol=0)
    want = {r["ein"] for r in rev}
    got = {}
    for line in txt:
        e = line.split("|", 1)[0].strip()
        if e in want: got.setdefault(e, []).append(line)
    chk("all published EINs still on the IRS revocation list", sorted(want), sorted(got))
    chk("total rows the IRS returns for those EINs", 8, sum(len(v) for v in got.values()))
    for r in rev:
        f = [x.strip() for x in next(l for l in got[r["ein"]]
             if [y.strip() for y in l.split("|")][9] == r["revocation_date"]).split("|")]
        chk("EIN %s revoked %s" % (r["ein"], r["revocation_date"]), r["posting_date"], f[10])
except Exception as e:
    chk("IRS revocation file re-download", "ok", "ERROR: %s" % e)

# --- the two null searches must still be null
try:
    leie = _get("https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv", raw=True).decode("latin-1")
    rdr = list(csv.DictReader(io.StringIO(leie)))
    chk("LEIE record count as published", 84001, len(rdr), tol=0)
    hits = [r for r in rdr
            if "OSAGIEDE" in (r.get("LASTNAME") or "").upper()
            or (r.get("LASTNAME") or "").upper().strip() == "EGAH"
            or any(k in (r.get("BUSNAME") or "").upper() for k in
                   ("BEYOND HEALTHCARE", "BEYOND INDEPENDENT", "GREATER BOSTON HOME HEALTH",
                    "ALWAYS AVAILABLE HEALTH", "COMMUNITY PSYCH HEALTH", "BEYOND ZOE"))]
    chk("HHS-OIG exclusions for this web", 0, len(hits))
except Exception as e:
    chk("LEIE re-download", "ok", "ERROR: %s" % e)

sj = q(select="count(1) as n", where=("upper(payee_name) like '%25BEYOND%25' OR upper(payee_name) like '%25OSAGIEDE%25' "
                                      "OR upper(payee_name) like '%25EGAH%25'"), dataset="gpqz-7ppn")
chk("Comptroller settlements/judgments naming this web", "0", sj[0]["n"])

# --- the claim that ties the two registers together
ents_by_id = {e["soc_id"]: e for e in ents}
chk("EIN 462941036 is also a SoC entity id", True, "462941036" in ents_by_id)
chk("  and that entity is the $32.4M payee", "BEYOND INDEPENDENT LIVING LLC", ents_by_id.get("462941036", {}).get("entity", ""))
for doc, nm in [(README, "README"), (HTML, "index.html")]:
    chk("%s cites the IRS revocation" % nm, True, "462941036" in doc and "15 May 2021" in doc)
    chk("%s cites the null exclusion search" % nm, True, "84,001" in doc)
    chk("%s keeps the no-enforcement-action line" % nm, True, "no enforcement action" in doc.lower())

print()
print("=" * 118)
print("K. SOURCING DISCIPLINE (every rule-shaped claim must carry a citation)")
print("=" * 118)
import re as _re
for doc, nm in [(README, "README"), (HTML, "index.html")]:
    prose = chr(10).join(l for l in doc.split(chr(10)) if not l.strip().startswith("|"))
    hedges = _re.findall(r"(ordinarily|generally|typically|usually)", prose, _re.I)
    chk("%s free of unsourced hedge words" % nm, [], [h.lower() for h in hedges])
    chk("%s cites 130 CMR 450.212 (provider eligibility)" % nm, True, "450.212" in doc)
    chk("%s cites 130 CMR 450.231 (conditions of payment)" % nm, True, "450.231" in doc)
    chk("%s cites 130 CMR 450.235 (duty to return overpayments)" % nm, True, "450.235" in doc)
    chk("%s cites 130 CMR 450.237 (overpayment determination)" % nm, True, "450.237" in doc)
    chk("%s cites the dissolution statutes" % nm, True, "156D" in doc and "156C" in doc)
    chk("%s states the 90-day cure period" % nm, True, "90-day cure" in doc)
    chk("%s no longer asserts a dissolution schedule" % nm, False, "scheduled batches" in doc)
    chk("%s no longer asserts an offset mechanism" % nm, False, "nets recoveries" in doc)

print()
print("=" * 118)
print("L. SCOPE STATEMENT (a reader must be able to see where the work stops)")
print("=" * 118)
for doc, nm in [(README, "README"), (HTML, "index.html")]:
    chk("%s carries a scope section" % nm, True, "Scope of this check" in doc)
    chk("%s bounds the CMR reading to four sections" % nm, True,
        all(x in doc for x in ("450.212", "450.231", "450.235", "450.237")) and "bounded to those four sections" in doc)
    chk("%s states nobody was contacted" % nm, True, "was contacted" in doc)
    chk("%s states no wrongdoing is alleged" % nm, True, "wrongdoing" in doc.lower())
    chk("%s disclaims legal advice" % nm, True, "nothing here is legal advice" in doc.lower())
    chk("%s gives the retrieval date" % nm, True, "20 September 2026" in doc)

print("\n" + "=" * 118)
fails = [r for r in results if not r[0]]
print("RESULT: %d checks, %d passed, %d FAILED" % (len(results), len(results) - len(fails), len(fails)))
for _, lab, e, a in fails:
    print("   FAIL  %-52s published=%s  live=%s" % (lab, e, a))
sys.exit(1 if fails else 0)
