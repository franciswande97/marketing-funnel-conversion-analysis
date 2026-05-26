import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data


# Page Config
st.set_page_config(
    page_title="Audience Insights",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Audience Insights")
st.caption("Understanding who engages and converts")


# Load Data
users, ads, campaigns, events = load_data()


# Merge users with events
user_data = events.merge(users, on="user_id", how="left")


# Add engagement flag
user_data["is_purchase"] = user_data["event_type"] == "Purchase"
user_data["is_click"] = user_data["event_type"] == "Click"


# AGE GROUP ANALYSIS


age_group = user_data.groupby("age_group").agg(
    impressions=("event_type", lambda x: (x == "Impression").sum()),
    purchases=("event_type", lambda x: (x == "Purchase").sum())
).reset_index()

age_group["conversion_rate"] = (
    age_group["purchases"] / age_group["impressions"] * 100
)


fig1 = px.bar(
    age_group,
    x="age_group",
    y="conversion_rate",
    title="Conversion Rate by Age Group"
)

st.plotly_chart(fig1, use_container_width=True)


# GENDER ANALYSIS


gender = user_data.groupby("user_gender").agg(
    impressions=("event_type", lambda x: (x == "Impression").sum()),
    purchases=("event_type", lambda x: (x == "Purchase").sum())
).reset_index()

gender["conversion_rate"] = (
    gender["purchases"] / gender["impressions"] * 100
)

fig2 = px.bar(
    gender,
    x="user_gender",
    y="conversion_rate",
    title="Conversion Rate by Gender"
)

st.plotly_chart(fig2, use_container_width=True)

# COUNTRY ANALYSIS

country = user_data.groupby("country").agg(
    impressions=("event_type", lambda x: (x == "Impression").sum()),
    purchases=("event_type", lambda x: (x == "Purchase").sum())
).reset_index()

country["conversion_rate"] = (
    country["purchases"] / country["impressions"] * 100
)

fig3 = px.bar(
    country,
    x="country",
    y="conversion_rate",
    title="Conversion Rate by Country"
)

st.plotly_chart(fig3, use_container_width=True)