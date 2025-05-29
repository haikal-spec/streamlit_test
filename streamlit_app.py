import streamlit as st
import requests

# Set the app title
st.title('My First Streamlit App !!')

# Add a welcome message
st.write('Domain Expansion!')

# Create a text input
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# Display the customized message
st.write('Customized Message:', widgetuser_input)

# Pilihan mata wang
currency_options = ['USD', 'EUR', 'GBP', 'JPY', 'SGD', 'AUD', 'IDR', 'THB', 'CNY']
selected_currency = st.selectbox('Pilih mata wang:', currency_options)

# Input nilai dalam MYR
myr_amount = st.number_input('Masukkan nilai MYR:', min_value=0.0, format="%.2f")

# API call untuk mendapatkan kadar pertukaran
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    
    # Semak jika mata wang yang dipilih ada dalam data
    if selected_currency in rates:
        exchange_rate = rates[selected_currency]
        st.write(f"Kadar pertukaran MYR ke {selected_currency}: {exchange_rate}")

        # Kira jumlah pertukaran
        converted_amount = myr_amount * exchange_rate
        st.write(f"{myr_amount:.2f} MYR = {converted_amount:.2f} {selected_currency}")
    else:
        st.warning(f"Kadar pertukaran untuk {selected_currency} tidak dijumpai.")
else:
    st.error(f"API call failed with status code: {response.status_code}")


