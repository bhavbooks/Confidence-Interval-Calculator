import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st


''' app layout '''

st.set_page_config(page_title='Confidence Interval Calculator - for Z approach', layout='wide', initial_sidebar_state='expanded')

# Custom styling (used GPT for this)
st.markdown("""
    <style>
    .metric-box {padding: 10px; border-radius: 8px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;}
    .footer {text-align: center; padding: 20px; color: #888; font-size: 0.9em; border-top: 1px solid #ddd; margin-top: 30px;}
    </style>
""", unsafe_allow_html=True)

## header

col1, col2 = st.columns([3,1])
with col1:
    st.title('Confidence Interval Calculator')
    st.markdown('*Z-Procedure for Population Mean Estimation*')
with col2:
    st.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/bhavv77)    '''added my linkedin here'''
    """)


## taking inputss from the user
with st.sidebar:
    st.header('⚙️ Configuration')
    confidence_level = st.slider('Confidence Level (%)', 50, 99.9, 95.0, 0.1)
    sample_mean = st.number_input('Sample Mean (μ)', value=100.0)
    population_std_dev = st.number_input('Population Std Dev (σ)', value=15.0, min_value=0.1)
    sample_size = st.number_input('Sample Size (n)', value=30, min_value=1, step=1)