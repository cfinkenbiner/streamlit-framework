# Milestone## https://catie-tdi-milestone-project.herokuapp.com/import streamlit as stimport requestsimport pandas as pd# specific codes for API key = 'QC1O9GVDGRVR6UAU'ticker = 'IBM'size = 'compact'url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize={}&apikey={}'.format(ticker, size, key)response = requests.get(url)json_dict = response.json()metadata = json_dict['Meta Data']final_column_names = ['open', 'high', 'low', 'close', 'adjusted_close',        'volume', 'dividend_amount', 'split_coefficient']data = pd.DataFrame.from_dict(json_dict['Time Series (Daily)'], orient='index')data.rename(columns={col_original:col_new for col_original, col_new in zip(data.columns, final_column_names)}, inplace=True)data['datetime'] = pd.to_datetime(data.index)st.title("Data Incubator - Milestone Project")st.sidebar.write("Author: Catie Finkenbiner")# option2 = st.sidebar.selectbox(#     'Choose your y-axis:',#      final_column_names)# option3 = st.sidebar.selectbox(#     'Choose your legend:',#      final_column_names)# from bokeh.plotting import figure# p = figure(#     title='Alpha Vantage - Time Series Daily Adjusted Dataset',#     x_axis_label='datetime',#     y_axis_label='adjusted_close')# p.line(data['datetime'], data['adjusted_close'], legend_label='Adjusted_Close', line_width=2)# st.bokeh_chart(p, use_container_width=True)st.line_chart(data['adjusted_close'])# import altair as alt# c = alt.Chart(data).mark_circle().encode(#     x='datetime', y='adjusted_close', size='high', color='high', tooltip=['datetime', 'adjusted_close', 'high'])# st.write(c)