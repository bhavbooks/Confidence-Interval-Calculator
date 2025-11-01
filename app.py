import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st
from scipy.stats import norm


''' app layout '''

st.set_page_config(page_title='Confidence Interval Calculator', layout='wide', initial_sidebar_state='expanded')

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
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/bhavv77) 
    """)


## taking inputss from the user
with st.sidebar:
    st.header('⚙️ Configuration')
    confidence_level = st.slider('Confidence Level (%)', 50.0, 99.9, 95.0, 0.1)
    sample_mean = st.number_input('Sample Mean (μ)', value=100.0)
    population_std_dev = st.number_input('Population Std Dev (σ)', value=15.0, min_value=0.1)
    sample_size = st.number_input('Sample Size (n)', value=30, min_value=1, step=1)

# calculating Confidence Interval
z_score = norm.ppf(1 - (1 - confidence_level / 100) / 2)
margin_of_error = z_score * (population_std_dev / np.sqrt(sample_size))
lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error

# Displaying major components
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric('Z-Score', f'{z_score:.3f}', f'CL: {confidence_level:.1f}%')
with col2:
    st.metric('Margin of Error', f'{margin_of_error:.3f}', f'σ/√n: {population_std_dev/np.sqrt(sample_size):.3f}')
with col3:
    st.metric('Lower Bound', f'{lower_limit:.2f}')
with col4:
    st.metric('Upper Bound', f'{upper_limit:.2f}')

st.success(f'**Confidence Interval:** ({lower_limit:.2f}, {upper_limit:.2f})')

## Visualising (used GPT)
col_chart, col_dist = st.columns(2)

with col_chart:
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    x = np.linspace(lower_limit - margin_of_error, upper_limit + margin_of_error, 100)
    y = norm.pdf(x, sample_mean, population_std_dev / np.sqrt(sample_size))
    
    ax1.fill_between(x, y, alpha=0.3, color='#667eea', label='CI Region')
    ax1.plot(x, y, color='#667eea', linewidth=2.5)
    ax1.axvline(sample_mean, color='#2ecc71', linestyle='--', linewidth=2, label='Sample Mean')
    ax1.axvline(lower_limit, color='#e74c3c', linestyle=':', linewidth=2, label='Bounds')
    ax1.axvline(upper_limit, color='#e74c3c', linestyle=':', linewidth=2)
    
    ax1.set_xlabel('Value', fontsize=11)
    ax1.set_ylabel('Probability Density', fontsize=11)
    ax1.set_title('CI Distribution Visualization', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.grid(alpha=0.3)
    st.pyplot(fig1, use_container_width=True)

with col_dist:
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    bounds = [lower_limit, upper_limit]
    colors = ['#e74c3c', '#2ecc71']
    ax2.barh(['Lower', 'Upper'], bounds, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    ax2.axvline(sample_mean, color='#f39c12', linestyle='--', linewidth=2.5, label='Sample Mean')
    ax2.set_xlabel('Value', fontsize=11)
    ax2.set_title('Interval Bounds', fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(axis='x', alpha=0.3)
    st.pyplot(fig2, use_container_width=True)




# Footer for personal Showcase 🙂
st.markdown("""
    <div class="footer">
    Built by <b>Bhavesh</b> | 
    <a href="https://linkedin.com/in/bhavv77" target="_blank">LinkedIn</a> | 
    Economics Major, DU
    </div>
""", unsafe_allow_html=True)

