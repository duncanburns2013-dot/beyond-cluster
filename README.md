# The Beyond Cluster

**A public-records check on 45 Massachusetts corporate entities and $105.9M in MassHealth payments.**

📄 **[Read the formatted memo →](https://duncanburns2013-dot.github.io/beyond-cluster/)**

Everything is also on this page. The tables below are the findings; the raw data is in [`data/`](data/).

---

## What this is

On 21 January 2026, [@Ryan_Arthur_xyz](https://x.com/Ryan_Arthur_xyz/status/2014115608476950664) alleged that one person's companies had drawn roughly $103 million from MassHealth since 2016 while repeatedly being dissolved by the Secretary of the Commonwealth, and after a state audit flagged $887,225 in questionable billing.

This repository is the verification. Every claim was checked against the body that produces the record — not against news coverage, not against a summary.

**Checked 20 September 2026. Payment data current to 17 September 2026.**

### Sources, all primary

| Source | What it gave |
|---|---|
| CTHRU Comptroller of the Commonwealth Spending — Socrata `pegc-naaa`, 49,009,712 rows, updated 2026-09-19 | Every state payment, by vendor, date, appropriation and city |
| MA Secretary of the Commonwealth, Corporations Division | All 45 entity summaries, pulled individually |
| Office of the State Auditor, [audit published 21 Sep 2020](https://www.mass.gov/audit/audit-of-the-office-of-medicaid-masshealth-review-of-claims-paid-for-services-by-beyond-healthcare-agency-llc) | The $887,225 finding, verbatim |
| IRS Automatic Revocation of Exemption list, 1,247,140 records | Every 501(c)(3) in this web, and the date each lost exemption |
| IRS Exempt Organization Business Master File, Massachusetts, 44,035 records | Confirmation that none of them holds exemption today |
| NPPES national provider registry (CMS) | The federal billing numbers, their authorized officials and their status |
| HHS-OIG List of Excluded Individuals and Entities, 84,001 records | Checked: **no exclusions** |
| Comptroller's Settlements and Judgments file, 7,999 records | Checked: **no settlement or judgment** |

Two stale mirrors of the spending dataset exist under the same schema (`f7y8-q6ex`, `2bxs-ytms`) and were **not** used.

---

## Headline numbers

| | |
|---|---|
| Total state payments, six vendor identities | **$105,956,006.17** |
| Payments | **7,380** (2011-05-25 → 2026-09-17) |
| Entities registered under Naomi Osagiede or Naomi Egah | **45** |
| …carrying at least one involuntary dissolution | **27** |
| Paid to the audited company *while it stood dissolved* | **$643,388.39** |
| Recoupment visible anywhere in the ledger | **$0.00** |

---

## Verdicts

| Claim | Verdict | What the records say |
|---|---|---|
| $103,000,000 **since 2016** | ⚠️ Right size, wrong frame | $102,287,219 all-time at the post date — within 0.7%. But since 2016 is only **$62,897,039**; ~41% predates 2016. |
| BIL received >$29M FY2017–early 2026 | ⚠️ Slightly over then, true now | $28,730,379 at the post date. $32,404,181 now. |
| **$121,728.16 on 16 Jan 2025** | ❌ **Fails** | No payment that day. No row in 49M carries that amount. Nearest: 16 Jan **2026**, $172,708.26. |
| State audit flagged $887,225 | ✅ Exact | Published 21 Sep 2020, period 2016-01-01→2018-12-31. But the auditor says *"appear to be unallowable"*, not "fraudulent". |
| 12–15 entities | ✅ Understated | **45**. |
| Vast majority involuntarily dissolved | ✅ Confirmed | **27 of 45** (60%). |
| Charter revoked Feb 2025 | ⚠️ Date differs | Register says **30 June 2025**. February fits the notice. |
| Registered to 661 Centre St on 22 Jan 2020 | ✅ Exact | Entity `001421873`, organised 22 Jan 2020, 661 Centre St **Brockton**, agent **Naomi Egah**. |
| "The money keeps flowing" | ✅ Confirmed | **$3,608,847** paid since the post. Latest payment 17 Sep 2026. |

---

## The finding that ties it together

The post asserts Naomi Osagiede also files as Naomi Egah. That is not inference — it is on a single filing.

**Beyond Faith Consulting, LLC — entity `463474045`**, at 1208B VFW Parkway, Suite 304, Boston 02132:

```
MANAGER        →  NAOMI EGAH
SOC SIGNATORY  →  NAOMI EGAH
REAL PROPERTY  →  ADERONKE NAOMI OSAGIEDE
REAL PROPERTY  →  NAOMI EGAH
MANAGER        →  BEYOND BUSINESS MANAGEMENT INC   (Suite 301)
```

Searching only `OSAGIEDE` returns 20 entities. Searching `EGAH` returns 26. One overlaps — Beyond Faith Consulting, the filing above. Anyone who searched one name and stopped saw less than half the structure.

That last line is a separate finding: an entity in this web is itself the registered manager of another entity in this web. The same nesting appears at Beyond Healthcare Agency LLC, whose managers are "Naomi A Osagiede" and an entity called **Beyond Trust** — which exists in the register as Beyond Trust Int LLC, filed under Egah.

---

## Where the money went

Six vendor identities in the Comptroller's file, mapping to three real businesses.

| Vendor string, exactly as the state spells it | City | Payments | Total | Span |
|---|---|---:|---:|---|
| `ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR` | Woburn | 1,432 | $63,247,375.74 | 2012–2018 |
| `BEYOND INDEPENDENT LIVING LLC` | Woburn → Methuen → West Roxbury | 4,038 | $32,404,181.08 | 2015–2026 |
| `BEYOND HEALTHCARE AGENCY LLC` | Andover | 1,391 | $5,868,134.35 | 2019–2026 |
| `ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE` | Andover | 424 | $4,385,632.99 | 2018–2019 |
| `GREATER BOSTON HOME HEALTH CARE LLC` | Boston → Brockton | 83 | $47,203.01 | 2025–2026 |
| `BEYOND HEATHCARE AGENCY` | Woburn | 12 | $3,479.00 | 2011–2012 |
| **Total** | | **7,380** | **$105,956,006.17** | **2011–2026** |

Rows 1, 3, 4 and 6 are **one company**. The Corporations Division name history for entity `271533104` records that Beyond Healthcare Agency LLC was legally named *Aderonke Naomi Osagiede Beyond Healthcare Agency LLC* until 14 October 2015; the payment system carried the old name for four more years. That single entity accounts for **$73.50 million**.

The largest block — $63.2M — is invisible to a plain search: the vendor string is truncated at 40 characters and misspells "Beyond" as **BEYONE**.

### By fiscal year, all six vendors

| FY | Payments | Total | | FY | Payments | Total |
|---|---:|---:|---|---|---:|---:|
| 2011 | 2 | $875 | | 2020 | 546 | $4,123,965 |
| 2012 | 13 | $3,444 | | 2021 | 628 | $4,522,195 |
| 2013 | 152 | $4,654,499 | | 2022 | 679 | $4,904,932 |
| 2014 | 207 | $13,229,976 | | 2023 | 706 | $5,015,271 |
| 2015 | 202 | **$17,473,028** | | 2024 | 662 | $5,044,840 |
| 2016 | 286 | $13,811,313 | | 2025 | 722 | $5,139,962 |
| 2017 | 451 | $9,209,113 | | 2026 | 888 | $5,157,241 |
| 2018 | 534 | $7,202,340 | | 2027 | 186 | $1,172,732 |
| 2019 | 516 | $5,290,282 | | | | |

---

## The federal record

The state register shows companies being struck off. The federal register shows the same
pattern, independently, and it is the harder of the two documents.

### Every 501(c)(3) in this web lost its exemption

The IRS publishes an Automatic Revocation of Exemption list: organisations whose tax-exempt
status was revoked under IRC 6033(j) for failing to file a return three years running.
Searching all 1,247,140 records returns eight rows, covering all seven of the nonprofits here.

| EIN | Organisation | Revoked | Posted | Reinstated |
|---|---|---|---|---|
| **462941036** | **BEYOND INDEPENDENT LIVING LLC** | **15 May 2021** | 9 Aug 2021 | no |
| 472476331 | Fire of Life Inc | 15 May 2022 | **17 Jan 2026** | no |
| 850730708 | Hope and Power Mega Church | 15 May 2023 | 14 Aug 2023 | no |
| 821341006 | Nkums World Outreach | 15 May 2020 | 11 Aug 2020 | no |
| 822091333 | Nigerian Nurses Association of Massachusetts | 15 May 2020 | 11 Aug 2020 | no |
| 822326336 | Embassy of Grace, A Place of Favor | 15 May 2020 | 11 Aug 2020 | no |
| 465109128 | Beyond Zoe Ministry | 15 May 2017 | 16 Aug 2017 | 15 May 2017 |
| 472476331 | Fire of Life *(first revocation)* | 15 May 2017 | 16 Aug 2017 | 15 May 2017 |

Two facts in that table carry weight beyond the rest.

**EIN 462941036 is the same number the Secretary of the Commonwealth uses as the
identification number for Beyond Independent Living LLC** — the vendor the Comptroller has
paid **$32,404,181**. Its exemption was revoked on 15 May 2021 for three consecutive years of
not filing. The Commonwealth has paid it every year since: $3.48M in FY2021, climbing to
$4.78M in FY2026.

**Fire of Life's second revocation was posted on 17 January 2026** — four days before the X
post that started this.

None of the seven EINs appears in the IRS's current Massachusetts exempt-organization master
file. I checked all 44,035 records by EIN and by name.

### Seven federal billing numbers, all still live

| NPI | Organisation | Authorized official | Practice address | Status | Last updated |
|---|---|---|---|---|---|
| 1003226630 | Beyond Independent Living LLC | **Naomi Osagiede**, Owner | 661 Centre St, Brockton | active | 23 Jun 2026 |
| 1003116021 | Beyond Healthcare Agency LLC | **Naomi Osagiede**, CEO | 10 New England Business Center Dr, Andover | active | 23 Jun 2026 |
| 1063691905 | Greater Boston Home Health Care LLC | **Naomi Osagiede**, Owner | 661 Centre St, Brockton | active | 24 Aug 2026 |
| 1255748281 | Community Psych Healthcare LLC | **Naomi Egah**, Owner | 661 Centre St, Brockton | active | 9 Oct 2024 |
| 1952723322 | Always Available Healthcare LLC | **Aderonke Osagiede**, CEO | 691 Main St, Waltham | active | 9 Jun 2014 |
| 1316376999 | Beyond Zoe Hospice LLC | **Aderonke Osagiede**, CEO | 10 Tower Office Park, Woburn | active | 3 Mar 2015 |
| 1700662186 | Healing Pathways Home Care LLC | Raquel Vargas, Owner/President | 101 Amesbury St, Lawrence | active | 1 Sep 2023 |

Every one carries status **A**. None has a deactivation date. That includes companies the
Commonwealth has struck off.

This table also settles the identity question a third time, and settles it in a federal
record rather than a state one. Community Psych Healthcare is filed under **Naomi Egah** with
a mailing address of **1208B VFW Parkway, West Roxbury** — the Osagiede hub — and shares the
telephone number **978-930-9410** with Always Available Healthcare, filed under **Aderonke
Osagiede**. Beyond Healthcare Agency and Beyond Zoe Hospice share **781-932-1166**.

Healing Pathways Home Care is the exception worth naming: Naomi Aderonke Egah is a manager on
the state filing, but the federal registry names a different authorized official. Treat it as
adjacent, not as hers.

### What the federal record does *not* show

Two searches came back empty, and both matter.

- **No exclusions.** The HHS-OIG List of Excluded Individuals and Entities, all 84,001
  records, returns nothing for Osagiede, for Egah, or for any of the business names. Nobody
  here is barred from federal health programmes.
- **No settlement, no judgment.** The Comptroller's own Settlements and Judgments file, 7,999
  records, returns nothing either.

**There is no enforcement action against anyone in this web anywhere on the public record.**
That is a fact about the file, and it belongs in any honest write-up of it.

---

## What is actually provable

Worth being exact about, because the gap between what the records show and what a reader will
assume is where this goes wrong.

**Provable from documents today, no inference:**

1. One person operates 45 Massachusetts entities under two filing names. Three independent
   records tie the names together, one of them federal.
2. Twenty-seven of those entities carry an involuntary dissolution.
3. All seven that held federal tax exemption lost it for failure to file.
4. The entity whose exemption was revoked in May 2021 has been paid $32.4M by the
   Commonwealth, $4.78M of it in FY2026 alone.
5. Beyond Healthcare Agency was paid $643,388 across 153 payments while it stood dissolved.
6. A 2020 state audit put up to $887,225 in apparently unallowable billing, and no recovery
   appears in any public file.
7. Every company here still holds an active federal billing number.

**Answerable with one more record, which nobody has yet:** whether MassHealth ever recouped
the $887,225, and whether provider enrolment lapsed during the dissolution. Both sit in
MassHealth's provider file. The public records request is the way to get them.

**Not provable by anyone outside government:** whether services were delivered, whether any
billing was knowingly false, and intent. Those need claims-level data and a subpoena.

The defensible claim is not that someone stole $103 million. It is that a single operator
with 45 companies, 27 administrative dissolutions, seven revoked exemptions and an unresolved
audit finding has been paid $105.9 million and is still being paid, and that no public body
appears to have looked. That is a demand for an audit, and the records carry it.

---

## What the original post missed

**1. The state paid the audited company while it was legally dissolved.**
Beyond Healthcare Agency LLC was involuntarily dissolved on **29 Dec 2023** and not revived until **20 Sep 2024**. Inside that nine-month window: **153 payments, $643,388.39**, from 8 Jan to 16 Sep 2024.

**2. Payments continue after the surviving corporate entity was dissolved.**
Since the Beyond Independent Living nonprofit was dissolved on 30 Jun 2025, a vendor named "Beyond Independent Living LLC" has taken **778 payments worth $5,908,174.45**, through 17 Sep 2026 — booked to West Roxbury 02132, the Osagiede address, not the separately registered Brockton LLC of the same name.

> ⚠️ Keep this caveat attached: a MassHealth provider number and a corporate charter are separate instruments, and a provider can stay enrolled through a filing lapse. The finding is that two of the state's own registers disagree. That is a question for MassHealth, not an answer.

**3. A new payee opened as the old one closed.**
**Greater Boston Home Health Care LLC** began drawing state money on **20 June 2025** — ten days before the nonprofit's dissolution. 83 payments, $47,203, still paid as of 17 Sep 2026. Payments start at Boston 02132 (the Osagiede address) and **move to Brockton 02302** — the 661 Centre St / Fire of Life address — during FY2026.

**4. No recoupment is visible anywhere.**
Across all 7,380 payments there is not one negative amount; the smallest line is $0.21.

> ⚠️ MassHealth ordinarily nets recoveries against future claims rather than posting a negative to the Comptroller's ledger. Absence is **not** proof nothing was repaid — which is exactly why the public records request is the right next step. Ask for the recoupment determination by name.

**5. Fire of Life checks out.** `FIRE OF LIFE. INC`, entity `001150418`, is a Chapter 180 religious corporation filed under Naomi Egah at a Brockton address.

---

## Corrections to the original post

| Entity | CTHRU total | Why it must come out |
|---|---:|---|
| `BEYOND ADULT DAY HEALTH CENTER, LLC` | $2,048,436.95 | Different company. Entity `001175773` was renamed **Vilaj Lajwa, LLC** on 6 Jul 2017; managers Victoria Vinokur, Paul Rayev, Gennady Vinokur of Waltham. |
| `BEYOND TRANSPORTATION LLC` | $124,799.78 | Methuen/Tewksbury. No officer link in the register. |
| `MEDICAL COMMUNITY PSYCHOTHERAPY LLC` | $10,851.69 | Natick. Substring collision with "Community Psych". |

---

## Read this before publishing anything

- **None of this establishes fraud.** An involuntary dissolution is a failure to file an annual report. The auditor's phrase is *"appear to be unallowable"* — an upper-bound estimate, not an adjudicated finding. Every sentence should survive being read by a lawyer for the other side.
- **The clustered dissolution dates are the state's calendar, not an event.** The Corporations Division dissolves delinquent entities in scheduled batches — late June for corporations, late December for LLCs. Five entities share 28 Jun 2019 and five share 30 Jun 2025. Report the **count**, not the coincidence.
- **$105.9M is a floor, not a ceiling.** CTHRU records Comptroller disbursements. MassHealth fee-for-service claims appear; care paid through an MCO or ACO generally does not.
- **Appropriation labels are accounting buckets.** "Managed Care Plan", "MassHealth Senior Care", "Indemnity / Third Party Liability Plan" describe which account the money left, not which service was billed.
- **41 of the 45 entities show no state payment at all.** The money maps to three businesses across six vendor strings. Two of the 45 are identically named Greater Boston Home Health Care LLCs, and because CTHRU carries no entity ID the $47,203 cannot be attributed between them.
- **Other people share these surnames.** The Osagiede search returns filings by at least a dozen other individuals — an attorney, a shipping company, several churches. Only the 45 entities in [`data/entities.csv`](data/entities.csv) carry Naomi Osagiede or Naomi Egah as an officer, manager, agent or signatory.

---

## Files

| Path | Contents |
|---|---|
| [`index.html`](index.html) | The full memo, formatted |
| [`data/entities.csv`](data/entities.csv) | All 45 entities — SoC ID, type, organised, dissolved, revived, city, which name it was filed under, and a note where attribution is uncertain |
| [`data/payments-by-fiscal-year.csv`](data/payments-by-fiscal-year.csv) | Every vendor × fiscal year × city, with counts and totals |
| [`data/payments-by-appropriation.csv`](data/payments-by-appropriation.csv) | Every vendor × appropriation × department |
| [`data/irs-revocations.csv`](data/irs-revocations.csv) | The eight rows these EINs return from the IRS Automatic Revocation list |
| [`data/npi-registry.csv`](data/npi-registry.csv) | The seven federal billing numbers, officials, addresses and status |
| [`data/findings.json`](data/findings.json) | Machine-readable verdicts with evidence per claim |
| [`scripts/soda.py`](scripts/soda.py) | The Socrata query helper — reproduce any figure here |
| [`scripts/audit.py`](scripts/audit.py) | **The accuracy audit.** Re-derives all 162 published figures from the live API and the register, and fails if any disagree |

### Checking this page

Every figure here is machine-checked. `scripts/audit.py` re-queries the live Comptroller
dataset and re-reads the entity register, then compares each result against the number as
published in this README, in `index.html`, and inside the hand-built chart SVGs. It exits
non-zero if anything disagrees.

```bash
cd scripts && python audit.py
# RESULT: 162 checks, 162 passed, 0 FAILED
```

Figures move as the Commonwealth pays more money, so a re-run will legitimately diverge on
the running totals. What it must never show is an internal disagreement — a number in the
prose that the data does not support.

### Reproducing a figure

```python
from soda import q, f
SIX = ["ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR","ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE",
       "BEYOND HEALTHCARE AGENCY LLC","BEYOND INDEPENDENT LIVING LLC","BEYOND HEATHCARE AGENCY",
       "GREATER BOSTON HOME HEALTH CARE LLC"]
IN = "vendor in(%s)" % ",".join("'%s'" % v for v in SIX)
print(q(select="count(1) as n,sum(amount) as total", where=IN))
```

Entity records are at `corp.sec.state.ma.us` — search by ID number using the values in `data/entities.csv`.

---

*No wrongdoing by any named individual is alleged. Every record cited is a public filing or a public payment disclosure made by the Commonwealth of Massachusetts.*
