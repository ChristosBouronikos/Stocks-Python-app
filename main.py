import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide')
st.write("""# Stocks""")
st.write(""" #### by Christos Bouronikos """)
st.write("\n\n\n")

col1, col2 = st.beta_columns(2)
search = col1.text_input(value='GOOGL', label="Search for a ticker: (eg. TSLA, AMZN, MSFT, FB, AAPL, GOOGL, DOW) ")
time_period = '1y'
time_period = col2.selectbox('Pick a time period', ('5d', '1mo', '3mo', '6mo', '1y', '2y', '5y'))

tickerSymbol = search
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = time_period)
st.write(f"{tickerSymbol}   -   " + """**Closing Price**""")
st.area_chart(tickerDf.Close)