# 🎙️ TTS Chat

Assistente de voz em português que grava sua fala, transcreve com Whisper, responde com GPT4All (local) e fala a resposta com a API TTS da OpenAI.

## Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/belasoaress/tts-chat.git
cd tts-chat
```

### 2. Instale as dependências

```bash
pip install openai sounddevice numpy scipy python-dotenv gpt4all
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

> Na primeira execução o modelo GPT4All (~4GB) será baixado automaticamente.

## Dependências

| Biblioteca        | Uso                                 |
| ----------------- | ----------------------------------- |
| `openai`          | Whisper (transcrição) e TTS (voz)   |
| `gpt4all`         | Chat local sem tokens (LLaMA 3)     |
| `sounddevice`     | Gravação e reprodução de áudio      |
| `numpy` / `scipy` | Processamento e salvamento do áudio |
| `python-dotenv`   | Leitura segura da API Key           |

## Observações

- O microfone grava por **5 segundos** por padrão (altere `RECORD_SECONDS` no código)
- O chat roda **100% local** com GPT4All — apenas Whisper e TTS usam a API da OpenAI
- Recomendado pelo menos **8GB de RAM** para rodar o modelo local
