import streamlit as st
import speech_recognition as sr

# Configuración de página
st.set_page_config(page_title="Traductor Divertido", page_icon="🎙️")

# Título y Estética
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌍 ¡Hablemos con el Mundo!</h1>", unsafe_allow_html=True)

# Imagen de personas hablando
try:
    st.image("personas hablando.JPEG", use_container_width=True)
except:
    st.warning("⚠️ Asegúrate de subir 'personas hablando.JPEG' a tu carpeta de GitHub.")

# Selección de idioma
idiomas = {
    "Español 🇪🇸": "es-ES",
    "Français 🇫🇷": "fr-FR",
    "Deutsch 🇩🇪": "de-DE",
    "Русский 🇷🇺": "ru-RU"
}

seleccion = st.selectbox("¿En qué idioma quieres hablar?", list(idiomas.keys()))

# Botón interactivo
if st.button(f"🚀 ¡Empezar a escuchar!"):
    r = sr.Recognizer()
    
    # Intentar usar el micrófono
    try:
        with sr.Microphone() as source:
            st.info("🎧 Te escucho... ¡Habla ahora!")
            audio = r.listen(source, timeout=5)
            
            # Procesar voz a texto
            texto = r.recognize_google(audio, language=idiomas[seleccion])
            
            # Mostrar resultado divertido
            st.success("¡Te entendí perfectamente!")
            st.balloons()
            st.markdown(f"### Lo que dijiste fue:\n> **{texto}**")
            
    except sr.RequestError:
        st.error("Error de conexión con el servicio de voz.")
    except sr.UnknownValueError:
        st.error("No logré entender el audio. ¡Inténtalo de nuevo!")
    except Exception as e:
        st.error(f"Error técnico: {e}")
        st.info("Nota: Si estás en la web, Streamlit Cloud requiere permisos de micrófono en tu navegador.")
