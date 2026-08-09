import streamlit as st
import random
import time

st.markdown("""
    <style>
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .stTextArea textarea {
        background-color: #1e1f20 !important;
        color: #e3e3e3 !important;
        border-radius: 12px !important;
        border: 1px solid #333538 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🧠 Hashim")
st.caption("Tvoj lični AI sportski analitičar.")

st.markdown("Zdravo! Unesi parove za svoj tiket u polje ispod (svaki u novi red) i klikni dugme za analizu.")

sport_izbor = st.radio("Izaberi sport:", ["Fudbal ⚽", "Košarka 🏀"], horizontal=True)

parovi_input = st.text_area(
    "Unesi parove (svaki u novi red):", 
    placeholder="Real Madrid - Barcelona\nManchester City - Arsenal\nInter - Milan",
    height=150
)

if st.button("🚀 Pokreni analizu tiketa", type="primary"):
    if parovi_input.strip():
        parovi_lista = [p.strip() for p in parovi_input.split("\n") if p.strip()]
        
        with st.spinner(f"Hashim analizira {len(parovi_lista)} parova..."):
            time.sleep(1)
            
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
                * 🔥 Over 2.5 gola: **{sansa_golova}%**
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
    else:
        st.warning("Molimo te da uneseš barem jedan par.")

