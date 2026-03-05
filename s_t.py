import streamlit as st
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

# Configuración visual divertida
st.set_page_config(page_title="Traductor Mágico", page_icon="🗣️")

st.title("¡Hablemos con el Mundo! 🌍")
st.image("personas hablando.JPEG", caption="¡Dime algo y lo escribiré!")

# Diccionario de idiomas para el reconocimiento
idiomas = {
    "Español 🇪🇸": "es-ES",
    "Français 🇫🇷": "fr-FR",
    "Deutsch 🇩🇪": "de-DE",
    "Русский 🇷🇺": "ru-RU"
}

# Selección de idioma con un tono amigable
seleccion = st.selectbox("¿En qué idioma vas a hablarme hoy?", list(idiomas.keys()))
lang_code = idiomas[seleccion]

if st.button(f"🚀 ¡Empezar a escuchar en {seleccion}!"):
    r = Recognizer()
    with Microphone() as source:
        st.write("### 🎧 Escuchando... ¡Dilo con ganas!")
        # Ajuste para ruido ambiental
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            # Traduciendo voz a texto
            texto_detectado = r.recognize_google(audio, language=lang_code)
            
            # Interfaz divertida para mostrar el resultado
            st.success(f"**Lo que entendí fue:**")
            st.balloons() # ¡Efecto divertido de globos!
            st.markdown(f"> # {texto_detectado}")
            
        except UnknownValueError:
            st.error("¡Ups! No logré entender lo que dijiste. ¿Podrías repetirlo más claro?")
        except RequestError:
            st.warning("Parece que tengo problemas de conexión. Verifica tu internet.")

# Estilo extra con CSS para que se vea más colorido
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_config=True)
