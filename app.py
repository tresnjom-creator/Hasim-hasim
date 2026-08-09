import streamlit as st

st.title("⚽🏀 AI Sportski Analitičar")
st.write("Aplikacija za automatsko predviđanje i simulaciju (pobjednik, više od 2.5 gola, zbroj koševa).")

tim1 = st.text_input("Unesi ime domaćina:")
tim2 = st.text_input("Unesi ime gosta:")

if st.button("Pokreni AI Analizu"):
    if tim1 and tim2:
        st.info(f"Sistem se priprema za automatsko prikupljanje podataka za meč: {tim1} vs {tim2}...")
    else:
        st.warning("Molim te unesi oba tima.")
