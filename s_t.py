import streamlit as st
import speech_recognition as sr

# 1. Configuración de la página y Estilo Visual (CSS)
st.set_page_config(page_title="Traductor Mágico", page_icon="🎙️", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff7575;
        transform: scale(1.02);
    }
    .title-text {
        text-align: center;
        color: #1E1E1E;
        font-family: 'Helvetica', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Interfaz de Usuario
st.markdown("<h1 class='title-text'>🌍 ¡Traductor de Voz Pro!</h1>", unsafe_allow_html=True)

# Imagen personalizada
try:
    st.image("personas hablando.JPEG", use_container_width=True)
except:
    st.info("💡 Consejo: Sube la imagen 'personas hablando.JPEG' para que aparezca aquí.")

st.markdown("---")

# 3. Configuración de Idiomas
idiomas = {
    "Español 🇪🇸": "es-ES",
    "Francés 🇫🇷": "fr-FR",
    "Alemán 🇩🇪": "de-DE",
    "Ruso 🇷🇺": "ru-RU"
}

col1, col2 = st.columns([1, 2])
with col1:
    seleccion = st.selectbox("Tu idioma:", list(idiomas.keys()))

with col2:
    st.write(" ") # Espaciador
    st.write(f"Seleccionaste: **{seleccion}**")

# 4. Lógica de Reconocimiento de Voz
if st.button("🎤 ¡PRESIONA PARA HABLAR!"):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        st.toast("Ajustando ruido ambiental...")
        r.adjust_for_ambient_noise(source, duration=1)
        st.warning("🎧 Escuchando ahora... ¡Di algo!")
        
        try:
            # Captura el audio
            audio = r.listen(source, timeout=5)
            # Convierte a texto
            texto = r.recognize_google(audio, language=idiomas[seleccion])
            
            # Resultado divertido
            st.success("✅ ¡Te entendí!")
            st.balloons()
            
            st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #FF4B4B; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <p style="color: gray; margin-bottom: 5px;">Dijiste:</p>
                <h2 style="margin-top: 0;">"{texto}"</h2>
            </div>
            """, unsafe_allow_html=True)
            
        except sr.UnknownValueError:
            st.error("❌ No pude entender el audio. Intenta hablar más claro o cerca del micro.")
        except sr.RequestError:
            st.error("❌ Error de conexión. Revisa tu internet.")
        except Exception as e:
            st.error(f"Hubo un problema: {e}")

st.markdown("<p style='text-align: center; color: gray; font-size: 0.8em;'>Recuerda dar permisos de micrófono en tu navegador</p>", unsafe_allow_html=True)
