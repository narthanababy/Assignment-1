import pandas as pd
import numpy as np

def load_and_clean():
    # Load CSVs
    fb = pd.read_csv("data/Facebook.csv", parse_dates=['date'])
    gg = pd.read_csv("data/Google.csv", parse_dates=['date'])
    tt = pd.read_csv("data/TikTok.csv", parse_dates=['date'])
    biz = pd.read_csv("data/Business.csv", parse_dates=['date'])

    # Standardize and add channel column
    fb['channel'] = 'Facebook'
    gg['channel'] = 'Google'
    tt['channel'] = 'TikTok'

    # Combine campaign data
    campaigns = pd.concat([fb, gg, tt], ignore_index=True)

    # ✅ Rename columns to standard names
    campaigns = campaigns.rename(columns={
        'impression': 'impressions',
        'attributed revenue': 'attributed_revenue'
    })

    # Derived metrics
    campaigns['ctr'] = np.where(campaigns['impressions'] > 0,
                                campaigns['clicks'] / campaigns['impressions'], 0)
    campaigns['cpc'] = np.where(campaigns['clicks'] > 0,
                                campaigns['spend'] / campaigns['clicks'], np.nan)
    campaigns['roas'] = np.where(campaigns['spend'] > 0,
                                 campaigns['attributed_revenue'] / campaigns['spend'], np.nan)

    # Standardize business data columns
    biz = biz.rename(columns={
        '# of orders': 'orders',
        '# of new orders': 'new_orders',
        'new customers': 'new_customers',
        'total revenue': 'revenue',
        'gross profit': 'profit',
        'COGS': 'cogs'
    })

    return campaigns, biz
