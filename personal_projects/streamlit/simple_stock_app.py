import yfinance as yf
import pandas as pd
import streamlit as st
import numpy as np

st.write("""
# Simple Stock Price App

Shown are the stock **Closing Price** and **Volume** of Google!         
""")

#define the ticker symbol
tickersymbol = 'GOOGL'

#get data on this ticker
ticker_data = yf.Ticker(tickersymbol)

#get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d',start='2022-01-01',end='2022-11-13')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)

