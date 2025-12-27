# 🤖 AI Content Generator

Streamlit aplikace pro generování profesionálního obsahu pomocí OpenAI API.

## ✨ Funkce

- **Více typů obsahu**: Instagram posty, LinkedIn články, Twitter vlákna, Email marketing, Blog posty
- **Přizpůsobitelný tón**: Profesionální, Přátelský, Motivující, Edukační
- **Nastavení délky**: Kontroluj počet slov (50-500)
- **Jednoduché rozhraní**: Intuitivní UI postaveno na Streamlit

## 🚀 Instalace

### 1. Klonování repozitáře

```bash
git clone https://github.com/pangro-droid/ai-content-generator.git
cd ai-content-generator
```

### 2. Instalace závislostí

```bash
pip install -r requirements.txt
```

### 3. Nastavení API klíče

Vytvoř soubor `.env` v kořenovém adresáři a přidej svůj OpenAI API klíč:

```
OPENAI_API_KEY=sk-your-api-key-here
```

**Kde získat API klíč:**
1. Jdi na https://platform.openai.com/api-keys
2. Přihlaste se nebo vytvoř účet
3. Klikni na "Create new secret key"
4. Zkopíruj klíč a vlož ho do `.env` souboru

### 4. Spuštění aplikace

```bash
streamlit run app.py
```

Aplikace se otevře v prohlížeči na `http://localhost:8501`

## 💻 Použití

1. **Vyber typ obsahu** v postraním menu
2. **Zadej téma** nebo klíčová slova
3. **Zvol tón** obsahu
4. **Nastav délku** textu
5. **Klikni na "Generuj obsah"**
6. **Zkopíruj výsledek** a použij ho!

## 💰 Náklady

Aplikace využívá GPT-3.5-turbo model:
- Cena: ~$0.002 za 1000 tokenů
- Typický požadavek: ~500-1000 tokenů
- Cena za generování: ~$0.001-0.002 (0.02-0.05 Kč)

## 🛠️ Technologie

- **Streamlit**: Web framework pro Python
- **OpenAI API**: AI model pro generování textu  
- **Python-dotenv**: Správa prostředí

## 📝 Struktura projektu

```
ai-content-generator/
├── app.py              # Hlavní aplikace
├── requirements.txt   # Závislosti
├── .env               # API klíč (vytvoř ručně)
└── README.md          # Dokumentace
```

## 👥 Pro freelancery

Tento projekt je perfektní příklad do portfolia:

1. **Přidej na GitHub** - Už hotovo! ✅
2. **Nasdílej na LinkedIn** - Ukaž své schopnosti
3. **Přidej do portfolia** - Odkaz: https://github.com/pangro-droid/ai-content-generator
4. **Ukázka skillů**: Python, AI, Streamlit, Git

## ⚠️ Bezpečnost

- **NIKDY** nesdilej svůj API klíč
- `.env` soubor je v `.gitignore` (nebude nahraný na GitHub)
- Pravidelně kontroluj použití na https://platform.openai.com/usage

## 💬 Podpora

Pokud máš otázky nebo problémy, otevři issue na GitHubu.

## 📝 Licence

Tento projekt je open source a volně k dispozici pro všechny.

---

**Happy Content Creating! 🎉**
