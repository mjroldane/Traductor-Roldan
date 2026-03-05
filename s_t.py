import streamlit as st
import streamlit.components.v1 as components

# Título de la pestaña en el navegador
st.set_page_config(page_title="Traductor Divertido")

# Definimos el código HTML/JS como un bloque de texto
codigo_interactivo = """
<div id="app-container" style="text-align: center; font-family: sans-serif; background: #fdfcf0; padding: 25px; border-radius: 20px; border: 4px solid #FFD700;">
    
    <h1 id="titulo" style="color: #FF4B4B;">¡Hola, mundo de los idiomas! 🌍</h1>
    
    <img id="imagen-principal" src="https://cdn-icons-png.flaticon.com/512/3050/3050525.png" alt="Gente charlando" style="width: 150px; border-radius: 20px; margin: 15px 0;">

    <p id="mensaje-guia" style="font-size: 1.2em; font-weight: bold;">¿Cómo quieres que nos saludemos hoy?</p>

    <div id="botonera" style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
        <button onclick="cambiarIdioma('es')" style="cursor:pointer; padding: 10px; border-radius: 10px; border:none; background:#eee;">Español 🇪🇸</button>
        <button onclick="cambiarIdioma('fr')" style="cursor:pointer; padding: 10px; border-radius: 10px; border:none; background:#eee;">Français 🇫🇷</button>
        <button onclick="cambiarIdioma('de')" style="cursor:pointer; padding: 10px; border-radius: 10px; border:none; background:#eee;">Deutsch 🇩🇪</button>
        <button onclick="cambiarIdioma('ru')" style="cursor:pointer; padding: 10px; border-radius: 10px; border:none; background:#eee;">Русский 🇷🇺</button>
    </div>
</div>

<script>
    const traducciones = {
        'es': { titulo: "¡Hola, mundo!", guia: "¡Qué bueno verte!", color: "#FF4B4B" },
        'fr': { titulo: "Salut tout le monde! 🥐", guia: "C'est super de vous voir !", color: "#0055A4" },
        'de': { titulo: "Hallo an alle! 🥨", guia: "Schön, dich hier zu sehen!", color: "#FFCE00" },
        'ru': { titulo: "Привет всем! 🇷🇺", guia: "Рад вас видеть!", color: "#D52B1E" }
    };

    function cambiarIdioma(lang) {
        const info = traducciones[lang];
        document.getElementById('titulo').innerText = info.titulo;
        document.getElementById('mensaje-guia').innerText = info.guia;
        document.getElementById('app-container').style.borderColor = info.color;
        document.getElementById('titulo').style.color = info.color;
    }
</script>
"""

# Renderizamos el HTML en Streamlit
components.html(codigo_interactivo, height=500)

