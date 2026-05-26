import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.metrics import calculate_kpis


# Page Config
st.set_page_config(
    page_title="Recommendations",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Recommendations Engine")
st.caption("Data-driven marketing insights and actions")


# Load Data
users, ads, campaigns, events = load_data()

kpis = calculate_kpis(events)


# BUSINESS CONTEXT SUMMARY


st.subheader("📊 Performance Summary")

col1, col2, col3 = st.columns(3)

col1.metric("CTR", f"{kpis['ctr']:.2f}%")
col2.metric("Conversion Rate", f"{kpis['conversion_rate']:.2f}%")
col3.metric("Engagement Rate", f"{kpis['engagement_rate']:.2f}%")


st.divider()


# INSIGHT 1: FUNNEL DROP-OFF


st.subheader("📉 Funnel Insight")

if kpis["ctr"] < 15:
    st.warning(
        "High drop-off between Impression → Click. "
        "Creative or targeting may need improvement."
    )
else:
    st.success(
        "Impression → Click performance is strong."
    )


if kpis["conversion_rate"] < 10:
    st.warning(
        "Low Click → Purchase conversion. "
        "Landing page or offer may not be effective."
    )
else:
    st.success(
        "Click → Purchase conversion is performing well."
    )


# INSIGHT 2: ENGAGEMENT


st.subheader("📢 Engagement Insight")

if kpis["engagement_rate"] < 20:
    st.warning(
        "Low engagement rate detected. "
        "Content may not be resonating with audience."
    )
else:
    st.success(
        "Engagement levels are healthy."
    )


# INSIGHT 3: STRATEGIC RECOMMENDATIONS

st.subheader("🧠 Strategic Recommendations")

st.write(
    """
    • Improve ad creatives to increase click-through rate  
    • Optimize landing pages to improve conversion after click  
    • Focus budget on high-performing campaigns identified earlier  
    • Target age groups with higher conversion rates (from audience analysis)  
    • Reduce spend on low-performing platforms or campaigns  
    """
)


# FINAL SUMMARY


st.divider()

st.success(
    "Project Complete: Marketing Funnel Intelligence System successfully built."
)