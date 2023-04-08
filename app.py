import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./Dataset/df.csv')
df_monthly = pd.read_csv('./Dataset/df_monthly.csv')

min_date = df["datetime"].min()
max_date = df["datetime"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        # label='Rentang Waktu',
        # min_value=min_date,
        # max_value=max_date,
        # value=[min_date, max_date]
    )


def main():
    main_df = df[(df["datetime"] >= str(start_date)) & (df["datetime"] <= str(end_date))]
    # main_df_monthly = df_monthly[(df_monthly["datetime"] >= str(start_date)) & (df_monthly["datetime"] <= str(end_date))]

    st.title("Bike Sharing")
    st.subheader('Jumlah Peminjam Harian')
 
    col1 = st.columns(1)
    
    with col1:
        total_count = main_df.total_count.sum()
        st.metric("Total Peminjam", value=total_count)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        main_df['datetime'],
        main_df["total_count"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

if __name__ == '__main__':
    main()