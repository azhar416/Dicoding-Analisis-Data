import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('./Dataset/df.csv')
df_monthly = pd.read_csv('./Dataset/df_monthly.csv')

df['datetime']=pd.to_datetime(df.datetime)
min_date = df.datetime.min()
max_date = df.datetime.max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

def main():
    main_df_monthly = df_monthly[(df_monthly["datetime"] >= str(start_date)) & (df_monthly["datetime"] <= str(end_date))]
    main_df = df[(df["datetime"] >= str(start_date)) & (df["datetime"] <= str(end_date))]

    st.title("Bike Sharing")
 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        casual_count = main_df.casual.sum()
        st.metric("Casual User", value=casual_count)

    with col2:
        registered_count = main_df.registered.sum()
        st.metric("Registered User", value=registered_count)

    with col3:
        total_count = main_df.total_count.sum()
        st.metric("Total User", value=total_count)
    
    st.subheader('Jumlah Peminjam Harian')
    fig, ax =  plt.subplots(1, 1, figsize = (16,10))
    ax.plot(
        main_df["datetime"],
        main_df["total_count"], 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

    st.subheader('Jumlah Peminjam Bulanan')
    fig, ax =  plt.subplots(1, 1, figsize = (16,10))
    ax.plot(
        main_df_monthly["datetime"],
        main_df_monthly["total_count"], 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15, rotation=45)
    st.pyplot(fig)



if __name__ == '__main__':
    main()