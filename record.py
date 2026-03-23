import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
language = 'pt'

SAMPLE_RATE = 44100
RECORD_SECONDS = 5
RECORD_FILE = 'request_audio.wav'
RESPONSE_FILE = 'response_audio.mp3'

client = OpenAI()

def record(sec=RECORD_SECONDS):
    print(f'Ouvindo por {sec} segundos...\n')
    audio = sd.rec(int(sec * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()  # Aguarda a gravação terminar
    wav.write(RECORD_FILE, SAMPLE_RATE, audio)
    print('Gravação concluída!\n')
    return RECORD_FILE

# Grava o áudio
record_file = record()

# Transcreve via Whisper API
with open(record_file, 'rb') as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language=language,
    ).text
print(f'Transcrição: {transcription}\n')

# Envia ao ChatGPT
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": transcription}]
)
chatgpt_response = response.choices[0].message.content
print(f'Resposta: {chatgpt_response}\n')

# Sintetiza a resposta em voz
tts_response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=chatgpt_response,
)
tts_response.stream_to_file(RESPONSE_FILE)

# Reproduz o áudio da resposta
print('Reproduzindo resposta...')
response_audio, _ = wav.read(RESPONSE_FILE)  # Lê para reprodução
sd.play(response_audio, samplerate=SAMPLE_RATE)
sd.wait()