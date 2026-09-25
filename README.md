# The Beyond Cluster

**A public-records check on 45 Massachusetts corporate entities, $105.9M in MassHealth payments from the state ledger, and the federal record behind them.**

📄 **[Read the formatted memo →](https://duncanburns2013-dot.github.io/beyond-cluster/)** The memo is split into tabs: Overview, Claims checked, State payments, Medicaid & Medicare, Greater Boston Home Health, COVID money, Identity, Register & IRS, Enforcement, Follow-ups, Corrections & method.

**First checked 20 September 2026. Updated 25 September 2026.** State payment data from the Comptroller's load of 25 September 2026, latest dated lines 21 September 2026.

---

## What this is

On 21 January 2026, [@Ryan_Arthur_xyz](https://x.com/Ryan_Arthur_xyz/status/2014115608476950664) alleged that one person's companies had drawn roughly $103 million from MassHealth since 2016 while repeatedly being dissolved by the Secretary of the Commonwealth, and after a state audit flagged $887,225 in questionable billing.

This repository is the verification. Every claim was checked against the body that produces the record, not against news coverage or a summary. The 25 September update adds the federal record: HHS Medicaid billing, CMS Medicare enrollment and payments, SBA COVID loans, HHS relief payments, a fuller NPI sweep, and a re-read of the corporate filings.

### Sources, all primary

| Source | What it gave |
|---|---|
| CTHRU Comptroller of the Commonwealth Spending, Socrata `pegc-naaa`, 49,022,699 rows, load of 2026-09-25 | Every state payment line, by vendor, date, appropriation and city |
| MA Secretary of the Commonwealth, Corporations Division | All 45 entity summaries, the name indexes of 20 and 24 September, and the filing documents behind the Greater Boston Home Health Care and Beyond Adult Day Health Center timelines |
| Office of the State Auditor, [audit published 21 Sep 2020](https://www.mass.gov/audit/audit-of-the-office-of-medicaid-masshealth-review-of-claims-paid-for-services-by-beyond-healthcare-agency-llc), and its Medicaid Audit Unit annual reports 2021 to 2026 | The $887,225 finding, verbatim, and the only public word on recoupment |
| HHS Open Data, *Medicaid Provider Spending by HCPCS* (T-MSIS), release of 9 Feb 2026, 238,015,729 rows | Medicaid paid by billing NPI, procedure code and month, 2018 to 2024, including managed-care encounters |
| CMS data.cms.gov: Home Health Agency Enrollments and All Owners (PECOS), Provider of Services, Medicare Post-Acute Care Utilization by provider | Medicare certification, owners, and Medicare payments |
| NPPES national provider registry (CMS) | Sixteen billing numbers, their authorized officials and status |
| SBA PPP loan-level FOIA data; SBA COVID EIDL loan and advance data | Pandemic loans and grants |
| HRSA Provider Relief Fund and ARP Rural payments (data.cdc.gov) | Pandemic relief payments |
| IRS Automatic Revocation of Exemption list, 1,247,140 records; IRS EO master file; 990 indexes | Every revoked exemption in this web |
| HHS-OIG List of Excluded Individuals and Entities, 84,001 records; SAM exclusions; MassHealth suspended list; CMS revocations | Checked: **no exclusions** |
| Comptroller's Settlements and Judgments file, 8,297 records | Checked: **no settlement or judgment** |
| 130 CMR 450.212, 450.231, 450.235 and 450.237; 101 CMR 351; MGL c.156D §14.21 and c.156C §70 | What the rules actually require, read rather than assumed |

Two stale mirrors of the spending dataset exist under the same schema (`f7y8-q6ex`, `2bxs-ytms`) and were **not** used.

---

## What the 25 September update adds

1. **Greater Boston Home Health Care is not a new payee. She bought it in 2015.** A state amendment of 30 July 2015 records "the sale of the agency to Aderonke Naomi Osagiede". The Comptroller paid it as `GR. BOSTON HOME HLTH LLC` from 2009, $453,684.67 of it after the sale. Medicare paid it $13,673,342 for 2016 to 2024, and the SBA forgave two PPP loans totalling $2,369,200.
2. **One federal owner ID, four home health agencies, three states.** CMS lists associate 1254592256, NAOMI A EGAH, as 100% owner of Beyond Healthcare Agency and Greater Boston Home Health Care in Massachusetts, Guaranteed Home Health Services in Pennsylvania, and (in its 2023 file) Eden Healthcare in Texas. NPPES names Naomi Osagiede for the same agencies.
3. **The audited company was dissolved twice and paid through both.** A 2019 window adds $730,589.08, for $1,373,977.47 paid while dissolved.
4. **HHS Medicaid data show more than the state ledger.** T-MSIS records $29,101,580.81 under Beyond Independent Living's NPI and $13,234,951.02 under Beyond Healthcare Agency's for 2018 to 2024, against $22,130,538.18 and $12,711,139.06 in the ledger.
5. **COVID money:** two forgiven PPP loans, eleven EIDL loans to cluster entities ($1,328,200), a $74,500 EIDL loan to Naomi Egah personally, $56,000 in EIDL advances and $169,199 in HHS Provider Relief Fund payments.
6. **Correction:** Beyond Adult Day Health Center, dropped in the first version as a stranger's company, was organised and managed by Osagiede from 2014 to February 2017.

---

## Headline numbers

| | |
|---|---|
| Total state payments, six vendor strings | **$105,956,006.17** |
| Payment lines | **7,380** (1,868 distinct payments), 2011-05-25 → 2026-09-21 |
| Entities registered under Naomi Osagiede or Naomi Egah | **45** |
| …carrying at least one involuntary dissolution | **27** |
| Paid to the audited company *while it stood dissolved*, two windows | **$1,373,977.47** ($730,589.08 in 2019, $643,388.39 in 2024) |
| Medicare paid Greater Boston Home Health Care after the sale, CY2016–2024 | **$13,673,342** |
| EINs on the IRS revocation list / still revoked | **10 / 9** |
| Recoupment visible anywhere in the ledger | **$0.00** |

These come from different payers. Do not add them together.

---

## Verdicts

| Claim | Verdict | What the records say |
|---|---|---|
| $103,000,000 **since 2016** | ⚠️ Right size, wrong frame | $102,287,219 all-time at the post date, within 0.7%. Since 2016 is only **$62,897,039**; about 41% predates 2016. |
| BIL received >$29M FY2017–early 2026 | ⚠️ Slightly over then, true now | $28,730,379 at the post date. $32,404,181 now. |
| **$121,728.16 on 16 Jan 2025** | ❌ **Fails** | No payment that day. No row in 49M carries that amount. Nearest: 16 Jan **2026**, $172,708.26. |
| State audit flagged $887,225 | ✅ Exact | Published 21 Sep 2020, period 2016-01-01→2018-12-31. The auditor says *"appear to be unallowable"*, not "fraudulent". |
| 12–15 entities | ✅ Understated | **45**, plus a 46th she organised and managed from 2014 to 2017. |
| Vast majority involuntarily dissolved | ✅ Confirmed | **27 of 45** (60%). |
| Charter revoked Feb 2025 | ⚠️ Date differs | Register says **30 June 2025**. February fits the notice. |
| Registered to 661 Centre St on 22 Jan 2020 | ✅ Exact | Entity `001421873`, organised 22 Jan 2020, 661 Centre St **Brockton**, agent **Naomi Egah**. |
| "The money keeps flowing" | ✅ Confirmed | **$3,608,847** paid since the post. Latest dated lines 21 Sep 2026. |

---

## Six records join the two names

| Entity | Record | Name on it | Second record | Name on it |
|---|---|---|---|---|
| Beyond Faith Consulting, LLC | MA register 463474045 | Naomi Egah | same filing | Aderonke Naomi Osagiede |
| Greater Boston Home Health Care, LLC | MA register 412251357 | Naomi Aderonke Egah, manager | same record | Aderonke Naomi Osagiede, resident agent |
| Beyond Healthcare Agency LLC | CMS owners O20120322000034 | Naomi A Egah, 100% | NPPES 1003116021 | Naomi A Osagiede, CEO |
| Greater Boston Home Health Care | CMS owners O20071114000553 | Naomi A Egah, 100% | NPPES 1063691905 | Naomi Osagiede, Owner |
| Guaranteed Home Health Services (PA) | CMS owners O20191107002080 | Naomi A Egah, 100% | NPPES 1356750228 | Naomi Osagiede, Owner/CEO |
| Beyond Agency Software Systems, LLC | MA register 001127305 | Naomi Egah, manager | NPPES 1639544471 | Naomi Osagiede, Owner |

Searching only `OSAGIEDE` returns 20 entities. Searching `EGAH` returns 26. One overlaps: Beyond Faith Consulting, the bridge filing. Anyone who searched one name and stopped saw less than half the structure.

---

## Where the money went

Six vendor identities in the Comptroller's file, mapping to three real businesses.

| Vendor string, exactly as the state spells it | City | Payment lines | Total | Span |
|---|---|---:|---:|---|
| `ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR` | Woburn | 1,432 | $63,247,375.74 | 2012–2018 |
| `BEYOND INDEPENDENT LIVING LLC` | Woburn → Methuen → West Roxbury | 4,038 | $32,404,181.08 | 2015–2026 |
| `BEYOND HEALTHCARE AGENCY LLC` | Andover | 1,391 | $5,868,134.35 | 2019–2026 |
| `ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE` | Andover | 424 | $4,385,632.99 | 2018–2019 |
| `GREATER BOSTON HOME HEALTH CARE LLC` | Boston → Brockton | 83 | $47,203.01 | 2025–2026 |
| `BEYOND HEATHCARE AGENCY` | Woburn | 12 | $3,479.00 | 2011–2012 |
| **Total** | | **7,380** | **$105,956,006.17** | **2011–2026** |

Rows 1, 3, 4 and 6 are **one company**. The Corporations Division name history for entity `271533104` records that Beyond Healthcare Agency LLC was legally named *Aderonke Naomi Osagiede Beyond Healthcare Agency LLC* until 14 October 2015; the payment system carried the old name for four more years. That single entity accounts for **$73.50 million**. Row 6 ties to it by name, town and program, so treat those $3,479 as probable.

The largest block, $63.2M, is invisible to a plain search: the vendor string is truncated at 40 characters and misspells "Beyond" as **BEYONE**.

**Two more strings, kept outside the headline total:**

- `GR. BOSTON HOME HLTH LLC`: $2,017,617.52 across 1,248 lines, 2009-09-25 to 2025-06-13. It is Greater Boston Home Health Care before June 2025 (probable: name, ZIP history, and a seven-day handover to the new string at the same ZIP). $1,563,932.85 predates the July 2015 sale; **$453,684.67** follows it.
- `BEYOND ADULT DAY HEALTH CENTER, LLC`: $101,510.19 across 23 lines from 2016-09-19 to 2017-02-13, while Osagiede managed it. The $1,946,926.76 paid after 22 February 2017, and the $3,729,881.81 paid to its successor `VILAJ LAJWA ADHC, LLC`, went to a company with other managers.

### By fiscal year, all six vendors

| FY | Payment lines | Total | | FY | Payment lines | Total |
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

## Paid while it had no legal existence, twice

| Window | Register record | Lines | Paid |
|---|---|---:|---:|
| mid-2019 → reinstated 10 Oct 2019 | reinstatement filing `201931597250` | 81 | $730,589.08 |
| 29 Dec 2023 → revived 20 Sep 2024 | summary page dates | 153 | $643,388.39 |
| **Both** | | **234** | **$1,373,977.47** |

The 2019 dissolution date does not appear on the summary page. The 2019 figure covers lines dated 1 July to 30 September 2019 and assumes the 28 June 2019 sweep that dissolved three other LLCs in this web. HHS T-MSIS shows Beyond Healthcare Agency billing $653,850.92 for service months January to August 2024 and $744,126.71 for July to September 2019.

> ⚠️ **Read this before calling it a violation.** A MassHealth provider number and a corporate charter are separate instruments. [130 CMR 450.212](https://www.law.cornell.edu/regulations/massachusetts/130-CMR-450-212) sets out ten provider eligibility criteria, and none of them requires the provider to hold active corporate registration or to tell MassHealth it has been dissolved. [130 CMR 450.231](https://www.law.cornell.edu/regulations/massachusetts/130-CMR-450-231) conditions payment on the provider being *a participating provider on the date of service*, and says nothing about corporate status. On the face of those two sections, paying a dissolved company breaks no rule. **That is the finding.** Two of the Commonwealth's own registers disagree, and nothing in the billing regulation requires them to agree. A legislator can close that gap; an auditor cannot.

Since the Beyond Independent Living nonprofit was dissolved on 30 June 2025, a vendor named "Beyond Independent Living LLC" has taken **778 payment lines worth $5,908,174.45**, through 21 Sep 2026, booked to West Roxbury 02132. Its federal NPI sits at the Brockton LLC's address, so which legal entity receives the money is not settled; every candidate is filed under Osagiede or Egah.

---

## HHS Medicaid billing (T-MSIS)

| Billing NPI | Business | T-MSIS 2018–2024 | CTHRU 2018–2024 | Ratio |
|---|---|---:|---:|---:|
| 1003226630 | Beyond Independent Living (S5140 adult foster care) | $29,101,580.81 | $22,130,538.18 | 1.32× |
| 1003116021 | Beyond Healthcare Agency (home health, GAFC) | $13,234,951.02 | $12,711,139.06 | 1.04× |
| 1063691905 | Greater Boston Home Health Care | $1,143,093.82 | $253,725.31 | 4.51× |

The CTHRU column counts lines dated 2018–2024 plus undated lines whose budget fiscal year falls in FY2019–FY2024 ($59,939.61 for Beyond Healthcare Agency, $52,974.98 for GR. BOSTON). T-MSIS includes claims paid by managed-care plans, which never pass through the Comptroller; that fits the gaps (inference: neither file carries a payer flag). Beyond Independent Living's ratio matches the median of 25 matched Massachusetts adult foster care billers (1.26×). Greater Boston Home Health Care's is far above the median of 30 Massachusetts home health billers (1.15×). Beyond Independent Living's paid per beneficiary-month sat between the 82nd and 95th percentile of Massachusetts S5140 billers every year: high within the peer range, not outside it. HHS suppresses cells under 12 lines or 12 patients, 2024 is preliminary, and the file's whole-dataset total is unusable because of a placeholder stream under code "20"; no cluster row carries it. Per-year figures: [`data/tmsis-by-npi-year.csv`](data/tmsis-by-npi-year.csv).

## Medicare

| Agency | CCN | State | Egah 100% owner since | Medicare paid |
|---|---|---|---|---|
| Beyond Healthcare Agency LLC | 227541 | MA | 2010-05-20 | one published year: CY2015 $82,133 |
| Greater Boston Home Health Care, LLC | 227507 | MA | 2016-09-12 | CY2014–2024 $15,333,781; CY2016–2024 $13,673,342 |
| Guaranteed Home Health Services Inc (dba Always A Step Beyond) | 398334 | PA | 2019-09-09 | no published row |
| Eden Healthcare LLC, later Trinity Home Healthcare LLC | 677975 | TX | 2014-08-22 (2023 file) | CY2015–2018 $622,931 |

CMS suppresses providers with ten or fewer beneficiaries in a year. Beyond Healthcare Agency stayed enrolled in Medicare through its 2023–24 dissolution. Files: [`data/cms-owners.csv`](data/cms-owners.csv), [`data/medicare-home-health.csv`](data/medicare-home-health.csv).

## Greater Boston Home Health Care

2007 organised under other managers → 2008 Medicare certification → 30 Jul 2015 amendment records the sale to Aderonke Naomi Osagiede → 26 Jan 2016 merger certificate names "Naomi Osagiede's corporate designee Beyond Business Management Inc." → 12 Sep 2016 CMS ownership start (Naomi A Egah) → 28 Jun 2019 the surviving LLC dissolved; no active LLC of the name until 11 Nov 2022 → PPP loans 15 Apr 2020 and 31 Mar 2021, $1,184,600 each, forgiven → 20 Jun 2025 new vendor string → 2025 move to 661 Centre St, Brockton. Filing numbers: [`data/gbhhc-and-adhc-filings.csv`](data/gbhhc-and-adhc-filings.csv).

The seller became manager of Beyond Adult Day Health Center, the company Osagiede organised, on 22 February 2017, and sued her in 2018 (*Vinokur v. Osagiede*, D. Mass. 1:18-cv-10335, dismissed after two months; complaint unread).

## COVID money

| Program | Recipients | Amount |
|---|---|---:|
| PPP, Greater Boston Home Health Care LLC, two loans, forgiven | 1 | $2,369,200 |
| PPP, Beyond Business Consulting LLC (former name of 463474045; probable) | 1 | $155,107 |
| COVID EIDL loans to cluster entities | 11 | $1,328,200 |
| COVID EIDL loan to Naomi Egah personally | 1 | $74,500 |
| EIDL advance grants, incl. $10,000 to "Naomi Egah DBA Beyond Faith Clinic" | 7 | $56,000 |
| HHS Provider Relief Fund (name and city match) | 4 | $169,199 |

Four borrowers had no active registration under the borrowing name on the day they borrowed, and three LLCs were revived three weeks before theirs. These are sequences in the records, not findings of wrongdoing. File: [`data/covid-federal.csv`](data/covid-federal.csv).

---

## The federal record

### Every tax-exempt entity in this web lost its exemption

The IRS Automatic Revocation list returns eleven rows for ten EINs in this web. Nine EINs stand revoked.

| EIN | Organisation | Revoked | Posted | Reinstated |
|---|---|---|---|---|
| **462941036** | **BEYOND INDEPENDENT LIVING LLC** | **15 May 2021** | 9 Aug 2021 | no |
| 851507631 | John Egah Ministries | 15 Apr 2023 | 10 Jul 2023 | no |
| 472476331 | Fire of Life Inc | 15 May 2022 | **17 Jan 2026** | no |
| 850730708 | Hope and Power Mega Church | 15 May 2023 | 14 Aug 2023 | no |
| 821341006 | Nkums World Outreach | 15 May 2020 | 11 Aug 2020 | no |
| 822091333 | Nigerian Nurses Association of Massachusetts | 15 May 2020 | 11 Aug 2020 | no |
| 822326336 | Embassy of Grace, A Place of Favor | 15 May 2020 | 11 Aug 2020 | no |
| 814176136 | ZEIIND Family Foundation | 15 May 2019 | 12 Aug 2019 | no |
| 464731086 | Beyond Zoe Ministries International | 15 May 2017 | 16 Aug 2017 | no |
| 465109128 | Beyond Zoe Ministry | 15 May 2017 | 16 Aug 2017 | 15 May 2017 |
| 472476331 | Fire of Life *(first revocation)* | 15 May 2017 | 16 Aug 2017 | 15 May 2017 |

**EIN 462941036 is the same number the Secretary of the Commonwealth uses as the identification number for Beyond Independent Living LLC**, the vendor the Comptroller has paid **$32,404,181**. Its exemption was revoked on 15 May 2021 for three consecutive years of not filing. The Commonwealth has paid it every year since: $3.48M in FY2021, climbing to $4.78M in FY2026. Only Fire of Life ever filed a return (five paper 990-EZs, 2014–2018).

### Sixteen federal billing numbers, all active

[`data/npi-registry.csv`](data/npi-registry.csv) lists sixteen NPIs from a sweep by name, official, address and phone: 11 confirmed (the registry names Naomi Osagiede, Aderonke Osagiede or Naomi Egah as authorized official), 2 probable, 3 adjacent. Every one is status A with no deactivation date. Two are in Pennsylvania. The phone 978-930-9410 also appears on three NPIs whose officials are other people, so it does not identify the cluster on its own.

### What the federal record does *not* show

- **No exclusions.** HHS-OIG LEIE (84,001 records), SAM exclusions (168,671 active), CMS revocations and eight editions of MassHealth's suspended list return nothing for any person, entity or NPI here.
- **No settlement, no judgment.** The Comptroller's Settlements and Judgments file, 8,297 records, returns nothing.
- **No press release.** DOJ, HHS-OIG and the Massachusetts AG name no one here. The State Auditor's 2021 annual report marks the Beyond audit "MassHealth Recouping Payments: Yes" with no amount and nothing since.

**There is no enforcement action against anyone in this web anywhere on the public record.** That is a fact about the file, and it belongs in any honest write-up of it.

---

## What is actually provable

**Provable from documents today, no inference:**

1. One person operates 45 Massachusetts entities under two filing names. Six records tie the names together, three of them inside CMS's own systems.
2. Twenty-seven of those entities carry an involuntary dissolution. The audited company was dissolved twice and paid $1,373,977.47 while dissolved.
3. Nine of ten cluster EINs on the IRS revocation list stand revoked, including the EIN of the $32.4M payee.
4. One CMS owner ID holds or held four Medicare home health agencies in three states.
5. She bought Greater Boston Home Health Care in 2015; Medicare has paid it $13,673,342 since 2016.
6. A 2020 state audit found up to $887,225 in apparently unallowable billing; MassHealth was marked "recouping" in 2021 and no amount is public.
7. Every NPI checked still holds active status.

**Answerable with a records request, which nobody has yet:** the recoupment amount, provider enrolment during the dissolutions, which managed-care plans paid these providers, and what the SBA applications certified. The memo's Follow-ups tab lists each request by holder.

**Not provable by anyone outside government:** whether services were delivered, whether any billing was knowingly false, and intent. Those need claims-level data and a subpoena.

The defensible claim is not that someone stole $103 million. It is that a single operator with 45 companies, 27 administrative dissolutions, nine revoked exemptions, agencies in three states and an unresolved audit finding has drawn more than $105.9 million from the Commonwealth alone, is still being paid, and that no public body appears to have looked. That is a demand for an audit, and the records carry it.

---

## Corrections to the 20 September version

1. Greater Boston Home Health Care was not a new payee in June 2025; only the vendor string changed.
2. Beyond Adult Day Health Center was hers from 2014 to February 2017. Its current managers are Victoria Vinokur and Paul Rayev; Gennady Vinokur is a real-property signatory, not a manager.
3. Beyond Healthcare Agency was dissolved twice, not once.
4. The IRS list holds 11 rows for 10 EINs, not 8 for 7.
5. "7,380 payments" are 7,380 payment lines (1,868 payments).
6. The latest date moved from 17 to 21 September 2026 after a Comptroller reload, with no new money; nine undated lines ($59,939.61) sit outside every date-bounded figure.
7. The NPI table grew from seven to sixteen; Beyond Healthcare Agency's record changed on 24 September 2026.
8. Healing Pathways: Naomi Aderonke Egah is the SOC signatory, not a manager.
9. Entity 412251357 merged away in 2016, and Medicoach Transportation dissolved voluntarily in 2015; both were shown as active.
10. The phone link is weaker than first presented.
11. A chart caption asserted "scheduled sweeps"; no schedule is published.
12. The audit's settlements-and-judgments check was malformed; the corrected search still finds nothing.
13. `data/findings.json` carried five-vendor totals and retracted claims; it has been replaced.

---

## Read this before publishing anything

- **None of this establishes fraud.** An involuntary dissolution is a failure to file an annual report. The auditor's phrase is *"appear to be unallowable"*, an upper-bound estimate, not an adjudicated finding. Every sentence should survive being read by a lawyer for the other side.
- **Do not add figures across sources.** CTHRU and T-MSIS overlap; Medicare, the SBA and the Provider Relief Fund are separate programs.
- **Do not read the clustered dissolution dates as a single event.** Five entities share 28 Jun 2019 and five share 30 Jun 2025, and the LLC dissolutions fall on 29–31 December. Neither statute prescribes a date: [MGL c.156D §14.21](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter156D/Section14.21) (corporations) and [MGL c.156C §70](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter156C/Section70) (LLCs) each require written notice and a **90-day cure period**, after which the Secretary *shall* dissolve. The clustering is an observed pattern in the filing data, consistent with batch processing, and I have not found a published schedule. Report the **count**, not the coincidence of dates.
- **$105.9M is a floor, not a ceiling.** HHS data show Medicaid money reaching these providers through managed-care plans, which never passes through the Comptroller, and Medicare pays through CMS.
- **Appropriation labels are accounting buckets.** "Managed Care Plan", "MassHealth Senior Care", "Indemnity / Third Party Liability Plan" describe which account the money left, not which service was billed.
- **Attribution between same-named LLCs is open** for Greater Boston Home Health Care and Beyond Independent Living. CTHRU carries no entity ID. Every candidate is filed under Osagiede or Egah.
- **Other people share these surnames.** The Osagiede search returns filings by at least a dozen other individuals: an attorney, a shipping company, several churches. Only the 45 entities in [`data/entities.csv`](data/entities.csv) carry Naomi Osagiede or Naomi Egah as an officer, manager, agent or signatory.

### Recoupment

Across all 7,380 lines there is not one negative amount; the smallest line is $0.21. Absence is not proof that nothing was repaid: CTHRU records money paid *out*, and the Comptroller's only public revenue dataset (`kcy7-ivxi`) has no payer column. [130 CMR 450.235](https://www.law.cornell.edu/regulations/massachusetts/130-CMR-450-235) requires a provider to report and return an identified overpayment within 60 days. [130 CMR 450.237](https://www.law.cornell.edu/regulations/massachusetts/130-CMR-450-237) gives MassHealth a notice-and-determination process and says the agency "will take appropriate action to recover the overpayment". Neither section, as written, describes netting an overpayment against future claims. Ask for the overpayment determination by name.

### Kept out of every total

| Entity | CTHRU total | Why |
|---|---:|---|
| `BEYOND ADULT DAY HEALTH CENTER, LLC` after 2017-02-22, and `VILAJ LAJWA ADHC, LLC` | $1,946,926.76 + $3,729,881.81 | Other managers from 22 Feb 2017 (Victoria Vinokur, Paul Rayev) |
| `BEYOND TRANSPORTATION LLC` | $124,799.78 | Methuen/Tewksbury. No officer link in the register. |
| `MEDICAL COMMUNITY PSYCHOTHERAPY LLC` | $10,851.69 | Natick. Substring collision with "Community Psych". |

---

## Scope of this check

Stated plainly so a reader can see where the work stops.

**Retrieved.** First pull 20 September 2026; every figure re-derived on 24 and 25 September 2026. Payment data from the Comptroller's load of 25 September 2026. Re-running [`scripts/audit.py`](scripts/audit.py) re-derives the published figures from the live sources and fails on any disagreement.

**Read in full.** All 45 entity summaries at the Corporations Division, and the filing histories of the Greater Boston Home Health Care, Greater Healthcare Solutions, Beyond Business Management and Beyond Adult Day Health Center entities. The Office of the State Auditor report of 21 September 2020 and its 2021 annual report. Every row these EINs return from the IRS Automatic Revocation list. Every NPPES record in the NPI file. CMS owner and enrolment files for the four agencies.

**Searched completely, returning the counts stated.** CTHRU `pegc-naaa` (49,022,699 rows) and every other CTHRU table with a name column, HHS T-MSIS provider spending (238,015,729 rows), CMS Medicare post-acute utilisation files 2014–2024, SBA PPP and EIDL files, HRSA Provider Relief Fund, the IRS revocation list (1,247,140), the IRS Massachusetts exempt-organization master file, the HHS-OIG exclusion list (84,001), SAM exclusions, the Comptroller's Settlements and Judgments file (8,297).

**Read in part, and this is the limit that matters.** Of 130 CMR 450, I read only **450.212, 450.231, 450.235 and 450.237**. Statements on this page about what MassHealth's rules do and do not require are bounded to those four sections and should not be read as a survey of the regulation. Of the dissolution statutes I read MGL c.156D §14.21 and c.156C §70. Of the rate rules, 101 CMR 351 for the group adult foster care code.

**Not done.** No one named here was contacted. No interviews. No review of MassHealth's provider enrolment file, no claims-level data, no court filings beyond the docket entry, no property records, no Pennsylvania or Texas state records. Whether services were delivered has not been examined and could not be from these sources.

**Not alleged.** No conclusion of wrongdoing by any named person or entity is drawn or intended. Every record cited is a public filing or a public disclosure by the Commonwealth or the federal government. Nothing here is legal advice.

---

## Files

| Path | Contents |
|---|---|
| [`index.html`](index.html) | The full memo, in tabs |
| [`data/entities.csv`](data/entities.csv) | All 45 entities: SoC ID, type, organised, dissolved, revived, city, filing name, notes |
| [`data/payments-by-fiscal-year.csv`](data/payments-by-fiscal-year.csv) | Every vendor × fiscal year × city, with line counts and totals |
| [`data/payments-by-appropriation.csv`](data/payments-by-appropriation.csv) | Every vendor × appropriation × department |
| [`data/tmsis-by-npi-year.csv`](data/tmsis-by-npi-year.csv) | HHS T-MSIS paid by billing NPI and service year |
| [`data/medicare-home-health.csv`](data/medicare-home-health.csv) | CMS Medicare home health payments by CCN and year |
| [`data/cms-owners.csv`](data/cms-owners.csv) | CMS PECOS owner rows for associate 1254592256 |
| [`data/covid-federal.csv`](data/covid-federal.csv) | PPP, EIDL, EIDL advance, Provider Relief Fund and ARP rows |
| [`data/gbhhc-and-adhc-filings.csv`](data/gbhhc-and-adhc-filings.csv) | Corporations Division filings behind the two timelines |
| [`data/irs-revocations.csv`](data/irs-revocations.csv) | The eleven rows these EINs return from the IRS revocation list |
| [`data/npi-registry.csv`](data/npi-registry.csv) | Sixteen federal billing numbers, officials, addresses, status and tie |
| [`data/findings.json`](data/findings.json) | Machine-readable verdicts and findings with sources |
| [`scripts/soda.py`](scripts/soda.py) | The Socrata query helper |
| [`scripts/audit.py`](scripts/audit.py) | **The accuracy audit.** Re-derives the published figures from the live sources and the local data files, and fails if any disagree |

### Checking this page

`scripts/audit.py` re-queries the live Comptroller dataset, the NPI registry, CMS and HHS relief datasets, re-downloads the IRS revocation list and the HHS-OIG exclusion list, and compares each result against the number as published in this README and in `index.html`. It exits non-zero if anything disagrees. The SBA and T-MSIS checks run when the source files are present locally and are skipped, with a notice, when they are not.

```bash
cd scripts && python audit.py
```

Figures move as the Commonwealth pays more money, so a re-run will legitimately diverge on running totals. What it must never show is an internal disagreement: a number in the prose that the data does not support.

### Reproducing a figure

```python
from soda import q, f
SIX = ["ADERONKE NAOMI OSAGIEDE BEYONE HEALTHCAR","ADERONKE NAOMI OSAGIEDE BEYOND HLTH CARE",
       "BEYOND HEALTHCARE AGENCY LLC","BEYOND INDEPENDENT LIVING LLC","BEYOND HEATHCARE AGENCY",
       "GREATER BOSTON HOME HEALTH CARE LLC"]
IN = "vendor in(%s)" % ",".join("'%s'" % v for v in SIX)
print(q(select="count(1) as n,sum(amount) as total", where=IN))
```

Entity records are at `corp.sec.state.ma.us`: search by ID number using the values in `data/entities.csv`.

---

*No wrongdoing by any named individual is alleged. Every record cited is a public filing or a public payment disclosure made by the Commonwealth of Massachusetts or the federal government.*
