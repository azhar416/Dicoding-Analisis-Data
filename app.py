import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('./Dataset/df.csv')
df_monthly = pd.read_csv('./Dataset/df_monthly.csv')

min_date = pd.to_datetime(df.datetime.min())
max_date = pd.to_datetime(df.datetime.max())
def main():
    # main_df_monthly = df_monthly[(df_monthly["datetime"] >= str(start_date)) & (df_monthly["datetime"] <= str(end_date))]

    st.title("Bike Sharing")
    
    default_start_date = datetime.date(2011, 1, 1)
    default_end_date = datetime.date(2012, 12, 31)
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", default_start_date, min_value=min_date, max_value=max_date)
    
    with col2:
        end_date = st.date_input("Start Date", default_end_date, min_value=min_date, max_value=max_date)
    
    st.subheader('Jumlah Peminjam Harian')

    main_df = df[(df["datetime"] >= str(start_date)) & (df["datetime"] <= str(end_date))]
    st.dataframe(main_df.head(10))
 
    
    # with col1:
    #     total_count = main_df.total_count.sum()
    #     st.metric("Total Peminjam", value=total_count)
    
    # fig, ax = plt.subplots(figsize=(16, 8))
    # ax.plot(
    #     main_df['datetime'],
    #     main_df["total_count"],
    #     marker='o', 
    #     linewidth=2,
    #     color="#90CAF9"
    # )
    # ax.tick_params(axis='y', labelsize=20)
    # ax.tick_params(axis='x', labelsize=15)
    
    # st.pyplot(fig)

if __name__ == '__main__':
    main()