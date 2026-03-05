import streamlit as st
import speech_recognition as sr

# Configuración de la página
st.set_page_config(page_title="Traductor Mágico", page_icon="🎙️")

# Estilo divertido para la interfaz
st.markdown("""
    <style>
    .main { background-color: #fdfcf0; }
    h1 { color: #FF4B4B; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 ¡Hablemos con el Mundo!")

# Imagen personalizada (Asegúrate de que el nombre coincida con tu archivo en GitHub)
try:
    st.image("personas hablando.jpg", use_container_width=True)
except:
    st.image("personas hablando.jpg", use_column_width=True) # Versión para Streamlit más antiguo

# Selección de idiomas
idiomas = {
    "Español 🇪🇸": "es-ES",
    "Francés 🇫🇷": "fr-FR",
    "Alemán 🇩🇪": "de-DE",
    "Ruso 🇷🇺": "ru-RU"
}

seleccion = st.selectbox("¿En qué idioma vas a hablar?", list(idiomas.keys()))

if st.button("🎤 Haz clic para empezar a hablar"):
    r = sr.Recognizer()
    # Nota: sr.Microphone() suele fallar en la nube (Streamlit Cloud) 
    # porque el servidor no tiene tu micrófono físico.
    try:
        with sr.Microphone() as source:
            st.info("Escuchando... di algo.")
            audio = r.listen(source, timeout=5)
            texto = r.recognize_google(audio, language=idiomas[seleccion])
            st.success(f"**Dijiste:** {texto}")
            st.balloons()
    except Exception as e:
        st.error("El micrófono no está disponible en este servidor.")
        st.info("Para probar el reconocimiento de voz de verdad, ejecuta este código localmente en tu computadora.")
