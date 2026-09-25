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
chk("latest payment date (date field, load-dependent)", "2026-09-21", r["l"][:10]); chk("earliest payment date", "2011-05-25", r["f"][:10])
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
chk("ceased by conversion or merger", 4, sum(1 for e in ents if e["ceased_by_conversion"].strip()))
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
m = re.search(r'>\$([\d,]+) paid across (\d+) payment lines while the company stood administratively dissolved<', HTML)
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
import ssl, urllib.request, urllib.parse, io, zipfile, time
_CTX = ssl.create_default_context(); _CTX.check_hostname = False; _CTX.verify_mode = ssl.CERT_NONE
def _get(u, raw=False, timeout=600):
    rq = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(rq, timeout=timeout, context=_CTX) as fh:
        d = fh.read()
    return d if raw else json.loads(d.decode())

# --- every billing number in data/npi-registry.csv, re-queried live
npis = list(csv.DictReader(open(REPO + "data/npi-registry.csv", encoding="utf-8")))
chk("NPI rows on file", 16, len(npis))
for row in npis:
    time.sleep(1.5)  # NPPES answers 403 to bursts
    live = _get("https://npiregistry.cms.hhs.gov/api/?version=2.1&number=%s" % row["npi"], timeout=180)
    if not live.get("results"):
        chk("NPI %s resolves" % row["npi"], True, False); continue
    b = live["results"][0]["basic"]
    off = (b.get("authorized_official_first_name", "") + " " + b.get("authorized_official_last_name", "")).strip()
    chk("NPI %s status still active" % row["npi"], "A", b.get("status"))
    chk("NPI %s not deactivated" % row["npi"], "", b.get("deactivation_date") or "")
    if row.get("tie") == "confirmed":  # other officials are withheld from the published file
        chk("NPI %s authorized official" % row["npi"], row["authorized_official"], off)
    chk("NPI %s in the page" % row["npi"], True, row["npi"] in HTML)

# --- IRS automatic revocations, re-downloaded and re-scanned
rev = list(csv.DictReader(open(REPO + "data/irs-revocations.csv", encoding="utf-8")))
chk("IRS revocation rows on file", 11, len(rev))
chk("distinct EINs revoked", 10, len({r["ein"] for r in rev}))
chk("rows with no reinstatement", 9, sum(1 for r in rev if not r["reinstatement_date"].strip()))
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
    chk("total rows the IRS returns for those EINs", 11, sum(len(v) for v in got.values()))
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

sj = q(select="count(1) as n", where=("upper(payee_name) like '%BEYOND%' OR upper(payee_name) like '%OSAGIEDE%' "
                                      "OR upper(payee_name) like '%EGAH%'"), dataset="gpqz-7ppn")
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
print("M. THE 25 SEPTEMBER UPDATE (federal record, new strings, second window)")
print("=" * 118)
import os
from soda import f  # section J reuses the name f for a list; restore the number parser
skips = []
def skip(label, why):
    skips.append(label); print("SKIP  %-58s %s" % (label, why))

