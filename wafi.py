import streamlit as st


st.title("PROGRAM PENGHITUNG BMI")
Nama=st.text_input("masukan nama anda")


Berat_badan=(st.number_input("masukan berat badan(KG)  :"))
Tinggi_badan=(st.number_input("masukan tinggi badan(cm)  :"))
BMI=Berat_badan/(Tinggi_badan/100)**2
# st.write(BMI)



# st.write('ini web wafi')
# st.number_input("masukan nama ")


if st.button("hasilnya klik disini"):
    if BMI<18.5:
        st.write(f"BMI {Nama} adalah underweight,sebesar{BMI}")
    elif BMI>=18.5 and BMI<=24.9:
        st.write(f"BMI {Nama} adalah normal,sebesar{BMI}")
    elif BMI>=25 and BMI<=29.9:
        st.write(f"BMI {Nama} adalah overweight,sebesar{BMI}")
    elif BMI>=30 and BMI<=34.9:
        st.write(f"BMI {Nama} adalah obese,sebesar{BMI}")
    elif BMI<=35:
        st.write(f"BMI {Nama} adalah extremly obese,sebesar{BMI}")

# st.markdown("wafi")