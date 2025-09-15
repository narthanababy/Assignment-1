# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_prep import load_and_clean

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Marketing Intelligence Dashboard", layout="wide")

# ---------------------------
# Load Data
# ---------------------------
campaigns, biz = load_and_clean()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

# Channel filter
channels = st.sidebar.multiselect(
    "Select Channels",
    campaigns['channel'].unique(),
    default=campaigns['channel'].unique()
)

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [campaigns['date'].min(), campaigns['date'].max()]
)

# ✅ Convert to pandas datetime (fixes dtype errors)
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

# ---------------------------
# Apply Filters
# ---------------------------
mask = (campaigns['channel'].isin(channels)) & (
    campaigns['date'].between(start_date, end_date)
)
filtered = campaigns.loc[mask]

# ---------------------------
# KPI Metrics
# ---------------------------
col1, col2, col3 = st.columns(3)

total_spend = filtered['spend'].sum()
total_rev = filtered['attributed_revenue'].sum()
roas_value = total_rev / total_spend if total_spend > 0 else 0

col1.metric("Total Spend", f"${total_spend:,.0f}")
col2.metric("Attributed Revenue", f"${total_rev:,.0f}")
col3.metric("ROAS", f"{roas_value:.2f}")

# ---------------------------
# Time Series: Spend vs Revenue
# ---------------------------
daily = (
    filtered.groupby('date')
    .agg({'spend': 'sum', 'attributed_revenue': 'sum'})
    .reset_index()
)

fig = px.line(
    daily,
    x='date',
    y=['spend', 'attributed_revenue'],
    labels={'value': 'Amount', 'date': 'Date', 'variable': 'Metric'},
    title="Daily Spend vs Revenue"
)
st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Channel Comparison
# ---------------------------
channel_perf = (
    filtered.groupby('channel')
    .agg({
        'impressions': 'sum',   # ✅ make sure column matches your CSV
        'clicks': 'sum',
        'spend': 'sum',
        'attributed_revenue': 'sum'
    })
    .reset_index()
)

channel_perf['roas'] = channel_perf['attributed_revenue'] / channel_perf['spend']
channel_perf['roas'] = channel_perf['roas'].fillna(0)

st.subheader("Channel Performance")
st.dataframe(channel_perf)

fig2 = px.bar(
    channel_perf,
    x='channel',
    y='roas',
    color='channel',
    hover_data=['spend', 'attributed_revenue'],
    title="ROAS by Channel"
)
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Business KPIs (Optional)
# ---------------------------
if biz is not None and not biz.empty:
    st.subheader("Business Overview")

    biz_daily = (
        biz.groupby('date')
        .agg({'orders': 'sum', 'revenue': 'sum', 'profit': 'sum'})
        .reset_index()
    )

    fig3 = px.line(
        biz_daily,
        x='date',
        y=['orders', 'revenue', 'profit'],
        labels={'value': 'Amount', 'date': 'Date', 'variable': 'Metric'},
        title="Daily Business Metrics"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.dataframe(biz_daily)
