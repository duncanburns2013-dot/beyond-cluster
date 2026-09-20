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
| [`data/findings.json`](data/findings.json) | Machine-readable verdicts with evidence per claim |
| [`scripts/soda.py`](scripts/soda.py) | The Socrata query helper — reproduce any figure here |

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