# --- CTHRU: new strings, windows, reconciliation years
n, t = one(IN + " AND date >= '2016-01-01' AND date <= '2026-01-21'"); chk("since 2016 through the post date $", 59288191.46, round(t, 2))
n, t = one(IN + " AND date < '2016-01-01'"); chk("before 2016 $", 42999027.68, round(t, 2))
n, t = one(IN + " AND date IS NULL"); chk("undated lines in the six strings", 9, n); chk("undated total", 59939.61, round(t, 2))
pid = q(select="count(distinct payment_id) as p", where=IN)[0]["p"]; chk("distinct payment ids behind 7,380 lines", "1868", pid)
G = "vendor='GR. BOSTON HOME HLTH LLC'"
n, t = one(G);                                   chk("GR. BOSTON all-time $", 2017617.52, round(t, 2)); chk("GR. BOSTON all-time lines", 1248, n)
n, t = one(G + " AND date <= '2015-07-16'");     chk("GR. BOSTON before the 2015 sale $", 1563932.85, round(t, 2))
n, t = one(G + " AND date > '2015-07-16'");      chk("GR. BOSTON after the sale, dated $", 400709.69, round(t, 2))
n, t = one(G + " AND date IS NULL");             chk("GR. BOSTON undated (FY2021-22) $", 52974.98, round(t, 2))
n, t = one("vendor='BEYOND ADULT DAY HEALTH CENTER, LLC' AND date < '2017-02-22'")
chk("Beyond ADHC while Osagiede managed it $", 101510.19, round(t, 2)); chk("Beyond ADHC while Osagiede managed it, lines", 23, n)
n, t = one("vendor='BEYOND ADULT DAY HEALTH CENTER, LLC' AND date >= '2017-02-22'"); chk("Beyond ADHC after 2017-02-22 $", 1946926.76, round(t, 2))
n, t = one("vendor='VILAJ LAJWA ADHC, LLC'"); chk("Vilaj Lajwa ADHC $ (moves with new payments)", 3729881.81, round(t, 2))
n, t = one(IN_BHA + " AND date > '2019-06-28' AND date < '2019-10-10'")
chk("BHA 2019 window $", 730589.08, round(t, 2)); chk("BHA 2019 window lines", 81, n)
n2, t2 = one(IN_BHA + " AND date > '2023-12-29' AND date < '2024-09-20'")
chk("both dissolution windows $", 1373977.47, round(t + t2, 2)); chk("both windows lines", 234, n + n2)
Y = " AND date >= '2018-01-01' AND date <= '2024-12-31'"
# undated lines count toward 2018-2024 when their budget fiscal year falls inside it (FY2019-FY2024)
YU = " AND ((date >= '2018-01-01' AND date <= '2024-12-31') OR (date IS NULL AND budget_fiscal_year >= 2019 AND budget_fiscal_year <= 2024))"
n, t = one("vendor='BEYOND INDEPENDENT LIVING LLC'" + Y); chk("BIL CTHRU 2018-2024 $", 22130538.18, round(t, 2))
n, t = one(IN_BHA + YU);                                    chk("BHA CTHRU 2018-2024 $", 12711139.06, round(t, 2))
n, t = one(G + YU);                                         chk("GR. BOSTON CTHRU 2018-2024 $", 253725.31, round(t, 2))
n, t = one("vendor='BEYOND INDEPENDENT LIVING LLC' AND appropriation_name like '%MANAGED CARE PLAN%'" + Y)
chk("BIL Managed Care Plan account 2018-2024 $", 5146623.26, round(t, 2))

# --- CMS Medicare payments (PAC PUF by provider, one dataset per year)
PUF = {2014: "28544ea6-d53c-4fd6-a85c-1457ac7872c3", 2015: "42ec5f14-9c41-405a-8450-eda5f4161525", 2016: "5e931266-c5ea-447e-884d-43c30d581fba",
       2017: "9993352b-2ea4-4375-afb6-c7711fe66e04", 2018: "7d6f3161-1768-4796-91a8-42f4930a5ff6", 2019: "5c063a22-c9f6-4402-bacb-853b8d49a819",
       2020: "e968ecf6-cef3-4b75-ae40-460273d3844e", 2021: "35416e1b-b805-464f-a376-d2ed04e2574b", 2022: "672e81ea-f675-4f48-ae2e-e4492d996a3f",
       2023: "51d84821-8fc0-45ce-820c-38be22d1736f", 2024: "7013adbd-3cf9-4a64-a61f-d7d65a0eaa97"}
def puf(ccn, years):
    out = {}
    for y in years:
        rows = _get("https://data.cms.gov/data-api/v1/dataset/%s/data?filter[PRVDR_ID]=%s" % (PUF[y], ccn), timeout=180)
        prov = [r for r in rows if (r.get("SMRY_CTGRY") or "").upper() == "PROVIDER"] or rows
        if prov: out[y] = int(float(prov[0]["TOT_MDCR_PYMT_AMT"]))
    return out
