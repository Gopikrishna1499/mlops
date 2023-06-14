import streamlit as st
import yfinance as yf
import pandas as pd



st.title("Stock Market Analysis")

st.write("This is my first app")

tick = "MSFT"
ticker_data = yf.Ticker(tick)



# get historical market data


import datetime
import streamlit as st

d = st.date_input(
    "enter starting date",
    datetime.date(2019, 7, 6))
st.write('Your entered date:', d)


ticker_df = ticker_data.history(period="1mo",start=f"{d}",end="2019-05-05")




st.write(f"we are viewing for {ticker_data}")
st.write(ticker_df)

st.write("volume analysis")
st.line_chart(ticker_df['Volume'])


st.write("close analysis")
st.line_chart(ticker_df['Close'])