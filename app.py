import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./Dataset/df.csv')
df_monthly = pd.read_csv('./Dataset/df_monthly.csv')

def main():
    st.title("Home Credit Default Prediction!")
    df.head(10)

if __name__ == '__main__':
    main()