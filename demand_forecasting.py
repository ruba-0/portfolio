import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Load dataset 
def load_data():
    df = pd.read_csv("walmart_sales.csv")  # Load CSV
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')  # Convert 'Date' to datetime
    df.set_index("Date", inplace=True)  # Set 'Date' as index
    df = df.resample('D').sum()
    return df

# Train ARIMA model
def train_arima(df):
    model = ARIMA(df['Weekly_Sales'], order=(5,1,0))
    arima_result = model.fit()
    return arima_result

    # Train Machine Learning model with hyperparameter tuning
def train_ml_model(df):
    df['Day'] = df.index.day
    df['Month'] = df.index.month
    df['Year'] = df.index.year
    df['Weekday'] = df.index.weekday
    
    X = df[['Day', 'Month', 'Year', 'Weekday']]
    y = df['Weekly_Sales']
    
    param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
    model = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=3, scoring='neg_mean_squared_error')
    model.fit(X, y)
    
    return model.best_estimator_


# Evaluate models
def evaluate_models(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = mean_absolute_percentage_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mape, r2

    # Predict future sales and visualize
def forecast_sales():
    df = load_data()

    if df is None or df.empty:
        st.error("Error: Loaded data is empty!")
        return None, None

    arima_model = train_arima(df)
    ml_model = train_ml_model(df)
    
    future_dates = pd.date_range(start=df.index[-1] + timedelta(days=1), periods=30, freq='D')
    future_df = pd.DataFrame(index=future_dates)
    future_df['Day'] = future_df.index.day
    future_df['Month'] = future_df.index.month
    future_df['Year'] = future_df.index.year
    future_df['Weekday'] = future_df.index.weekday
    
    try:
        arima_forecast = arima_model.forecast(steps=30)
        ml_forecast = ml_model.predict(future_df[['Day', 'Month', 'Year', 'Weekday']])
        final_forecast = (arima_forecast + ml_forecast) / 2
        
        forecast_results = pd.DataFrame({'Date': future_dates, 'Predicted_Sales': final_forecast})
        forecast_results.to_csv("daily_forecast.csv", index=False)
        
        return df, forecast_results
    except Exception as e:
        st.error(f"An error occurred during forecasting: {e}")
        return None, None



df, forecast_results = forecast_sales()

# Streamlit Dashboard
def run_streamlit():
    st.title("Walmart Sales Forecasting Dashboard")

    st.subheader("Historical Sales Data")
    st.line_chart(df['Weekly_Sales'])
    
    st.subheader("Predicted Sales for Next 30 Days")
    st.line_chart(forecast_results.set_index('Date')['Predicted_Sales'])
    
    # Combined Visualization
    st.subheader("Actual vs. Predicted Sales")
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x=df.index, y='Weekly_Sales', label='Actual Sales')
    sns.lineplot(data=forecast_results, x='Date', y='Predicted_Sales', label='Forecasted Sales')
    plt.title("Sales Forecasting: Actual vs Predicted")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid()
    
# Apache Airflow DAG for daily predictions
def airflow_dag():
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2025, 1, 1),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }
    
    dag = DAG(
        'daily_sales_forecast',
        default_args=default_args,
        description='Daily Walmart Sales Forecasting',
        schedule_interval=timedelta(days=1),
    )
    
    forecast_task = PythonOperator(
        task_id='forecast_sales',
        python_callable=forecast_sales,
        dag=dag,
    )
    
    forecast_task

if __name__ == "__main__":
    run_streamlit()

    st.pyplot(plt)
    
    st.write("### Download Forecasted Data")
    st.download_button(label="Download CSV", data=forecast_results.to_csv().encode('utf-8'), file_name='sales_forecast.csv', mime='text/csv')

