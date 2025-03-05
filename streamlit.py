import streamlit as st
import pandas as pd
import numpy as np

st.write('first code')
st.header('dkfj')
st.subheader('dlkfjk')

df = pd.DataFrame({
  'first column': ['roshan', 'dkfj', 'qe', 'df'],
  'second column': [10, 20, 30, 40]
})

st.table(df)

st.write(df)
st.line_chart(df['first column'])

st.slider('x')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.076090, 72.877426],
    columns=['lat', 'lon'])

st.map(map_data)
st.text_input('enter your name')

option = st.selectbox('Which number do you like best?',
     df['first column'])

'you selected ', option

