import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('Sample Data')

st.sidebar.title("Filter Data") 

df = pd.read_csv('sample_data.csv')

df = df.dropna()

date = ['ClaimReceivedDate','ClaimIncurredDate','FromDate','ToDate','AdmissionDate','DischargeDate','ReviewDate']

for i in date:
    df[i] = pd.to_datetime(df[i])
    
    
description_name = st.sidebar.selectbox('Select description name',df['DESCRIPTION'].unique())
if description_name:
    filtered_df = df[(df['DESCRIPTION'] == description_name)]


st.write(filtered_df)



DC_count = df['DiagnosisCode'].value_counts().to_frame().reset_index().rename(columns = {'DiagnosisCode':'count','index':'DiagnosisCode'})

def bc():
    grouped_df = df.groupby('DESCRIPTION')['FinalAmt'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped_df.plot(kind='barh', ax=ax, color='#051094', width=0.7)

    ax.set_title('Drug Description By Final Amount', fontsize=20, c='black')
    ax.set_xlabel('Description', fontsize=20, c='black')
    ax.set_ylabel('Final Amount', fontsize=20, c='black')
    plt.grid()
    
    return st.pyplot(fig)


def pc():
    fig, ax2 = plt.subplots(figsize=(7,7))
    ax2.pie(DC_count['count'], labels=DC_count['DiagnosisCode'], autopct='%1.2f%%', explode=[0.09, 0.0, 0.0 ])                                
    ax2.axis('equal')                                
    ax2.set_title('Percentage Distribution of DiagnosisCode')                                             

    st.pyplot(fig)
    
    
    
Charts = st.sidebar.selectbox('Select Chart', ['Drug Description By Final Amount','Percentage Distribution of DiagnosisCode'])

if Charts == 'Drug Description By Final Amount':
    bc()
else: 
    pc()
    