from flask import Flask, request, send_file
from twilio.twiml.messaging_response import MessagingResponse
import openai
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

#openai.api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = "sk-..."
character_prompt = """
You are an AI Chef named Marco. You're friendly, knowledgeable, and always respond with helpful, step-by-step cooking advice. Be enthusiastic and kind.
"""

def generate_reply(user_message):
    messages = [
        {"role": "system", "content": character_prompt},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response['choices'][0]['message']['content']

def text_to_speech(text):
    filename = f"voice_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    user_msg = request.form.get('Body')
    response_text = generate_reply(user_msg)
    audio_file = text_to_speech(response_text)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response_text)
    msg.media(request.url_root + audio_file)

    return str(resp)

@app.route("/<filename>")
def serve_audio(filename):
    return send_file(filename, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)