try:
    g = puf("227507", range(2014, 2025))
    chk("Medicare GBHHC years with a row", 11, len(g))
    chk("Medicare GBHHC CY2014-2024 $", 15333781, sum(g.values()))
    chk("Medicare GBHHC CY2016-2024 $", 13673342, sum(v for k, v in g.items() if k >= 2016))
    chk("Medicare BHA rows (CY2015 only)", {2015: 82133}, puf("227541", range(2014, 2025)))
    chk("Medicare Eden CY2015-2018 $", 622931, sum(puf("677975", range(2015, 2019)).values()))
except Exception as e:
    chk("CMS PUF reachable", "ok", "ERROR: %s" % e)

# --- CMS PECOS owners, associate 1254592256
try:
    own = _get("https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data?filter[ASSOCIATE%20ID%20-%20OWNER]=1254592256", timeout=180)
    pct = {(r["ENROLLMENT ID"], r["ASSOCIATION DATE - OWNER"]) for r in own if r.get("ROLE TEXT - OWNER", "").startswith("5% OR GREATER DIRECT")}
    chk("PECOS: Egah 100% owner rows (BHA, GBHHC, PA)", 3, len(pct))
    chk("PECOS: owner name", {"EGAH"}, {r["LAST NAME - OWNER"] for r in own})
    eden = _get("https://data.cms.gov/data-api/v1/dataset/94c1d434-bdad-47e5-b301-6bcf8634af6b/data?filter[ENROLLMENT%20ID]=O20150912000320", timeout=180)
    chk("PECOS 2023: Eden owned by 1254592256 from 2014-08-22", True, any(r["ASSOCIATE ID - OWNER"] == "1254592256" and r["ASSOCIATION DATE - OWNER"] == "2014-08-22" for r in eden))
except Exception as e:
    chk("CMS PECOS reachable", "ok", "ERROR: %s" % e)

# --- HRSA Provider Relief Fund
try:
    prf = 0
    for s, st in [("BEYOND%20HEALTHCARE", "MA"), ("BEYOND%20INDEPENDENT", "MA"), ("GREATER%20BOSTON%20HOME%20HEALTH", "MA"), ("GUARANTEED%20HOME%20HEALTH", "PA")]:
        for r in _get("https://data.cdc.gov/resource/kh8y-3es6.json?$q=%s" % s, timeout=180):
            if r.get("state") == st: prf += int(r["payment"].replace("$", "").replace(",", ""))
    chk("HHS Provider Relief Fund, four payees $", 169199, prf)
except Exception as e:
    chk("HRSA PRF reachable", "ok", "ERROR: %s" % e)

try:
    aap = _get("https://data.cdc.gov/resource/v2pi-w3up.json?$where=" + urllib.parse.quote("upper(provider_name) like '%GREATER BOSTON HOME%'"), timeout=180)
    chk("Medicare accelerated/advance payment, GBHHC $", 463529.01, sum(float(r.get("aap") or 0) for r in aap if r.get("state_territory") == "Massachusetts"))
except Exception as e:
    chk("HHS AAP file reachable", "ok", "ERROR: %s" % e)

