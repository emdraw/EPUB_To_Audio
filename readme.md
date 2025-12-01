# 📚 EPUB to Human-Like Audiobook (edge-tts)

Convierte cualquier archivo **.epub** en un **audiolibro en MP3** con voz **natural y humana** usando las voces neuronales de **Microsoft Edge TTS**.

Este script:

- Extrae el texto del `.epub`
- Limpia y divide en chunks seguros
- Usa **SSML** para pausas y entonación natural
- Genera audio con `edge-tts`
- Une todo en un solo `audiolibro.mp3`

---

## 🚀 Requisitos

### 1. Instalar dependencias de Python
```bash
pip install requirements.txt
```
### 2. Instalar FFmpeg
Linux (Debian/Ubuntu):

```bash
Copy code
sudo apt install ffmpeg
```

Mac (Homebrew):

```bash
Copy code
brew install ffmpeg
Windows:
```
Descarga FFmpeg desde su página oficial

Extrae y agrega la carpeta bin/ al PATH

📄 Uso
Convertir un EPUB a audio:

```bash
python epub_to_audio.py libro.epub
Cambiar nombre del archivo de salida:
```
```bash
python epub_to_audio.py libro.epub --out mi_libro.mp3
Usar otra voz:
```
```bash
 python main.py DonCatrin.epub --voice "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
```

## 🎙️ Voces recomendadas
# Idioma	Voz
Español México	es-MX-DaliaNeural, es-MX-JorgeNeural
Español España	es-ES-ElviraNeural, es-ES-AlvaroNeural
Español Neutral	es-ES-AbrilNeural
Inglés US	en-US-JennyNeural
Inglés UK	en-GB-SoniaNeural

# Listar todas las voces:

```bash
Copy code
edge-tts --list-voices
```
# 📦 Estructura del proyecto
```bash
.
├── epub_to_audio.py
├── README.md
└── temp_audio/   # se crea automáticamente
```
# ⚙️ ¿Cómo funciona?
Lee el .epub con ebooklib

Extrae el texto, lo limpia y elimina etiquetas HTML

Separa el texto en oraciones

Agrupa en chunks de ~2800 caracteres

Genera audio con edge-tts + SSML

Une todos los fragmentos en un solo MP3

# 🧩 Características de la voz (SSML)
El script usa:

prosody → velocidad y tono naturales

break → pausas entre secciones

Escapado automático para evitar errores en SSML

Puedes personalizar el estilo de voz si lo necesitas.

# 🛠 Mejoras opcionales
Si quieres, puedo generar versiones del script que:

Dividen por capítulos

Mejoran la entonación de diálogos

Añaden música de fondo

Exportan también en WAV / OGG

Tienen interfaz web

Funcionan 3× más rápido con multihilo