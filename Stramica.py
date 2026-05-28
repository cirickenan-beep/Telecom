mport streamlit as st

# Sve je spakovano unutar zagrada i provjereno radi u IDLE-u
st.markdown('<style>[data-testid="stAppViewContainer"] {background-color: #FF6600 !important;} h1, h2, p, div, span, label {color: black !important;}</style>', unsafe_allow_html=True)

st.title("Moj BH Telecom")

# 1. Kreiramo stanje u memoriji ako već ne postoji
if "kliknuto" not in st.session_state:
    st.session_state.kliknuto = False

# 2. Ako dugme NIJE kliknuto, prikaži ga na ekranu
if not st.session_state.kliknuto:
    Dalje = st.button("Zaroni u svijet optičkog inteneta")
    if Dalje:
        st.session_state.kliknuto = True
        st.rerun()  

# 3. Ako JE kliknuto, prikaži samo pakete
if st.session_state.kliknuto:
    st.title("Paketi")
    Ponuda_1 = st.button("20mbps/5 , 25,50KM")
    Ponuda_2 = st.button("40mbps/10, 39.99KM")
    Ponuda_3 = st.button("100mbps/30, 69.99KM")
    Ponuda_4 = st.button("200mbps/60, 99.99KM")