# --- SBA files (local; skipped when absent)
SBA = os.environ.get("BEYOND_SBA_DIR", "")
ppp = os.path.join(SBA, "public_150k_plus_240930.csv")
if SBA and os.path.exists(ppp):
    got = {}
    with open(ppp, encoding="utf-8", errors="replace", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["LoanNumber"] in ("8009847100", "3390558708", "5267977702"):
                got[r["LoanNumber"]] = (float(r["CurrentApprovalAmount"]), float(r["ForgivenessAmount"] or 0))
    chk("PPP GBHHC two loans $", 2369200.0, got.get("8009847100", (0, 0))[0] + got.get("3390558708", (0, 0))[0])
    chk("PPP GBHHC forgiven $", 2388640.42, round(got.get("8009847100", (0, 0))[1] + got.get("3390558708", (0, 0))[1], 2))
    chk("PPP Beyond Business Consulting $", 155107.0, got.get("5267977702", (0, 0))[0])
else:
    skip("SBA PPP checks", "set BEYOND_SBA_DIR to a folder holding public_150k_plus_240930.csv")
cov = list(csv.DictReader(open(REPO + "data/covid-federal.csv", encoding="utf-8")))
chk("EIDL entity loans in data file $", 1390000, sum(int(r["amount"]) for r in cov if r["program"] == "EIDL loan" and "individual" not in r["recipient_as_filed"]))
chk("EIDL advances in data file $", 66000, sum(int(r["amount"]) for r in cov if r["program"] == "EIDL advance"))

# --- HHS T-MSIS (local parquet; skipped when absent)
PQ = os.environ.get("BEYOND_TMSIS", "E:/hhs-tmsis/medicaid-provider-spending.parquet")
try:
    import duckdb
    have = os.path.exists(PQ)
except ImportError:
    have = False
if have:
    con = duckdb.connect()
    tm = dict(con.sql("SELECT BILLING_PROVIDER_NPI_NUM, round(sum(TOTAL_PAID::DECIMAL(38,2)),2) FROM '%s' WHERE BILLING_PROVIDER_NPI_NUM IN ('1003226630','1003116021','1063691905') GROUP BY 1" % PQ).fetchall())
    chk("T-MSIS BIL 2018-2024 $", 29101580.81, float(tm.get("1003226630", 0)))
    chk("T-MSIS BHA 2018-2024 $", 13234951.02, float(tm.get("1003116021", 0)))
    chk("T-MSIS GBHHC 2018-2024 $", 1143093.82, float(tm.get("1063691905", 0)))
    w24 = con.sql("SELECT round(sum(TOTAL_PAID::DECIMAL(38,2)),2) FROM '%s' WHERE BILLING_PROVIDER_NPI_NUM='1003116021' AND CLAIM_FROM_MONTH BETWEEN '2024-01' AND '2024-08'" % PQ).fetchone()[0]
    w19 = con.sql("SELECT round(sum(TOTAL_PAID::DECIMAL(38,2)),2) FROM '%s' WHERE BILLING_PROVIDER_NPI_NUM='1003116021' AND CLAIM_FROM_MONTH BETWEEN '2019-07' AND '2019-09'" % PQ).fetchone()[0]
    chk("T-MSIS BHA service months 2024-01..08 $", 653850.92, float(w24)); chk("T-MSIS BHA service months 2019-07..09 $", 744126.71, float(w19))
else:
    skip("HHS T-MSIS checks", "parquet not found at %s (set BEYOND_TMSIS)" % PQ)
tmf = list(csv.DictReader(open(REPO + "data/tmsis-by-npi-year.csv", encoding="utf-8")))
chk("T-MSIS data file BIL total", 29101580.81, round(sum(float(r["total_paid"]) for r in tmf if r["billing_npi"] == "1003226630"), 2))

# --- the page and the README carry the new figures
for fig in ("$453,684.67", "$1,373,977", "$13,673,342", "$29,101,580.81", "$730,589.08", "$101,510.19", "1254592256", "$2,369,200", "$1,390,000", "$169,199", "$622,931", "$463,529.01", "$59,288,191", "201540575070", "201661665430"):
    chk("page carries %s" % fig, True, fig in HTML)
for fig in ("$453,684.67", "$1,373,977.47", "$13,673,342", "$29,101,580.81", "1254592256", "$2,369,200", "$1,390,000", "$59,288,191"):
    chk("README carries %s" % fig, True, fig in README)
chk("page has 11 tab panels", 11, HTML.count('role="tabpanel" id='))
chk("page has no em dash", 0, HTML.count("&mdash;") + HTML.count("\u2014"))
if skips: print("\n%d check group(s) skipped: %s" % (len(skips), ", ".join(skips)))

print("\n" + "=" * 118)
fails = [r for r in results if not r[0]]
print("RESULT: %d checks, %d passed, %d FAILED" % (len(results), len(results) - len(fails), len(fails)))
for _, lab, e, a in fails:
    print("   FAIL  %-52s published=%s  live=%s" % (lab, e, a))
sys.exit(1 if fails else 0)
