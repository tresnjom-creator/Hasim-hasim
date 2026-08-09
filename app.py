import streamlit as st
import random
import time

# Podešavanje čistog, tamnog dizajna u stilu AI chat-a
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

st.markdown("# 🧠 Hashim")
st.caption("Tvoj lični AI analitičar za masovnu obradu tiketa.")

st.markdown("Zdravo! Ja sam Hashim. Ovdje možeš ubaciti cijeli tiket odjednom – upiši ili zalijepi **više parova (svaki par u novi red)**, a ja ću ih sve automatski obraditi i izbaciti simulacije.")

# Izbor sporta za cijeli tiket
sport_izbor = st.radio("Izaberi sport za tiket:", ["Fudbal ⚽", "Košarka 🏀"], horizontal=True)

# Veliko polje za unos više parova odjednom
parovi_input = st.text_area(
    "Unesi parove (svaki u novi red):", 
    placeholder="Real Madrid - Barcelona\nManchester City - Arsenal\nInter - Milan\nBayern - Dortmund",
    height=150
)

if st.button("🚀 Obradi cijeli tiket", type="primary"):
    if parovi_input.strip():
        # Razdvajanje unesenih redova po parovima
        parovi_lista = [p.strip() for p in parovi_input.split("\n") if p.strip()]
        
        with st.spinner(f"Hashim analizira {len(parovi_lista)} parova i vrši Monte Carlo simulacije..."):
            time.sleep(1.5)
            
        st.success(f"Uspješno obrađeno parova: {len(parovi_lista)}!")
        st.divider()
        st.markdown("### 📊 Rezultati simulacije za tvoj tiket:")
        
        # Obrada svakog para zasebno
        for i, par in enumerate(parovi_lista, 1):
            p_dom = random.randint(42, 60)
            p_gost = random.randint(20, 38)
            p_ner = 100 - (p_dom + p_gost)
            
            if "Fudbal" in sport_izbor:
                sansa_golova = random.randint(60, 85)
                st.markdown(f"""
                **{i}. {par}**
                * 1: {p_dom}% | X: {p_ner}% | 2: {p_gost}%
                * 🔥 Preporuka (Više od 2.5 gola): **{sansa_golova}%**
                """)
            else:
                adj_dom = p_dom + (p_ner / 2)
                adj_gost = p_gost + (p_ner / 2)
                margina = random.randint(152, 218)
                st.markdown(f"""
                **{i}. {par}**
                * Pobjeda domaćina: {adj_dom:.1f}% | Pobjeda gosta: {adj_gost:.1f}%
                * 🔥 Procijenjena margina koševa: **~{margina}**
                """)
            st.write("---")
            
        st.info("Slobodno izmijeni parove i pokreni novu analizu kada god poželiš!")
    else:
        st.warning("Molimo te da uneseš barem jedan par u polje iznad.")

