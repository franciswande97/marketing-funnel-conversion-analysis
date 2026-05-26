import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.metrics import calculate_kpis


# Page Config
st.set_page_config(
    page_title="Funnel Analysis",
    page_icon="📉",
    layout="wide"
)

st.title("📉 Funnel Analysis")
st.caption("User drop-off across marketing funnel stages")


# Load Data
users, ads, campaigns, events = load_data()


# Get KPIs from metrics.py
kpis = calculate_kpis(events)


# Funnel DataFrame
funnel_df = pd.DataFrame({
    "Stage": ["Impression", "Click", "Purchase"],
    "Count": [
        kpis["impressions"],
        kpis["clicks"],
        kpis["purchases"]
    ]
})


# Funnel Chart
fig = px.funnel(
    funnel_df,
    x="Count",
    y="Stage",
    title="Marketing Funnel Flow"
)

st.plotly_chart(fig, use_container_width=True)


# Metrics (use KPI outputs ONLY)
col1, col2, col3 = st.columns(3)

col1.metric(
    "Impression → Click",
    f"{kpis['ctr']:.2f}%"
)

col2.metric(
    "Click → Purchase",
    f"{kpis['conversion_rate']:.2f}%"
)

col3.metric(
    "Overall Conversion",
    f"{kpis['overall_conversion']:.2f}%"
)