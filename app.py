import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Načtení .env souboru
load_dotenv()

# Nastavení API klíče z prostředí
openai.api_key = os.getenv("OPENAI_API_KEY")

# Nadpis aplikace
st.title("🤖 AI Content Generator")
st.write("Vytvoř profesionální obsah pomocí AI")

# Sidebar s nastavením
st.sidebar.header("Nastavení")
content_type = st.sidebar.selectbox(
    "Typ obsahu:",
    ["Instagram post", "LinkedIn článek", "Twitter vlákno", "Email marketing", "Blog post"]
)

# Hlavní formulář
st.header(f"Vytvoř {content_type}")

topic = st.text_input("Zadej téma nebo klíčová slova:")
tone = st.selectbox("Tón obsahu:", ["Profesionální", "Přátelský", "Motivující", "Edukační"])
length = st.slider("Délka (slova):", 50, 500, 150)

if st.button("Generuj obsah", type="primary"):
    if not topic:
        st.warning("Prosím zadej téma!")
    elif not openai.api_key:
        st.error("API klíč není nastaven! Přidej ho do .env souboru.")
    else:
        with st.spinner("Generuji obsah..."):
            try:
                # Vytvoření promptu
                prompt = f"""Vytvoř {content_type} na téma: {topic}
                Tón: {tone}
                Délka: přibližně {length} slov
                
                Obsah by měl být:
                - Poutavý a atraktivní
                - Optimalizovaný pro danou platformu
                - Obsahovat relevantní hashtagy (pokud je to vhodné)
                """
                
                # Volání OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Jsi expert na tvorbu digitálního obsahu a copywriting."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                
                generated_content = response.choices[0].message.content
                
                # Zobrazení výsledku
                st.success("Obsah úspěšně vygenerován!")
                st.subheader("Tvůj nový obsah:")
                st.write(generated_content)
                
                # Možnost kopírování
                st.code(generated_content, language="markdown")
                
            except Exception as e:
                st.error(f"Chyba při generování: {str(e)}")
                st.info("Zkontroluj, zda máš správně nastavený API klíč v .env souboru.")

# Spodní informace
st.sidebar.markdown("---")
st.sidebar.info(
    """💡 Tip: Pro použití této aplikace potřebuješ OpenAI API klíč.
    
    Přidej ho do souboru .env:
    ```
    OPENAI_API_KEY=tvuj-api-klic
    ```"""
)
