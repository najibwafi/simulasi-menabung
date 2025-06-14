import streamlit as st
st.title("PROGRAM HITUNG TABUNGAN")
i=1
total=0
tabungan=(st.number_input("masukan tabungan anda :",
                          min_value=1,
                          value=1000000))

lama_waktu=(st.number_input("masukan lama waktu :",
                            min_value=1,
                            value=1,
                            step=1))
bunga=st.slider("masukan bunga tahunan dalam persen",
                min_value=0,
                max_value=20,
                value=2,
                step=1)                            
persen_bunga=bunga/(100*12)
if st.button("hasil tabungan anda klik disini"):
  if tabungan==0:
    st.warning("uang tidak boleh 0")
  elif lama_waktu==0:
    st.warning("bulannya jangan 0")
  else:
    while i<lama_waktu:
      total=total+tabungan
      total=total*(1+persen_bunga)
      i=i+1
      st.success(f" tabungan anda pada bulanke {i+1} adalah :Rp. {int(total)}")
st.success(f"total tabungan anda pda bulan terakhir adalah :Rp. {int(total)}")
