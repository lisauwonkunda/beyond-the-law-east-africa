# Beyond the Law
### Testing the Limits of Legal Reform for Women's Economic Inclusion in East Africa

*Prepared by Lisa Uwonkunda*

---

## Executive Summary

Economist Esther Duflo's influential 2012 review in the *Journal of Economic Literature* argues that legal and economic reform levers alone are **"too weak to be self-sustaining"** for closing gender gaps — sustained, deliberate commitment is required precisely because reform on paper does not automatically produce real outcomes. Separately, economist Seema Jayachandran's research on social norms as a barrier to women's economic participation asks a related question: does the law being enforced, in practice, actually matter as much as the law existing at all?

This project tests both claims directly, using entirely real, publicly cited data across five East African economies — Kenya, Rwanda, Tanzania, Uganda, and Ethiopia — by building a four-stage pipeline: **Legal Rights → Real-World Enforcement → Credit Access → Education**, and checking whether movement at any stage predicts actual change in women's business ownership.

**Across every country tested, and at every stage of the pipeline, it breaks down.** This is not a data gap or an unresolved mystery — it is a specific, quantified confirmation of a recognized empirical debate in development economics, using a novel five-country panel that did not exist compiled this way before.

---

## Key Findings

1. **Governance quality does not predict labor-market inclusion.** A panel regression across 5 countries and ~15 years finds no significant relationship between governance level and inclusion outcomes.
2. **Female business ownership has declined over the past decade in Kenya (49.2%→36.5%) and Tanzania (24.7%→13.2%)** — the most rigorously triangulated finding here, verified across four independent data cuts.
3. **Rwanda's ownership surge (+13.2 points in 4 years) does not generalize.** A leave-one-out robustness check shows Rwanda alone carries the entire apparent link between governance change and ownership change; removing it reverses the relationship from +0.66 to -0.98.
4. **Legal reform does not predict ownership outcomes.** Kenya's legal Entrepreneurship and Assets scores rose more than any other country in this sample (+25, +20) over the same window its actual ownership fell the most (-12.7 points).
5. **Real-world enforcement of the law lags the law itself, unevenly.** Uganda shows the largest law-versus-enforcement gap (18.75 points on Assets); Rwanda shows none (0 points) — yet this gap does not correspond to ownership outcomes either.
6. **Access to business credit does not explain the pattern.** Kenya's female business-borrowing rate barely moved (-2 points) while ownership collapsed (-12.7 points); Uganda's borrowing rate rose 6 points while ownership stayed flat.
7. **Rising education does not explain the pattern — and Rwanda's case inverts the expected direction entirely.** Girls' secondary completion in Rwanda *declined* 9.1 points during the exact 2019-2023 window its ownership surged. In every other country, education rose while ownership fell or stagnated.

---

## Data & Methodology

**Sources, all real, publicly cited:**
- World Bank Worldwide Governance Indicators (6 dimensions, 2010-2024)
- World Bank World Development Indicators (labor force participation, unemployment, vulnerable employment, female literacy, female lower-secondary completion)
- World Bank Enterprise Surveys — multiple vintages per country: Kenya (2013, 2025), Rwanda (2019, 2023), Tanzania (2013, 2023), Uganda (2013, 2025), Ethiopia (2011, 2025)
- World Bank Women, Business and the Law — historical panel (1971-2024, Legal Frameworks) and the 2026 report (Legal Frameworks, Supportive Frameworks, and Enforcement Perceptions pillars)
- World Bank Global Findex 2025 — female business-borrowing rate, gender-disaggregated
- UNHCR Refugee Data Finder (2010-2025)

**Methodological approach:** with 4-5 countries, statistical significance is not achievable and is not claimed. Every finding is triangulated across independent data cuts, and the strongest apparent pattern is stress-tested with a leave-one-out check. Rates are annualized throughout since comparison windows differ by country.

**A data-integrity note, disclosed deliberately:** an earlier version of this analysis used an AI-tool summary of Women, Business and the Law figures, which contained an internal contradiction traced to conflated pre- and post-2024 methodology versions. That version was discarded once the primary-source historical panel was obtained directly from the World Bank, and a resulting speculative causal claim about Rwanda was withdrawn. Noted here rather than silently corrected.

