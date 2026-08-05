"""
Private-Sector Access & Economic Mobility — Interactive Explorer
Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="ESG & Economic Mobility — East Africa", layout="wide")

# ---------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------
@st.cache_data
def load_data():
    panel = pd.read_csv("data/country_year_panel.csv")
    full = pd.read_csv("data/full_country_comparison.csv")
    barrier = pd.read_csv("data/structural_ownership_barrier.csv")
    return panel, full, barrier

panel, full, barrier = load_data()
df = full.merge(barrier[["country", "structural_ownership_barrier_score"]], on="country")

st.title("Beyond the Law")
st.caption("Testing the Limits of Legal Reform for Women's Economic Inclusion in East Africa. "
           "Kenya · Rwanda · Tanzania · Uganda · Ethiopia — built on World Bank WGI/WDI/Enterprise "
           "Surveys/Women, Business and the Law, and UNHCR Refugee Data Finder. All figures are real, "
           "cited, publicly sourced data.")

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "The Pipeline", "ESG Score Explorer", "Governance vs. Outcomes", "Ownership Trends",
    "Country-Year Trends", "Robustness Checks"
])

with tab0:
    st.subheader("Where Does Legal Reform Break Down?")
    st.markdown(
        "Esther Duflo's influential 2012 review (*Journal of Economic Literature*) argues legal and "
        "economic reform levers alone are **\"too weak to be self-sustaining\"** for closing gender gaps. "
        "This tab tests that claim directly: does a country's legal standing on women's entrepreneurship "
        "and property rights, its real-world enforcement, and women's access to business credit predict "
        "actual business ownership outcomes? **Across every country tested, the pipeline breaks down.**"
    )
    pipeline = pd.read_csv("data/pipeline_data.csv")
    stage_cols = ["legal_score", "enforcement_score", "credit_access_score"]
    if pipeline["education_score"].notna().any():
        stage_cols.append("education_score")
    else:
        st.info("Education data (the fourth pipeline stage) is pending upload — shown here with three stages.")

    country_pick_pipe = st.selectbox("Select a country", pipeline["country"].tolist())
    row = pipeline[pipeline.country == country_pick_pipe].iloc[0]

    fig0 = go.Figure()
    labels = {"legal_score": "Legal Rights\n(WBL Legal Frameworks)", "enforcement_score": "Enforcement\n(WBL Enforcement Perceptions)",
              "credit_access_score": "Credit Access\n(Findex, % women)", "education_score": "Education\n(pending)"}
    fig0.add_trace(go.Bar(x=[labels[c] for c in stage_cols], y=[row[c] for c in stage_cols],
                          marker_color=["#2c5aa0", "#5b8ac6", "#e07b39", "#999999"][:len(stage_cols)]))
    fig0.update_layout(title=f"{country_pick_pipe}: The Pipeline (each stage, 0-100 scale except credit access, %)",
                       yaxis_title="Score", height=400)
    st.plotly_chart(fig0, use_container_width=True)
    st.metric("Actual annualized ownership change", f"{row['ownership_change_per_year']:+.2f} pts/year")
    st.caption(
        "Compare the pipeline bars above to this outcome metric: strong scores across all stages do not "
        "reliably predict a positive outcome (see Kenya), and a genuine outcome surge (Rwanda) is not "
        "preceded by movement in these specific legal/enforcement stages during the relevant window."
    )

    st.markdown("### All five countries, side by side")
    fig0b = px.bar(pipeline, x="country", y=stage_cols, barmode="group",
                   title="Pipeline Stages by Country", labels={"value": "Score", "variable": "Stage"})
    st.plotly_chart(fig0b, use_container_width=True)

# ---------------------------------------------------------------------
# TAB 1: Interactive ESG scoring
# ---------------------------------------------------------------------
with tab1:
    st.subheader("Build your own ESG Sourcing Score")
    st.markdown(
        "Adjust the pillar and sub-indicator weights below and watch the country ranking change live. "
        "**This is the point** — the ranking in the previous analysis was one defensible weighting choice, "
        "not the only one. Environmental is intentionally absent: no real environmental indicators were "
        "collected for this project, so it isn't scored rather than faked."
    )

    col1, col2 = st.columns(2)
    with col1:
        gov_weight = st.slider("Governance pillar weight", 0.0, 1.0, 0.5, 0.05)
    with col2:
        st.metric("Social pillar weight", f"{1-gov_weight:.2f}", help="Automatically balances with Governance")
    social_weight = 1 - gov_weight

    st.markdown("**Governance sub-weights** (must relate proportionally — normalized automatically)")
    g1, g2, g3 = st.columns(3)
    w_state_capacity = g1.slider("State capacity index", 0.0, 1.0, 0.6, 0.05, key="g1")
    w_voice = g2.slider("Voice & accountability", 0.0, 1.0, 0.2, 0.05, key="g2")
    w_bribery = g3.slider("Firm-level bribery (inverted)", 0.0, 1.0, 0.2, 0.05, key="g3")
    g_total = w_state_capacity + w_voice + w_bribery
    if g_total == 0:
        g_total = 1

    st.markdown("**Social sub-weights**")
    s1, s2, s3, s4 = st.columns(4)
    w_flfp = s1.slider("Female labor force participation", 0.0, 1.0, 0.25, 0.05, key="s1")
    w_ownership = s2.slider("Ownership access (inverted barrier)", 0.0, 1.0, 0.35, 0.05, key="s2")
    w_youth = s3.slider("Youth unemployment (inverted)", 0.0, 1.0, 0.20, 0.05, key="s3")
    w_vulnerable = s4.slider("Vulnerable employment (inverted)", 0.0, 1.0, 0.20, 0.05, key="s4")
    s_total = w_flfp + w_ownership + w_youth + w_vulnerable
    if s_total == 0:
        s_total = 1

    def z(series, flip=1):
        return flip * (series - series.mean()) / series.std()

    calc = df.copy()
    calc["g_score"] = (w_state_capacity * z(calc["governance_state_capacity_index"]) +
                        w_voice * z(calc["gov_voice_accountability"]) +
                        w_bribery * z(calc["bribery_incidence_pct"], -1)) / g_total
    calc["s_score"] = (w_flfp * z(calc["female_labor_force_participation"]) +
                        w_ownership * z(calc["structural_ownership_barrier_score"], -1) +
                        w_youth * z(calc["youth_unemployment_rate"], -1) +
                        w_vulnerable * z(calc["vulnerable_employment_rate"], -1)) / s_total
    calc["esg_score"] = gov_weight * calc["g_score"] + social_weight * calc["s_score"]
    calc = calc.sort_values("esg_score", ascending=False)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=calc["country"], y=calc["g_score"],
                          name="Governance pillar", marker_color="#2c5aa0"))
    fig.add_trace(go.Bar(x=calc["country"], y=calc["s_score"], name="Social pillar", marker_color="#e07b39"))
    fig.add_trace(go.Scatter(x=calc["country"], y=calc["esg_score"], mode="markers+lines",
                              name="Composite ESG Score", marker=dict(size=14, color="black"), line=dict(color="black", dash="dot")))
    fig.update_layout(barmode="group", title="ESG Sourcing Score by Country (live-updating)",
                       yaxis_title="Z-score (relative to the 5-country sample)", height=450)
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(calc[["country", "g_score", "s_score", "esg_score"]].round(3).rename(
        columns={"g_score": "Governance", "s_score": "Social", "esg_score": "Composite ESG"}
    ), use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------
# TAB 2: Governance vs outcomes scatter (descriptive, n=5, honestly labeled)
# ---------------------------------------------------------------------
with tab2:
    st.subheader("Governance vs. Labor-Market Outcomes")
    st.warning(
        "**Descriptive only — not a statistical test.** With 5 countries there are not enough independent "
        "data points for inference. The panel regression (5 countries × ~15 years, country fixed effects) "
        "found no statistically significant relationship between the governance index and these outcomes. "
        "This view shows the raw cross-country pattern for context, not a tested effect."
    )
    outcome_choice = st.selectbox("Outcome variable", [
        "female_labor_force_participation", "youth_unemployment_rate", "vulnerable_employment_rate"
    ])
    fig2 = px.scatter(df, x="governance_state_capacity_index", y=outcome_choice, text="country",
                       size=[14]*len(df), color="country", height=500)
    fig2.update_traces(textposition="top center", marker=dict(size=16))
    fig2.update_layout(showlegend=False, xaxis_title="Governance State Capacity Index (avg. 2010-2024)")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Note the Rwanda/Tanzania contrast: Rwanda has the highest governance score but the lowest "
               "female labor force participation and highest youth unemployment of the five countries.")

# ---------------------------------------------------------------------
# TAB 3: Tanzania ownership gap deep-dive
# ---------------------------------------------------------------------
with tab3:
    st.subheader("Female Business Ownership: 10-14 Year Trends")
    st.markdown(
        "Comparing each country's earliest available Enterprise Survey round to its most recent one. "
        "Time spans differ by country (Rwanda: 4 years; others: 10-14 years), so **rates are annualized** "
        "for fair comparison."
    )
    hist = pd.read_csv("data/historical_ownership_trend.csv")
    fig3 = px.bar(hist.sort_values("ownership_change_per_year"), x="country", y="ownership_change_per_year",
                  color="ownership_change_per_year", color_continuous_scale="RdYlGn",
                  title="Annualized Change in Female Business Ownership (points/year)")
    fig3.update_layout(coloraxis_showscale=False, yaxis_title="Percentage points per year")
    st.plotly_chart(fig3, use_container_width=True)
    st.dataframe(hist[["country", "year_early", "ownership_early", "year_recent", "ownership_recent",
                        "ownership_change_per_year"]].round(2), use_container_width=True, hide_index=True)
    st.caption(
        "Kenya and Tanzania show sustained decline despite very different starting points (49.2% and 24.7% "
        "respectively) — the cross-sectional snapshot alone would have missed that Kenya is trending toward "
        "Tanzania's problem, not exempt from it. Rwanda's rate of gain (+3.30 pts/year) is roughly 3x the "
        "magnitude of Kenya/Tanzania's decline rate — a compressed, policy-era shift, not a slow structural drift."
    )
    st.caption("Source: World Bank Enterprise Surveys, multiple country-profile vintages, 2011-2025.")

with tab5:
    st.subheader("Robustness Checks")
    st.markdown(
        "With only 4-5 countries, this project cannot rely on statistical significance. Instead, findings are "
        "**triangulated across independent data cuts**, and every relationship is stress-tested by removing "
        "one country at a time. This tab shows the most important result of that process."
    )
    st.error(
        "**Leave-one-out test: the 'governance change predicts ownership change' pattern reverses without Rwanda.**\n\n"
        "With Rwanda included, governance-change and ownership-change correlate at r = +0.66 (n=5) — weak "
        "positive. **Remove Rwanda and the correlation among the remaining four countries is r = -0.98** — "
        "a near-perfect *negative* relationship. This means the apparent positive pattern was carried entirely "
        "by one country. Rwanda is best read as a genuine outlier explained by specific policy (its 1999 land "
        "law reform granting women inheritance/property rights), not evidence of a general governance-ownership mechanism."
    )
    gov_chg = pd.read_csv("data/governance_change_vs_ownership_change.csv")
    fig5 = px.scatter(gov_chg, x="gov_change_per_year", y="ownership_change_per_year", text="country",
                      height=450, title="Governance Change vs. Ownership Change (annualized rates)")
    fig5.update_traces(textposition="top center", marker=dict(size=16))
    fig5.update_layout(xaxis_title="Governance state capacity, change/year", yaxis_title="Female ownership, change/year")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### Triangulation Matrix")
    matrix = pd.DataFrame([
        ["Kenya/Tanzania ownership decline", "✅", "✅", "✅ (Tanzania)", "✅", "—"],
        ["Rwanda's ownership surge is real", "✅", "—", "✅", "✅", "⚠️ drives the whole correlation alone"],
        ["\"Governance change → ownership change\"", "—", "—", "—", "✅ (n=5 only)", "❌ reverses without Rwanda"],
        ["Ethiopia's ownership rises with firm size", "✅", "—", "✅", "⚠️ contradicts overall decline", "—"],
    ], columns=["Finding", "Cross-sectional", "Regional benchmark", "Firm-size trend", "Historical trend", "Leave-one-out"])
    st.dataframe(matrix, use_container_width=True, hide_index=True)
    st.caption(
        "A finding passing 3-4 independent checks (Kenya/Tanzania decline) is far more credible than one "
        "passing only 1 (the governance-change correlation) — this table makes that distinction explicit "
        "rather than presenting every finding with equal confidence."
    )

# ---------------------------------------------------------------------
# TAB 4: Country-year time series
# ---------------------------------------------------------------------
with tab4:
    st.subheader("Explore the Full Time Series (2010-2025)")
    country_pick = st.multiselect("Countries", panel["country"].unique().tolist(),
                                   default=panel["country"].unique().tolist())
    numeric_cols = panel.select_dtypes("number").columns.tolist()
    numeric_cols = [c for c in numeric_cols if c != "year"]
    indicator_pick = st.selectbox("Indicator", numeric_cols)

    plot_df = panel[panel["country"].isin(country_pick)]
    fig5 = px.line(plot_df, x="year", y=indicator_pick, color="country", markers=True, height=500)
    st.plotly_chart(fig5, use_container_width=True)
    st.caption("Sources: World Bank Worldwide Governance Indicators, World Development Indicators, "
               "and UNHCR Refugee Data Finder.")

st.divider()
st.caption("Built by Lisa Uwonkunda · Data: World Bank (WGI, WDI, Enterprise Surveys) and UNHCR Refugee "
           "Data Finder, 2010-2025 · All country-level figures are real published statistics, not modeled.")
