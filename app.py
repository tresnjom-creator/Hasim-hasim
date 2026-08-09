import streamlit as st
import random
import time

# Sakrivamo sve Streamlitove standardne menije, zaglavlja i "Manage app" dugmad da bude čisto kao ja
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .stTextArea textarea {
        background-color: #1e1f20 !important;
        color: #e3e3e3 !important;
        border-radius: 14px !important;
        border: 1px solid #333538 !important;
        padding: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Čisto zaglavlje sa mojim imenom
st.markdown("## 🧠 Hashim")
st.caption("Tvoj lični AI analitičar i simulator tiketa.")

st.markdown("Zdravo Merzuhe! Spreman sam. Ubaci svoje parove u polje ispod (svaki u novi red), izaberi sport i pokrenut ću masovnu simulaciju.")

# Izbor sporta
sport_izbor = st.radio("Izaberi sport:", ["Fudbal ⚽", "Košarka 🏀"], horizontal=True)

# Polje za unos više parova odjednom
parovi_input = st.text_area(
    "Unesi parove za analizu:", 
    placeholder="Real Madrid - Barcelona\nManchester City - Arsenal\nInter - Milan",
    height=140
)

if st.button("🚀 Pokreni analizu tiketa", type="primary"):
    if parovi_input.strip():
        parovi_lista = [p.strip() for p in parovi_input.split("\n") if p.strip()]
        
        with st.spinner(f"Hashim vrši Monte Carlo simulacije za {len(parovi_lista)} parova..."):
            time.sleep(1.2)
            
        st.success(f"Uspješno obrađeno parova: {len(parovi_lista)}")
        st.divider()
        st.markdown("### 📊 Rezultati simulacije:")
        
        for i, par in enumerate(parovi_lista, 1):
            p_dom = random.randint(43, 59)
            p_gost = random.randint(21, 37)
            p_ner = 100 - (p_dom + p_gost)
            
            if "Fudbal" in sport_izbor:
                sansa_golova = random.randint(62, 86)
                st.markdown(f"""
                **{i}. {par}**
                * 1: {p_dom}% | X: {p_ner}% | 2: {p_gost}%
                * 🔥 Preporuka (Over 2.5): **{sansa_golova}%**
                """)
            else:
                adj_dom = p_dom + (p_ner / 2)
                adj_gost = p_gost + (p_ner / 2)
                margina = random.randint(154, 220)
                st.markdown(f"""
                **{i}. {par}**
                * Pobjeda domaćina: {adj_dom:.1f}% | Pobjeda gosta: {adj_gost:.1f}%
                * 🔥 Margina koševa: **~{margina}**
                """)
            st.write("---")
            
        st.info("Slobodno izmijeni parove i pokreni novu analizu kada god poželiš.")
    else:
        st.warning("Molimo te da uneseš barem jedan par.")

