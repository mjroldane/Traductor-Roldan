<div id="app-container" style="text-align: center; font-family: 'Comic Sans MS', sans-serif; background: #f0f8ff; padding: 20px; border-radius: 15px;">
    
    <h1 id="titulo">¡Hola, mundo de los idiomas! 🌍</h1>
    
    <img id="imagen-principal" src="personas hablando.JPEG" alt="Gente charlando" style="width: 300px; border-radius: 50%; border: 5px solid #ff6347; margin-bottom: 20px;">

    <p id="mensaje-guia" style="font-size: 1.2em;">¿Cómo quieres que nos saludemos hoy?</p>

    <div id="botonera">
        <button onclick="cambiarIdioma('es')">Español 🇪🇸</button>
        <button onclick="cambiarIdioma('fr')">Français 🇫🇷</button>
        <button onclick="cambiarIdioma('de')">Deutsch 🇩🇪</button>
        <button onclick="cambiarIdioma('ru')">Русский 🇷🇺</button>
    </div>
</div>

<script>
    const traducciones = {
        'es': {
            titulo: "¡Hola, mundo de los idiomas!",
            guia: "¡Qué bueno verte por aquí! ¿Hablamos?",
            color: "#ff6347"
        },
        'fr': {
            titulo: "Salut tout le monde! 🥐",
            guia: "C'est super de vous voir ici ! On discute ?",
            color: "#4682b4"
        },
        'de': {
            titulo: "Hallo an alle! 🥨",
            guia: "Schön, dich hier zu sehen! Sollen wir reden?",
            color: "#ffd700"
        },
        'ru': {
            titulo: "Привет всем! 🇷🇺",
            guia: "Рад вас видеть! Поговорим?",
            color: "#32cd32"
        }
    };

    function cambiarIdioma(lang) {
        const info = traducciones[lang];
        document.getElementById('titulo').innerText = info.titulo;
        document.getElementById('mensaje-guia').innerText = info.guia;
        
        // Cambio de color dinámico para hacerlo más divertido
        document.getElementById('app-container').style.border = `5px dashed ${info.color}`;
        document.getElementById('titulo').style.color = info.color;
    }
</script>

        
    


