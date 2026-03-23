# 🎙️ TTS Chat

Assistente de voz em português que grava sua fala, transcreve com Whisper, responde com GPT-4 e fala a resposta com a API TTS da OpenAI.

## Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/tts-chat.git
cd tts-chat
```

### 2. Instale as dependências

```bash
pip install openai sounddevice numpy scipy python-dotenv
```

### 3. Configure a API Key

Copie o arquivo de exemplo e adicione sua chave:

```bash
cp .env.example .env
```

Edite o `.env` com sua chave da OpenAI: https://platform.openai.com/account/api-keys

### 4. Execute

```bash
python record.py
```

## Dependências

| Biblioteca        | Uso                                            |
| ----------------- | ---------------------------------------------- |
| `openai`          | Whisper (transcrição), GPT-4 (chat), TTS (voz) |
| `sounddevice`     | Gravação e reprodução de áudio                 |
| `numpy` / `scipy` | Processamento e salvamento do áudio            |
| `python-dotenv`   | Leitura segura da API Key                      |

## Observações

- O microfone grava por **5 segundos** por padrão (altere `RECORD_SECONDS` no código)
- É necessário saldo na conta OpenAI para usar as APIs
