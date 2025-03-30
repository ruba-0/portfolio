import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

# Load financial data
def load_data():
    df = pd.read_csv("personal_transactions.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df["Income"] = df["Amount"].where(df["Transaction Type"] == "credit", 0)
    df["Expenses"] = df["Amount"].where(df["Transaction Type"] == "debit", 0).abs()
    return df 

# Budget Tracking
def track_budget(df):
    st.subheader("Budget Tracking")
    st.line_chart(df[['Income', 'Expenses']])
    df['Savings'] = df['Income'] - df['Expenses']
    return df

# Savings Recommendation
def savings_recommendation(df):
    st.subheader("Savings Recommendation")
    avg_savings = df['Savings'].mean()
    st.write(f"Your average monthly savings: ${avg_savings:.2f}")
    return avg_savings


# Market data dictionary
markets = {
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "Gold": "GC=F",
    "Bitcoin": "BTC-USD",
    "Real Estate ETF": "VNQ"
}

# Investment Insights Function
def investment_insights(avg_savings):
    st.subheader("Investment Insights")
    
    market_data = {}
    
    for market, ticker in markets.items():
        try:
            df = yf.download(ticker, period="1y")['Close']
            if df.empty:
                raise ValueError(f"No data for {market}")

            daily_return = df.pct_change().mean()  # Mean daily return
            annualized_roi = daily_return * 252 * 100  # Annualized return in %

            market_data[market] = float(annualized_roi)  # Convert to float

        except Exception as e:
            st.write(f"Error fetching data for {market}: {e}")
            market_data[market] = None  # Skip this market if error occurs
    
    # Remove invalid data before sorting
    sorted_markets = sorted(
        [(market, roi) for market, roi in market_data.items() if roi is not None],
        key=lambda x: x[1],
        reverse=True
    )
    
    # Display the top investment options
    st.write("### Top Markets to Invest In (Based on Last Year’s Performance):")
    
    for market, roi in sorted_markets:
        investment_amount = avg_savings * 0.3  # Allocate 30% of savings for investment
        expected_return = investment_amount * (roi / 100)
        
        st.write(f"**{market}**")
        st.write(f"🔹 **Expected ROI:** {roi:.2f}%")
        st.write(f"🔹 **Suggested Investment:** ${investment_amount:.2f}")
        st.write(f"🔹 **Expected Return:** ${expected_return:.2f}")
        st.write("---")  # Separator for readability



# Streamlit UI
def run_app():
    st.title("Personal Finance Advisor")
    df = load_data()
    df = track_budget(df)
    avg_savings = savings_recommendation(df)
    investment_insights(avg_savings)

if __name__ == "__main__":
    run_app()
