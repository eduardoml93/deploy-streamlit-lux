import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import lux
import io
import os

def app():
    st.set_page_config(layout="wide")
    st.title('Lux Streamlit EDA App')
    st.success('Check out these cool visualizations!')

    dir = os.getcwd()
    list_csv = os.listdir(dir)
    list_csv = [i for i in list_csv if i.endswith('.csv')]
    
    # uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    uploaded_file = st.selectbox("Choose a CSV file", list_csv, index=0)
    sep = st.selectbox("Choose a separator", [',', ';', '\t'], index=0)
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file, sep=sep)
        st.dataframe(df)

        export_file = 'visualizations.html'
        df.save_as_html(export_file)
        html = open(export_file, 'r').read()
        components.html(html, width=1200, height=800, scrolling=True)

app()

