import streamlit as st

# Tajuk aplikasi
st.title('Penentu Tahap Suhu')

# Input suhu dari pengguna
temperature = st.number_input('Masukkan suhu (°C):', format="%.1f")

# Tentukan tahap suhu
if temperature >= 30:
    st.write("Keadaan: Panas 🥵")
elif 20 <= temperature < 30:
    st.write("Keadaan: Sederhana 🙂")
else:
    st.write("Keadaan: Sejuk 🥶")




