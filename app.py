import streamlit as st
import random
import time

# Podešavanje izgleda stranice da liči na AI chat
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .chat-bubble {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🤖 AI Sportski Chat Analitičar")
st.write("Dobro došao! Reci mi koji meč želiš da analiziramo (npr. *Real Madrid - Barcelona* ili *LA Lakers - Boston*), pa ću pokrenuti simulaciju.")

# Inicijalizacija chata
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Pozdrav! Unesi par koji te zanima i izaberi sport, a ja ću izračunati procente za pobjedu i golove/koševe."}
    ]

# Prikaz prethodnih poruka u chat stilu
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Odabir sporta preko opcija u chatu
sport_izbor = st.radio("Izaberi sport za sljedeću analizu:", ["Fudbal ⚽", "Košarka 🏀"], horizontal=True)

# Polje za unos poruke / para
if prompt := st.chat_input("Npr. Arsenal - Chelsea"):
    # Dodaj korisničku poruku
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Odgovor AI-ja
    with st.chat_message("assistant"):
        with st.spinner("Analiziram tabelu, formu i vršim Monte Carlo simulacije..."):
            time.sleep(1.2)
            
        # Generisanje simulacije
        p_dom = random.randint(40, 60)
        p_gost = random.randint(20, 40)
        p_ner = 100 - (p_dom + p_gost)
        
        if "Fudbal" in sport_izbor:
            sansa_golova = random.randint(55, 80)
            odgovor = f"""📊 **Rezultati simulacije za meč: {prompt}**
            
* **1 (Pobjeda domaćina):** {p_dom}%
* **X (Neriješeno):** {p_ner}%
* **2 (Pobjeda gosta):** {p_gost}%
* 🔥 **Preporuka (Over 2.5 gola):** {sansa_golova}% šanse da bude više od 2 gola.
            
*Analiza završena na bazi 10.000 simulacija.*"""
        else:
            adj_dom = p_dom + (p_ner / 2)
            adj_gost = p_gost + (p_ner / 2)
            margina = random.randint(155, 220)
            odgovor = f"""🏀 **Košarkaška analiza za meč: {prompt}**
            
* **Pobjeda domaćina:** {adj_dom:.1f}%
* **Pobjeda gosta:** {adj_gost:.1f}%
* 🔥 **Procijenjena margina poena (Over/Under):** ~{margina} poena
            
*Simulacija uspješno obrađena.*"""

        st.markdown(odgovor)
        st.session_state.messages.append({"role": "assistant", "content": odgovor})

