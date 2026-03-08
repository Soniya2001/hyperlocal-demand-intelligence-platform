# OneMindAI – Hyperlocal Demand Intelligence Platform

## Problem
Retailers often suffer from stock imbalance across regions.

## Solution
OneMindAI uses ML forecasting and GenAI insights to predict demand and recommend inventory redistribution.

## Key Features
• ML-based demand forecasting
• Hyperlocal inventory analysis
• Intelligent stock redistribution
• GenAI strategic summaries (AWS Bedrock)
• Streamlit analytics dashboard

💡 Solution

OneMindAI combines machine learning + generative AI to deliver actionable inventory intelligence.

The platform:

1️⃣ Forecasts demand using machine learning
2️⃣ Identifies high-demand and surplus regions
3️⃣ Generates optimal stock redistribution plans
4️⃣ Produces AI-powered executive strategy summaries

This allows retailers to make data-driven operational decisions in real time.

✨ Key Features
📊 Hyperlocal Inventory Analytics
💡 Solution

OneMindAI combines machine learning + generative AI to deliver actionable inventory intelligence.

The platform:

1️⃣ Forecasts demand using machine learning
2️⃣ Identifies high-demand and surplus regions
3️⃣ Generates optimal stock redistribution plans
4️⃣ Produces AI-powered executive strategy summaries

This allows retailers to make data-driven operational decisions in real time.

✨ Key Features
📊 Hyperlocal Inventory Analytics
💡 Solution

OneMindAI combines machine learning + generative AI to deliver actionable inventory intelligence.

The platform:

1️⃣ Forecasts demand using machine learning
2️⃣ Identifies high-demand and surplus regions
3️⃣ Generates optimal stock redistribution plans
4️⃣ Produces AI-powered executive strategy summaries

This allows retailers to make data-driven operational decisions in real time.

✨ Key Features
📊 Hyperlocal Inventory Analytics
Analyze inventory across multiple regions

Identify slow-moving products

Track stock vs demand ratios

📈 ML Demand Forecasting

Uses Linear Regression to predict product demand

Generates region-level demand insights

🔄 Intelligent Stock Redistribution

Automatically detects supply-demand imbalance

Suggests optimal inventory transfer between regions

🧠 GenAI Strategic Insights

Generates executive-level strategy summaries

Powered by AWS Bedrock (Claude)

🖥 Interactive Dashboard

Built with Streamlit

Real-time analytics and business metrics

🏗 System Architecture
User Interface (Streamlit Dashboard)
        │
        ▼
Inventory Dataset
        │
        ▼
Machine Learning Forecast Model
        │
        ▼
Redistribution Engine
        │
        ▼
AWS Bedrock (Claude)
        │
        ▼
Strategic Business Insights
🛠 Tech Stack
Technology	Purpose
Python	Core development
Streamlit	Web dashboard
Pandas	Data analysis
Scikit-Learn	Machine learning forecasting
AWS Bedrock	Generative AI insights
Boto3	AWS integration
EC2	Cloud deployment
📂 Project Structure
hyperlocal-demand-intelligence-platform/

app.py

ui_pages/
    dashboard.py
    inventory.py
    forecasting.py
    matching.py

services/
    forecasting_service.py
    redistribution_service.py
    bedrock_client.py

utils/
    data_loader.py
    metrics.py

data/
    hyperlocal_inventory_data.csv

dependencies.txt
README.md
LICENSE
🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/hyperlocal-demand-intelligence-platform.git
2️⃣ Install dependencies
pip install -r dependencies.txt
3️⃣ Configure AWS credentials (for Bedrock)
aws configure

Provide:

AWS Access Key
AWS Secret Key
Region: ap-south-1
4️⃣ Run the Streamlit app
streamlit run app.py

The application will launch at:

http://localhost:8501
📊 Example Insights Generated

The system automatically generates insights such as:

High-demand regions requiring stock

Surplus inventory locations

Redistribution plans between regions

Estimated revenue loss risk

Strategic AI-generated executive summaries

