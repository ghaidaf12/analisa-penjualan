import streamlit as st
import pandas as pd

st.title("📊 Analisa Data Penjualan")

uploaded_file = st.file_uploader("Upload file penjualan (.csv / .xlsx)", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ File berhasil dibaca")
    st.write("📄 Preview Data", df.head())

    col_filter = st.selectbox("Pilih kolom untuk filter", df.columns)
    val_filter = st.selectbox("Pilih nilai", df[col_filter].unique())

    filtered_df = df[df[col_filter] == val_filter]
    st.write("📌 Hasil Filter:", filtered_df)

    st.write("📈 Statistik:", filtered_df.describe())
