import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data


# Page Config
st.set_page_config(
    page_title="Campaign Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Campaign Performance")
st.caption("Analyzing marketing campaign effectiveness")


# Load Data
users, ads, campaigns, events = load_data()


# Merge datasets
ads_events = events.merge(ads, on="ad_id", how="left")
full_data = ads_events.merge(campaigns, on="campaign_id", how="left")


# Campaign Performance Metrics

campaign_summary = full_data.groupby("name").agg(
    impressions=("event_type", lambda x: (x == "Impression").sum()),
    clicks=("event_type", lambda x: (x == "Click").sum()),
    purchases=("event_type", lambda x: (x == "Purchase").sum()),
    likes=("event_type", lambda x: (x == "Like").sum()),
    comments=("event_type", lambda x: (x == "Comment").sum()),
    shares=("event_type", lambda x: (x == "Share").sum())
).reset_index()


# Conversion calculations
campaign_summary["ctr"] = (
    campaign_summary["clicks"] / campaign_summary["impressions"] * 100
)

campaign_summary["conversion_rate"] = (
    campaign_summary["purchases"] / campaign_summary["clicks"] * 100
)

campaign_summary["overall_conversion"] = (
    campaign_summary["purchases"] / campaign_summary["impressions"] * 100
)



# KPI ROW (TOP LEVEL)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Campaigns",
    len(campaign_summary)
)

col2.metric(
    "Total Purchases",
    int(campaign_summary["purchases"].sum())
)

col3.metric(
    "Avg Conversion Rate",
    f"{campaign_summary['conversion_rate'].mean():.2f}%"
)


st.divider()


# CAMPAIGN PERFORMANCE CHARTS


# Purchases by Campaign
fig1 = px.bar(
    campaign_summary.sort_values("purchases", ascending=False),
    x="name",
    y="purchases",
    title="Purchases by Campaign"
)

st.plotly_chart(fig1, use_container_width=True)


# CTR by Campaign
fig2 = px.bar(
    campaign_summary.sort_values("ctr", ascending=False),
    x="name",
    y="ctr",
    title="CTR by Campaign"
)

st.plotly_chart(fig2, use_container_width=True)


# Conversion Rate by Campaign
fig3 = px.bar(
    campaign_summary.sort_values("conversion_rate", ascending=False),
    x="name",
    y="conversion_rate",
    title="Conversion Rate by Campaign"
)

st.plotly_chart(fig3, use_container_width=True)


# Budget vs Performance
fig4 = px.scatter(
    campaigns.merge(campaign_summary, on="name"),
    x="total_budget",
    y="purchases",
    size="duration_days",
    color="name",
    title="Budget vs Purchases (Campaign Efficiency)"
)

st.plotly_chart(fig4, use_container_width=True)