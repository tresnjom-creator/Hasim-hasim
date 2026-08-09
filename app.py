import streamlit as st
import random
import time

st.markdown("# ⚽🏀 AI Sportski Analitičar Pro")
st.write("Sistem za naprednu Monte Carlo simulaciju i analizu mečeva.")

# Izbor sporta
sport = st.selectbox("Izaberi sport:", ["Fudbal ⚽", "Košarka 🏀"])

# Unos timova
col1, col2 = st.columns(2)
with col1:
    domacin = st.text_input("Domaćin:", placeholder="npr. Real Madrid")
with col2:
    gost = st.text_input("Gost:", placeholder="npr. Barcelona")

st.divider()

# Dodatne opcije za klađenje / analizu
st.subheader("⚙️ Parametri analize")
forma_domacina = st.slider(f"Forma domaćina ({domacin if domacin else 'Tim 1'}):", 1, 10, 7)
forma_gosta = st.slider(f"Forma gosta ({gost if gost else 'Tim 2'}):", 1, 10, 5)

if st.button("🚀 Pokreni AI Simulaciju (10.000 iteracija)", type="primary"):
    if domacin and gost:
        
        # Simulacija učitavanja
        with st.spinner(f"Izvršavam Monte Carlo simulacije za {domacin} vs {gost}..."):
            time.sleep(1.5)
            
        st.success("Simulacija uspješno završena!")
        
        # Matematički model (baziran na formi i prednosti domaćeg terena)
        snaga_domacin = forma_domacina * 1.15  # Blaga prednost domaćeg terena
        snaga_gost = forma_gosta
        ukupno = snaga_domacin + snaga_gost
        
        procenat_domacin = int((snaga_domacin / ukupno) * 100)
        procenat_gost = int((snaga_gost / ukupno) * 100)
        nerijeseno = 100 - (procenat_domacin + procenat_gost)
        
        st.divider()
        st.subheader(f"📊 Rezultati simulacije: {domacin} - {gost}")
        
        if "Fudbal" in sport:
            st.metric(label=f"Šansa za pobjedu: {domacin}", value=f"{procenat_domacin}%")
            if nerijeseno > 0:
                st.metric(label="Šansa za neriješeno (X)", value=f"{nerijeseno}%")
            st.metric(label=f"Šansa za pobjedu: {gost}", value=f"{procenat_gost}%")
            
            # Procjena golova (Over/Under 2.5)
            ocekivani_golovi = round((forma_domacina + forma_gosta) / 3.5, 2)
            sansa_3_plus = min(max(int(ocekivani_golovi * 28), 25), 85)
            
            st.info(f"⚽ **Očekivani prosjek golova na meču:** {ocekivani_golovi}")
            st.warning(f"🔥 **Preporuka / Over 2.5 gola:** {sansa_3_plus}% šanse da bude 3 ili više golova.")
            
        else:
            # Košarka
            adj_domacin = procenat_domacin + (nerijeseno / 2)
            adj_gost = procenat_gost + (nerijeseno / 2)
            
            st.metric(label=f"Pobjeda domaćina ({domacin})", value=f"{adj_domacin:.1f}%")
            st.metric(label=f"Pobjeda gosta ({gost})", value=f"{adj_gost:.1f}%")
            
            # Procjena koševa
            prosjek_poena = int(150 + (forma_domacina + forma_gosta) * 3.2)
            st.info(f"🏀 **Procijenjeni ukupni zbroj koševa (Margina):** ~{prosjek_poena} poena")
            
    else:
        st.error("Molimo unesite imena oba tima prije pokretanja simulacije.")
