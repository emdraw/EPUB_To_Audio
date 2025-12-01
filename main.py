import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import os
import pyttsx3
from tqdm import tqdm
from pydub import AudioSegment
import argparse

def extract_text(epub_path):
    book = epub.read_epub(epub_path)
    text_content = []

    for item in book.get_items():
        if item.get_type() == 9:  # ITEM_DOCUMENT
            soup = BeautifulSoup(item.get_content(), "html.parser")
            for p in soup.find_all(["p", "div", "span"]):
                txt = p.get_text(strip=True)
                if txt:
                    text_content.append(txt)

    return "\n".join(text_content)

def split_into_chunks(text, max_chars=3000):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) < max_chars:
            current += " " + s
        else:
            chunks.append(current.strip())
            current = s

    if current:
        chunks.append(current.strip())

    return chunks

def tts_generate(text, outfile, rate=155, volume=1.0, voice_id=None):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    if voice_id:
        engine.setProperty("voice", voice_id)
    engine.save_to_file(text, outfile)
    engine.runAndWait()
    engine.stop()

def generate_audio(chunks, out_name, voice_id=None):
    temp_files = []

    print(f"Generando {len(chunks)} partes de audio...\n")

    for i, chunk in enumerate(tqdm(chunks, desc="Creando audio")):
        file_path = f"temp_audio/temp_{i}.wav"
        tts_generate(chunk, file_path, voice_id=voice_id)
        temp_files.append(file_path)

    print("\nUniendo en un solo MP3...")

    final_audio = AudioSegment.empty()

    for f in tqdm(temp_files, desc="Uniendo"):
        final_audio += AudioSegment.from_wav(f)

    final_audio.export(out_name, format="mp3")

    for f in temp_files:
        os.remove(f)

    print(f"\n✅ Audiolibro generado: {out_name}")

def epub_to_audio(epub_file, out_name, voice=None):
    print("Extrayendo texto...")
    text = extract_text(epub_file)

    print("Dividiendo texto...")
    chunks = split_into_chunks(text)

    print("Generando audio...")
    generate_audio(chunks, out_name, voice_id=voice)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("epub")
    parser.add_argument("--out", default="audiolibro.mp3")
    parser.add_argument("--voice", default=None)

    args = parser.parse_args()
    epub_to_audio(args.epub, args.out, args.voice)
