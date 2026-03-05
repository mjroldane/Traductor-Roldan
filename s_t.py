import streamlit as st
import speech_recognition as sr
from googletrans import Translator

# Configuración estética
st.set_page_config(page_title="Traductor Mágico", page_icon="🎙️")

# Estilo personalizado para que sea más divertido
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { 
        border-radius: 50px; 
        background-color: #ff4b4b; 
        color: white; 
        font-size: 20px;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 ¡El Traductor Divertido!")

# Mostrar la imagen que pediste
try:
    st.image("personas hablando.JPEG", use_column_width=True)
except:
    st.info("📸 Sube la imagen 'personas hablando.JPEG' a tu repo para verla aquí.")

# Diccionario de idiomas
idiomas = {
    "Español 🇪🇸": "es",
    "Francés 🇫🇷": "fr",
    "Alemán 🇩🇪": "de",
    "Ruso 🇷🇺": "ru"
}

seleccion = st.selectbox("¿En qué idioma me vas a hablar?", list(idiomas.keys()))

if st.button("🎤 ¡PRESIONA Y HABLA!"):
    r = sr.Recognizer()
    translator = Translator()
    
    with sr.Microphone() as source:
        st.write("### 🎧 Escuchando... ¡di algo genial!")
        audio = r.listen(source)
        
        try:
            # Reconocer voz
            texto_original = r.recognize_google(audio, language=idiomas[seleccion])
            st.success(f"**Escuché:** {texto_original}")
            
            # Efecto divertido
            st.balloons()
            
            # Mostrar traducción (ejemplo a Inglés por diversión)
            traduccion = translator.translate(texto_original, dest='en')
            st.info(f"**En Inglés sería:** {traduccion.text} 🇺🇸")
            
        except Exception as e:
            st.error("¡Ups! Mi radar no captó nada. ¿Podrías repetirlo?")
