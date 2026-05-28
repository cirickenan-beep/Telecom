import streamlit as st
st.title("Moj BH Telecom")
# 1.
if "kliknuto" not in st.session_state:
 st.session_state.kliknuto = False
#2.
 if not st.session_state.kliknuto:
  Dalje = st.button ("Zaroni u svijet optièkog inteneta")
st.session_state.kliknuto = True
st.return()
if session_state.kliknuto:
 if Dalje:
 st.title("Paketi")
 Ponuda_1 = st.button("20mbps/5 , 25,50KM")
 Ponuda_2 = st.button("40mbps/10, 39.99KM")
 Ponuda_3 = st.button("100mbps/30, 69.99KM")
 Ponuda_4 = st.button("200mbps/60, 90.99KM")

