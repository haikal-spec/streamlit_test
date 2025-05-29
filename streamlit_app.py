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

# Mata wang pilihan pengguna
currency_options = ['USD', 'EUR', 'GBP', 'JPY', 'SGD', 'AUD', 'IDR', 'THB', 'CNY']
selected_currency = st.selectbox('Pilih mata wang:', currency_options)

# API call
response = requests.get(f'https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    
    # Semak jika mata wang yang dipilih ada dalam rates
    if selected_currency in rates:
        exchange_rate = rates[selected_currency]
        st.write(f"Kadar pertukaran MYR ke {selected_currency}: {exchange_rate}")
    else:
        st.warning(f"Kadar pertukaran untuk {selected_currency} tidak dijumpai.")
else:
    st.error(f"API call failed with status code: {response.status_code}")

