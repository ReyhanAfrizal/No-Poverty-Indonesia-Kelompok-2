import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


st.set_page_config(page_title='Dashboard Statistic Angka Kemiskinan')
st.subheader('DASHBOARD ANGKA KEMISKINAN DI INDONESIA')
# data
dataset_file = 'Data Final.xlsx'
Sheet_name = 'Data Final'

df = pd.read_excel(dataset_file, sheet_name=Sheet_name,
                   usecols='A:G', header=0)
provinsi = df[df["Wilayah"] != 'INDONESIA']
indo = df[df["Wilayah"] == 'INDONESIA']
indo.drop(columns='Wilayah')
st.image(Image.open(
    '../Visualisasi_Data/map.png'))
st.text('')
st.text('')
st.text('')
st.subheader('Jumlah Penduduk Miskin di Indonesia per Tahun')
bar_chart = px.bar(indo,
                   x='Tahun', y='Jumlah Penduduk Miskin (Ribu Jiwa)')
st.plotly_chart(bar_chart)

st.dataframe(provinsi)
persentase_pend_miskin = px.line(provinsi, title='Persentase Penduduk Miskin di Indonesia Berdasarkan Provinsi',
                                 x='Tahun', y='Persentase Masyarakat Miskin', line_group='Wilayah', color='Wilayah',)
Jumlah_pend_miskin = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
                             x='Tahun', y='Jumlah Penduduk Miskin (Ribu Jiwa)', line_group='Wilayah', color='Wilayah',)
b1, b2 = st.columns(2)
b1.plotly_chart(persentase_pend_miskin)
b2.plotly_chart(Jumlah_pend_miskin)
rasio_gini = px.line(provinsi, title='Rasio Gini di Indonesia Berdasarkan Provinsi',
                     x='Tahun', y='Gini Rasio', line_group='Wilayah', color='Wilayah',)
st.plotly_chart(rasio_gini)

c1, c2 = st.columns(2)
makan = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
                x='Tahun', y='Garis Kemiskinan Makanan (Rupiah/Kapita/Bulan)', line_group='Wilayah', color='Wilayah',)
non_makan = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
                    x='Tahun', y='Garis Kemiskinan Non Makanan (Rupiah/Kapita/Bulan)', line_group='Wilayah', color='Wilayah',)
c1.plotly_chart(makan)
c2.plotly_chart(non_makan)

st.text('Selengkapnya dapat mengunjungi link berikut:')
linkgit = '[Github](https://github.com/ReyhanAfrizal/No-Poverty-Indonesia-Kelompok-2)'
linkml = '[Machine Learning](https://github.com/ReyhanAfrizal/No-Poverty-Indonesia-Kelompok-2/blob/master/Tubes_Visdas_2.ipynb)'
st.markdown(linkgit, unsafe_allow_html=True)
st.markdown(linkml, unsafe_allow_html=True)
