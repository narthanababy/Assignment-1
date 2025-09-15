# Assignment-1

Marketing Intelligence Dashboard

A Streamlit-based interactive dashboard for analyzing marketing campaigns across Facebook, Google, and TikTok, alongside business performance metrics. Visualize KPIs, compare channels, and track campaign performance over time.

🚀 Features

Campaign Data Analysis

Track impressions, clicks, spend, and attributed revenue.

Derived metrics: CTR (Click-Through Rate), CPC (Cost Per Click), ROAS (Return on Ad Spend).

Filter by channels and date range.

Business Performance Overview

Track total orders, new orders, new customers, revenue, profit, and COGS.

Aggregate and visualize daily business metrics.

Interactive Visualizations

Time series charts for spend vs revenue.

Channel-wise performance comparison.

KPI cards for quick insights.

🗂 Repository Structure
marketing-dashboard/
│
├─ data/
│   ├─ Facebook.csv
│   ├─ Google.csv
│   ├─ TikTok.csv
│   └─ Business.csv
│
├─ src/
│   └─ data_prep.py       # Load and clean data, calculate derived metrics
│
├─ dashboard.py           # Streamlit app entry point
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation

⚡ Installation

Clone the repository:

git clone <repo-url>
cd marketing-dashboard


Install dependencies:

pip install -r requirements.txt


Make sure the CSV data files are placed in the data/ folder.

🏃 Run the Dashboard

Start the Streamlit app:

streamlit run dashboard.py


Open the browser at http://localhost:8501 to view the dashboard.

📊 Usage

Use the sidebar filters to select channels and date range.

View KPI cards for total spend, attributed revenue, and ROAS.

Analyze time series trends for spend vs revenue.

Compare channel performance with bar charts and tables.

Explore business metrics for daily orders, revenue, and profit.

🛠 Dependencies

Python 3.10+

pandas

numpy

plotly

streamlit

🔧 Notes

Column names in CSV files must match the expected format:

Campaigns: date, tactic, state, campaign, impression, clicks, spend, attributed revenue

Business: date, # of orders, # of new orders, new customers, total revenue, gross profit, COGS

The src/data_prep.py script standardizes column names and calculates derived metrics for the dashboard.

📌 Author

Developed by Narthana Baby B S
