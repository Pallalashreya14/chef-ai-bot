# Chef AI WhatsApp Bot 🍳📱

This is a Python-based WhatsApp bot featuring a chef AI character that responds with both text and voice.

## 🔧 Setup Instructions

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Replace `YOUR_OPENAI_API_KEY` in `chef_whatsapp_bot.py` with your OpenAI API key.

3. Start the Flask server:

```bash
python chef_whatsapp_bot.py
```

4. Use [ngrok](https://ngrok.com/) to expose the app:

```bash
ngrok http 5000
```

5. Set the ngrok HTTPS URL as the webhook in your Twilio WhatsApp sandbox.

## 🗣️ Features

- User sends text to WhatsApp
- AI Chef replies in text **and** voice using gTTS
- Extendable to voice input (Whisper support can be added)

Enjoy your delicious coding! 🍝