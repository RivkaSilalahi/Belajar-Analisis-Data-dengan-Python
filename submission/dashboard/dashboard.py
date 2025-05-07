import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('hour.csv')
df['dteday'] = pd.to_datetime(df['dteday'])

# Title and description
st.title("Dashboard Analisis Data - Proyek Analisis Data")
st.markdown("### Visualisasi dan Analisis Data")

# Sidebar filter options
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Pilih Tanggal Mulai", df['dteday'].min())
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", df['dteday'].max())

# Filter data berdasarkan rentang tanggal
filtered_data = df[(df['dteday'] >= pd.to_datetime(start_date)) &
                   (df['dteday'] <= pd.to_datetime(end_date))]

# Tabs for visualizations
tab1, tab2 = st.tabs(["Distribusi Rush Hour", "Pengaruh Suhu"])

with tab1:
    st.subheader("Distribusi Penyewaan Sepeda pada Jam Sibuk")
    rush_hour = filtered_data[(filtered_data['hr'] >= 7) & (filtered_data['hr'] <= 9) |
                              (filtered_data['hr'] >= 17) & (filtered_data['hr'] <= 19)]
    plt.figure(figsize=(10, 6))
    sns.histplot(rush_hour['cnt'], kde=True, color='green')
    plt.xlabel('Jumlah Penyewa')
    plt.ylabel('Frekuensi')
    plt.title('Distribusi Penyewaan Sepeda pada Jam Sibuk')
    st.pyplot(plt)

with tab2:
    st.subheader("Pengaruh Suhu terhadap Jumlah Penyewa Sepeda")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='temp', y='cnt', data=filtered_data, alpha=0.5)
    sns.regplot(x='temp', y='cnt', data=filtered_data, scatter=False, color='red')
    plt.xlabel('Suhu (scaled)')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.title('Pengaruh Suhu terhadap Jumlah Penyewa Sepeda')
    st.pyplot(plt)

# Insight & Recommendations
st.markdown("## Insight & Rekomendasi")
st.markdown("- Pada jam sibuk, jumlah penyewa cenderung meningkat drastis terutama pada pagi dan sore hari.")
st.markdown("- Suhu yang lebih hangat menunjukkan tren peningkatan jumlah penyewa sepeda, dengan puncak aktivitas pada suhu sedang.")
st.markdown("- Disarankan untuk meningkatkan ketersediaan sepeda pada jam sibuk dan suhu ideal untuk memenuhi permintaan yang lebih tinggi.")
