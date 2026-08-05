# Beyond the Law
### Testing the Limits of Legal Reform for Women's Economic Inclusion in East Africa

Does legal reform on women's entrepreneurship and property rights actually translate into real business ownership gains? This project builds a four-stage pipeline — Legal Rights → Enforcement → Credit Access → Education — across five East African economies (Kenya, Rwanda, Tanzania, Uganda, Ethiopia) using entirely real, publicly cited data, and finds that at every stage, for every country, it breaks down.

**[Live interactive dashboard →](#)** (Streamlit Cloud link)
**[Tableau workbook →](#)** (Tableau Public link)
**[Read the full brief →](brief.md)**

---

## Key Findings

1. **Governance quality does not predict labor-market inclusion.**
2. **Female business ownership declined over the past decade in Kenya (49.2%→36.5%) and Tanzania (24.7%→13.2%)** — triangulated four independent ways.
3. **Rwanda's ownership surge does not generalize** — a leave-one-out check reverses the apparent governance-ownership correlation from +0.66 to -0.98.
4. **Legal reform does not predict ownership outcomes.** Kenya's legal scores rose more than any country in the sample while its ownership fell the most.
5. **Neither does enforcement, credit access, or education.** Four independent mechanisms tested, none explain the pattern — consistent with Duflo (2012) and Jayachandran's research on social norms as the binding constraint formal reform doesn't reach.

Full methodology, the four-stage pipeline breakdown, and a formal triangulation matrix are in [`brief.md`](brief.md).

---

## Repository Structure

```
├── app/                          Streamlit dashboard
│   ├── app.py
│   ├── requirements.txt
│   └── data/
├── data/                         Full analysis outputs
│   ├── country_year_panel.csv
│   ├── full_country_comparison.csv
│   ├── historical_ownership_trend.csv
│   ├── governance_change_vs_ownership_change.csv
│   ├── wbl2026_full_pillars.csv          Legal/Enforcement scores
│   ├── enforcement_gap_2026.csv
│   ├── female_business_borrowing.csv     Credit access (Findex)
│   ├── education_vs_ownership.csv        Education stage
│   ├── pipeline_data.csv                 All four stages, consolidated
│   ├── esg_sourcing_score_final.csv
│   └── tableau_extract.csv
├── brief.md
└── README.md
```

## Data Sources

| Source | What it provides |
|---|---|
| World Bank Worldwide Governance Indicators | 6 governance dimensions, 2010-2024 |
| World Bank World Development Indicators | Labor force, unemployment, literacy, education completion |
| World Bank Enterprise Surveys | Firm-level gender/ownership data, multiple vintages (2011-2025) |
| World Bank Women, Business and the Law | Legal Frameworks (1971-2024) and Enforcement Perceptions (2026) |
| World Bank Global Findex 2025 | Gender-disaggregated business-borrowing rate |
| UNHCR Refugee Data Finder | Refugee/IDP/host-community populations, 2010-2025 |

## Methodology Notes

With 4-5 countries, this project makes no claim of statistical significance. Every finding is triangulated across independent data cuts, stress-tested with leave-one-out checks, and reported with rates annualized for fair cross-country comparison. A data-integrity correction (an early AI-tool summary of WBL figures was discarded after an internal contradiction was found) is disclosed directly in the brief rather than silently fixed.

## Running the Dashboard Locally

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

## Author

Lisa Uwonkunda — [GitHub](#) · [LinkedIn](#)