**Known limitations:**
- Youth NEET, Global Findex account ownership, and the education indicators have sparse year coverage per country (survey-based, not administrative); several country/window pairs use the nearest available year rather than an exact match, disclosed in the underlying data.
- Rwanda has no Global Findex business-borrowing data covering its actual 2019-2023 surge window — the survey was not fielded there in those years, so credit access specifically cannot be tested for Rwanda's case.
- The WBL Enforcement Perceptions pillar is only measured for 2026 — a single year, not yet a time series, so it is a cross-sectional complement rather than a window-matched test.
- Composite ESG rankings are sample-relative; adding or removing a country shifts every other country's relative position.

---

## Finding 1: The Governance-Inclusion Disconnect

| Country | Governance State Capacity (avg. 2010-24) | Female Labor Force Participation | Youth Unemployment |
|---|---|---|---|
| Rwanda | **+0.10** (highest) | 54.7% (lowest) | 17.3% (highest) |
| Tanzania | -0.47 | **80.8%** (highest) | **3.7%** (lowest) |
| Uganda | -0.67 | 73.8% | 4.5% |
| Kenya | -0.68 | 67.3% | 10.3% |
| Ethiopia | -0.86 (lowest) | 66.1% | 4.5% |

---

## Finding 2: A Decade of Declining Female Business Ownership

| Country | Window | Ownership: then → now | Annualized change |
|---|---|---|---|
| Tanzania | 2013→2023 | 24.7% → 13.2% | -1.15 pts/yr |
| Kenya | 2013→2025 | 49.2% → 36.5% | -1.06 pts/yr |
| Ethiopia | 2011→2025 | 35.3% → 32.3% | -0.21 pts/yr |
| Uganda | 2013→2025 | 26.4% → 27.9% | +0.12 pts/yr |
| Rwanda | 2019→2023 | 24.6% → 37.8% | +3.30 pts/yr |

Triangulated four independent ways: cross-sectional snapshot, regional Sub-Saharan Africa benchmark, within-country firm-size trend, and this historical trend.

---

## Finding 3: Robustness Check — A Cautionary Result

| Country | Governance change/year | Ownership change/year |
|---|---|---|
| Rwanda | +0.033 | +3.30 |
| Tanzania | +0.010 | -1.15 |
| Kenya | +0.009 | -1.06 |
| Ethiopia | -0.008 | -0.21 |
| Uganda | -0.008 | +0.12 |

With all five countries, r = +0.66. **Removing Rwanda produces r = -0.98** among the remaining four — a near-perfect reversal. The entire positive result was carried by one country.

---

## Finding 4: The Full Pipeline — Legal Rights, Enforcement, Credit, and Education

### Stage 1 — Legal Reform vs. Actual Outcomes

| Country | Window | Legal Entrepreneurship change | Legal Assets change | Actual ownership change |
|---|---|---|---|---|
| Kenya | 2013-2024 | **+25** | **+20** | **-12.7 pts** |
| Rwanda | 2019-2023 | 0 | 0 | +13.2 pts |
| Tanzania | 2013-2023 | 0 | 0 | -11.5 pts |
| Uganda | 2013-2024 | 0 | **+40** | +1.5 pts |
| Ethiopia | 2011-2024 | **+25** | 0 | -3.0 pts |

Kenya's legal Entrepreneurship and Assets scores rose more than any other country in this sample over the exact window its actual ownership fell the most. An earlier version of this analysis speculated that Rwanda's surge was driven by legal reform in this window; the primary-source data shows Rwanda's Assets score was already at a ceiling of 100 throughout, unchanged, and its Entrepreneurship score only rose in 2024, after the surge occurred. That claim has been withdrawn.

### Stage 2 — Enforcement Perceptions (2026, cross-sectional)

| Country | Entrepreneurship enforcement gap | Assets enforcement gap |
|---|---|---|
| Uganda | 12.50 | **18.75** (largest) |
| Kenya | 12.50 | 6.25 |
| Ethiopia | 6.25 | 6.25 |
| Rwanda | 6.25 | **0.00** (full enforcement) |
| Tanzania | 6.25 | **-12.50** (perceived enforcement exceeds the codified law) |

