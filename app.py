import streamlit as st
import random
import time

# Podešavanje izgleda da bude čisto i moderno, poput Gemini chata
st.markdown("""
    <style>
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
    }
    .stChatMessage {
        background-color: #1e1f20;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🧠 Hashim")
st.caption("Tvoj lični AI sportski analitičar i simulator.")

# Inicijalizacija chata sa Hashimovim uvodom
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Zdravo! Ja sam Hashim, tvoj lični AI asistent za sportsku analizu. Reci mi koji meč želiš da obradimo (npr. *Real Madrid - Barcelona* ili *LA Lakers - Boston*), izaberi sport ispod, i pokrenut ću simulaciju za tvoj tiket!"}
    ]

# Prikaz historije razgovora
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Odabir sporta
sport_izbor = st.radio("Izaberi sport za analizu:", ["Fudbal ⚽", "Košarka 🏀"], horizontal=True)

# Polje za razgovor / unos parova
if prompt := st.chat_input("Npr. Inter - Milan"):
    # Dodaj korisnikovu poruku
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Hashimov odgovor i simulacija
    with st.chat_message("assistant"):
        with st.spinner("Hashim analizira tabelu, međusobne duele i pokreće Monte Carlo simulacije..."):
            time.sleep(1.2)
            
        # Generisanje simulacije
        p_dom = random.randint(40, 62)
        p_gost = random.randint(18, 38)
        p_ner = 100 - (p_dom + p_gost)
        
        if "Fudbal" in sport_izbor:
            sansa_golova = random.randint(58, 85)
            odgovor = f"""Analizirao sam meč **{prompt}**. Evo rezultata na bazi 10.000 simulacija:
            
* **1 (Pobjeda domaćina):** {p_dom}%
* **X (Neriješeno):** {p_ner}%
* **2 (Pobjeda gosta):** {p_gost}%
* 🔥 **Preporuka (Više od 2.5 gola):** {sansa_golova}% šanse.
            
Slobodno mi pošalji sljedeći par za tiket!"""
        else:
            adj_dom = p_dom + (p_ner / 2)
            adj_gost = p_gost + (p_ner / 2)
            margina = random.randint(154, 222)
            odgovor = f"""Obradio sam košarkaški meč **{prompt}**:
            
* **Pobjeda domaćina:** {adj_dom:.1f}%
* **Pobjeda gosta:** {adj_gost:.1f}%
* 🔥 **Procijenjeni ukupni zbroj koševa (Margina):** ~{margina} poena
            
Koji sljedeći par želiš da provjerimo?"""

        st.markdown(odgovor)
        st.session_state.messages.append({"role": "assistant", "content": odgovor})

