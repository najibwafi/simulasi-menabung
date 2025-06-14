import streamlit as st
st.title("PROGRAM HITUNG TABUNGAN")
i=1
total=0
tabungan=(st.number_input("masukan tabungan anda :"))
lama_waktu=(st.number_input("masukan lama waktu :"))

if st.button("hasil tabungan anda klik disini"):
  while i<lama_waktu:
    total=total+tabungan
    total=total*1.02
    i=i+1
    st.write(f" tabungan anda pada bulanke {i} adalah : {total}")
st.write(f"total tabungan anda pda bulan terakhir adalah :{total}")