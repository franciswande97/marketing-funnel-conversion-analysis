import pandas as pd
import streamlit as st

@st.cache_data

def load_data():
    
    users = pd.read_csv("data/processed/users.csv")
    
    ads = pd.read_csv("data/processed/ads.csv")
    
    campaigns = pd.read_csv("data/processed/campaigns.csv")
    
    events = pd.read_csv("data/processed/ad_events.csv")
    
    return users, ads, campaigns, events