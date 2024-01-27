import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import lux
import io

def app():
    st.set_page_config(layout="wide")
    st.title('Lux Streamlit EDA App')
    st.success('Check out these cool visualizations!')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        delimiter = st.selectbox("Select Delimiter", ('Comma (,)', 'Semicolon (;)', 'Tab (\t)', 'Space'), index=0)
        df = pd.read_csv(uploaded_file, sep=delimiter.split(' ')[1])
        st.dataframe(df)

        export_file = 'visualizations.html'
        df.save_as_html(export_file)
        html = open(export_file, 'r').read()
        components.html(html, width=1200, height=800, scrolling=True)

app()

