# Milestone## https://catie-tdi-milestone-project.herokuapp.com/import streamlit as stimport requestsimport pandas as pd# specific codes for API key = 'QC1O9GVDGRVR6UAU'ticker = 'IBM'size = 'compact'url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize={}&apikey={}'.format(ticker, size, key)response = requests.get(url)json_dict = response.json()metadata = json_dict['Meta Data']final_column_names = ['open', 'high', 'low', 'close', 'adjusted_close',        'volume', 'dividend_amount', 'split_coefficient']data = pd.DataFrame.from_dict(json_dict['Time Series (Daily)'], orient='index')data.rename(columns={col_original:col_new for col_original, col_new in zip(data.columns, final_column_names)}, inplace=True)data.index = pd.to_datetime(data.index)st.sidebar.title("Milestone Project")st.sidebar.write("Author: Catie Finkenbiner")st.sidebar.write("Updated: 04/01/2021")st.title("Alpha Avantage Time Series Stock APIs")st.write("Daily Adjusted Dataset")option = st.selectbox(    'What variable are you interested in plotting?',    (final_column_names))st.write('You selected:', option)agree = st.button("Click to see a fun figure:")if agree:    st.area_chart(data[option])