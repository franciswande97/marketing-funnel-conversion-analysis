import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.metrics import calculate_kpis


# PAGE CONFIG

st.set_page_config(
    page_title="Marketing Funnel Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Marketing Funnel Intelligence")
st.caption("Social Media Campaign Performance & Conversion Analytics")


# LOAD DATA

users, ads, campaigns, events = load_data()


# KPIS

kpis = calculate_kpis(events)


# KPI CARDS

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Impressions", f"{kpis['impressions']:,}")
col2.metric("Clicks", f"{kpis['clicks']:,}")
col3.metric("Purchases", f"{kpis['purchases']:,}")
col4.metric("CTR", f"{kpis['ctr']:.2f}%")
col5.metric("Conv. Rate", f"{kpis['conversion_rate']:.2f}%")
col6.metric("Engagement", f"{kpis['engagement_rate']:.2f}%")


st.divider()



# EVENT DISTRIBUTION

event_counts = (
    events["event_type"]
    .value_counts()
    .reset_index()
)

event_counts.columns = ["Event", "Count"]

fig1 = px.bar(
    event_counts,
    x="Event",
    y="Count",
    title="Event Distribution Across Campaigns",
    text="Count"
)

st.plotly_chart(fig1, use_container_width=True)


st.divider()



# PLATFORM PERFORMANCE

platform_data = events.merge(
    ads,
    on="ad_id",
    how="left"
)

platform_summary = (
    platform_data
    .groupby("ad_platform")
    .size()
    .reset_index(name="Events")
)

fig2 = px.pie(
    platform_summary,
    names="ad_platform",
    values="Events",
    title="Event Distribution by Platform"
)

st.plotly_chart(fig2, use_container_width=True)