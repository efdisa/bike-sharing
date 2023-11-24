import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
day_df = pd.read_csv("dashboard/day.csv")
hour_df = pd.read_csv("dashboard/hour.csv")

# Visualization
st.header('Bike Sharing ✨')

# Daily Sharing
st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)

with col1:
  # hitung jumlah semua data
  total_sharing = day_df['cnt'].sum()
  st.metric(label='Total Bike Sharing', value=total_sharing)

with col2:
  # hitung jumlah yang registered
  registered_sharing = day_df['registered'].sum()
  st.metric(label='Registered Bike Sharing', value=registered_sharing)

with col3:
  # hitung jumlah yang casual
  casual_sharing = day_df['casual'].sum()
  st.metric(label='Casual Bike Sharing', value=casual_sharing)
  
# Pengaruh cuaca terhadap jumlah sharing per jam 
st.subheader('Pengaruh cuaca(suhu, kelembaban, kecepatan angin dan cuaca) terhadap jumlah sharing per jam')
col1, col2 = st.columns(2)

with col1:
  # bike rental vs temperature
  fig, ax = plt.subplots(figsize=(10, 5))
  sns.lineplot(data=hour_df, x='temp', y='cnt', ax=ax)
  plt.xlabel('Temperature')
  plt.ylabel('Count of total rental bikes')
  plt.title('Bike rentals vs Temperature')
  st.pyplot(fig)
  
  # bike rental vs windspeed
  fig, ax = plt.subplots(figsize=(10, 5))
  sns.lineplot(data=hour_df, x='windspeed', y='cnt', ax=ax)
  plt.xlabel('Windspeed')
  plt.ylabel('Count of total rental bikes')
  plt.title('Bike rentals vs Windspeed')
  st.pyplot(fig)
  
with col2:
  # bike rental vs humidity
  fig, ax = plt.subplots(figsize=(10, 5))
  sns.lineplot(data=hour_df, x='hum', y='cnt', ax=ax)
  plt.xlabel('Humidity')
  plt.ylabel('Count of total rental bikes')
  plt.title('Bike rentals vs Humidity')
  st.pyplot(fig)
  
  # bike rental vs weather
  fig, ax = plt.subplots(figsize=(10, 5))
  sns.lineplot(data=hour_df, x='weathersit', y='cnt', ax=ax)
  plt.xlabel('Weather')
  plt.ylabel('Count of total rental bikes')
  plt.title('Bike rentals vs Weather')
  st.pyplot(fig)
  

# Perbedaan signifikan antara jumlah sharing per jam pada hari biasa dan hari libur
st.subheader('Perbedaan signifikan antara jumlah sharing per jam pada hari biasa dan hari libur')

# Membuat dua sampel yang berisi jumlah penyewaan sepeda di hari kerja dan akhir pekan
weekday_df = hour_df[hour_df['workingday']==1]
weekend_df = hour_df[hour_df['workingday']==0]

# visualisasi yang menunjukkan jumlah penyewaan sepeda per jam di hari kerja dan akhir pekan
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=weekday_df, x='hr', y='cnt', ax=ax, label='Weekday')
sns.lineplot(data=weekend_df, x='hr', y='cnt', ax=ax, label='Weekend')
plt.xlabel('Hour')
plt.ylabel('Count of total rental bikes')
plt.title('Bike rentals vs Hour')
st.pyplot(fig)

# Tren jumlah penyewaan sepeda sepanjang tahun 2011 dan 2012
st.subheader('Tren jumlah penyewaan sepeda sepanjang tahun 2011 dan 2012')

# membuat dataframe baru yang berisi jumlah penyewaan sepeda per hari
df_year = hour_df.groupby(['dteday', 'yr'])[['cnt']].sum().reset_index()

# visualisasi yang menunjukkan jumlah penyewaan sepeda per bulan di tahun 2011 dan 2012
fig, ax = plt.subplots(figsize=(20,10))
sns.lineplot(x='dteday', y='cnt', hue='yr', data=df_year)
plt.xlabel('Date')
plt.ylabel('Total rental bikes')
plt.title('Bike rentals per day for each year')
st.pyplot(fig)