import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from openai import OpenAI
from gpt4all import GPT4All
from dotenv import load_dotenv

load_dotenv()

language = 'pt'
SAMPLE_RATE = 44100
RECORD_SECONDS = 5
RECORD_FILE = 'request_audio.wav'
RESPONSE_FILE = 'response_audio.mp3'

# Cliente OpenAI apenas para Whisper e TTS
client = OpenAI()

# Baixa o modelo automaticamente na primeira execução
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

def record(sec=RECORD_SECONDS):
    print(f'Ouvindo por {sec} segundos...\n')
    audio = sd.rec(int(sec * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
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

# Envia ao GPT4All (local, sem tokens)
with model.chat_session():
    response = model.generate(transcription, max_tokens=512)
print(f'Resposta: {response}\n')

# Sintetiza a resposta em voz via OpenAI TTS
tts_response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=response,
)
tts_response.stream_to_file(RESPONSE_FILE)

# Reproduz o áudio
print('Reproduzindo resposta...')
response_audio, _ = wav.read(RESPONSE_FILE)
sd.play(response_audio, samplerate=SAMPLE_RATE)
sd.wait()