Uganda shows the largest enforcement gaps in the sample, yet its ownership trend was roughly flat — not the largest decline. Tanzania's negative Assets gap is a genuine anomaly, not explained away here: perceived enforcement exceeding the legal score likely reflects customary practice operating somewhat independently of statutory law.

### Stage 3 — Credit Access

| Country | Female business-borrowing rate | Direction | Actual ownership change |
|---|---|---|---|
| Kenya | 21.1% (2014) → 19.0% (2024) | Roughly flat | -12.7 pts |
| Tanzania | 18.1% → 13.7% | Declined | -11.5 pts |
| Uganda | 21.2% → 27.2% | Rose | +1.5 pts |
| Ethiopia | 12.1% (2014) → 11.3% (2017) | Roughly flat | -3.0 pts |
| Rwanda | 12.0% (2014) → 10.6% (2017) | **No data 2019-2023** | +13.2 pts |

Rwanda's actual surge window has no Findex coverage — the credit-access channel cannot be tested for the country where it would matter most. For the four countries that can be tested, magnitude and direction do not correspond to ownership change.

### Stage 4 — Education

| Country | Window used | Female secondary completion change | Actual ownership change |
|---|---|---|---|
| Kenya | 2016-2023 | +23.6 pts | -12.7 pts |
| Rwanda | 2019-2023 | **-9.1 pts** | **+13.2 pts** |
| Tanzania | 2016-2023 | +7.8 pts | -11.5 pts |
| Uganda | 2016-2017 (data ends 2017) | -2.1 pts | +1.5 pts |
| Ethiopia | 2022-2023 | -0.3 pts | -3.0 pts |

The sharpest result in the entire pipeline: **Rwanda's ownership surge coincided with a decline in girls' secondary completion**, moving in the opposite direction. Kenya's education rose 23.6 points — the largest gain in the sample — over the same window its ownership fell the most.

---

## Triangulation Matrix

| Finding | Cross-sectional | Regional benchmark | Firm-size trend | Historical trend | Leave-one-out |
|---|---|---|---|---|---|
| Kenya/Tanzania ownership decline | ✅ | ✅ | ✅ (Tanzania) | ✅ | — |
| Rwanda's ownership surge is real | ✅ | — | ✅ | ✅ | ⚠️ drives the governance-change correlation alone |
| "Governance change → ownership change" | — | — | — | ✅ (n=5 only) | ❌ reverses without Rwanda |
| Legal reform ≠ ownership outcomes | ✅ (Kenya) | — | — | ✅ | — |
| Enforcement gap ≠ ownership outcomes | ✅ (Uganda largest gap, flat outcome) | — | — | ⚠️ single year only | — |
| Credit access ≠ ownership outcomes | ✅ | — | — | ✅ (where data exists) | — |
| Education ≠ ownership outcomes | ✅ | — | — | ✅ (Rwanda inverts direction) | — |

Four independent mechanisms tested — legal reform, enforcement, credit access, and education — and none explain the direction or magnitude of ownership change in any country. This consistency across four entirely different data sources is itself the finding: it is strong, converging evidence for the Duflo/Jayachandran thesis that formal levers alone do not move real outcomes, applied here to a specific, real, five-country East African panel.

---

## Limitations

- Four to five countries cannot support statistical inference; findings are patterns and associations, robustness-tested where possible, never causal claims.
- Several country/indicator pairs rely on nearest-available-year matching due to real survey-coverage gaps, disclosed throughout rather than smoothed into false precision.
- Rwanda's actual surge window (2019-2023) lacks Findex coverage entirely; the credit-access stage cannot be tested for the one country most relevant to it.
- The WBL Enforcement Perceptions pillar is single-year (2026) and cannot yet be matched to the specific historical windows used elsewhere.
- Composite ESG rankings are sample-relative.

---

## Data & Code

Full pipeline, interactive dashboard, and analysis code at [GitHub link]. Live dashboard at [Streamlit Cloud link]. Tableau workbook at [Tableau Public link].
