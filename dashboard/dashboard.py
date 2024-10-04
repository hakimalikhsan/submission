import streamlit as slt
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

slt.title('Proyek Analisis Data: Bike Shareing Dataset')

# Memanggil data
day = pd.read_csv('D:/BIT/SMT7/bangkit/day.csv')


# Visualisasi
slt.subheader('Pengaruh Kondisis Cuaca terhadap Angka Perentalan Sepeda')
with slt.container():
    plt.figure(figsize=(8, 5)) 
    plt.bar(day['weathersit'],day['cnt'])
    plt.xticks(ticks=[1, 2, 3, 4], labels=['Clear', 'Mist', 'Light Rain/Snow', 'Heavy Rain/Snow'], fontsize=10)
    plt.xlabel('Weather')
    plt.ylabel('Bike Sharing Count')
    plt.title('Bike Sharing Count by Weather')
    slt.pyplot(plt)
with slt.container():
    plt.figure(figsize=(8, 5)) 
    plt.bar(day['season'], day['cnt'])
    plt.xticks(ticks=[1, 2, 3, 4], labels=['Spring', 'Summer', 'Fall', 'Winter'], fontsize=10)
    plt.xlabel('Season')
    plt.ylabel('Bike Sharing Count')
    plt.title('Bike Sharing Count by Season')
    slt.pyplot(plt)

with slt.expander('Penjelasan:'):
    slt.write(
        '''Dari grafik diatas dapat disimpulkan bahwa kondisi cuaca dan musim sangat berpengaruh terhadap
        banyak peminjaman sepeda. Tetapi pemakaian sepeda tidak terpengaruh oleh kondisi musim.'''
    )

slt.subheader('Pengaruh Temperatur terhadap pemakaian Bike Sharing')

with slt.container():
    plt.figure(figsize=(8, 5)) 
    sns.regplot(x = day['temp'], y = day['cnt'])
    plt.xlabel('Normalized Temperature')
    plt.ylabel('Count')
    plt.title('Temperature vs. Number of Bike Sharing')
    slt.pyplot(plt)

with slt.container():
    plt.figure(figsize=(8, 5))
    sns.regplot(x = day['atemp'], y = day['cnt'])
    plt.xlabel('Normalized Average Temperature')
    plt.ylabel('Count')
    plt.title('Average Temperature vs. Number of Bike Sharing')
    slt.pyplot(plt)

with slt.expander('Penjelasan:'):
    slt.write(
        '''Dari grafik di atas dapat dilihat bahwa penggunaan sepeda bergantung terhadap kondisi temperatur
        keadaan sekitar. Dapat dilihat bahwa semakin rendah temperatur udara, jumlah penggunaan sepeda semakin
        menurun dibandingkan saat temperatur lebih tinggi.'''
    )

slt.caption('Bangkit Academy 2024 Batch 2')