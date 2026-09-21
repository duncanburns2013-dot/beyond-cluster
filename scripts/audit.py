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
fails = [r for r in results if not r[0]]
print("RESULT: %d checks, %d passed, %d FAILED" % (len(results), len(results) - len(fails), len(fails)))
for _, lab, e, a in fails:
    print("   FAIL  %-52s published=%s  live=%s" % (lab, e, a))
sys.exit(1 if fails else 0)
