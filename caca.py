import streamlit as st

# Judul aplikasi
st.title('Aplikasi Penjumlahan Sederhana')

# Input angka pertama
angka1 = st.number_input('Masukkan angka pertama:', value=0)

# Input angka kedua
angka2 = st.number_input('Masukkan angka kedua:', value=0)

# Tombol untuk melakukan penjumlahan
if st.button('Jumlahkan'):
    hasil = angka1 + angka2
    st.write(f'Hasil penjumlahan {angka1} + {angka2} adalah {hasil}')