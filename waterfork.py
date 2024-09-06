from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

import soundfile as sf
import speech_recognition as sr
import os

app = Client(
    "user",
    api_id = 1234567,
    api_hash = "user_api_hash"
    )



# Команда PRINT
@app.on_message(filters.command("print", prefixes=".") & filters.me)
def print(_, msg):
    orig_text = msg.text.split(".print ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)



# Команда SPAM
@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def spam(_, msg):
    await msg.delete()
    cmd = msg.text.split()
    word = cmd[1:-1]
    joined_result = ' '.join(map(str, word))

    for i in range(int(cmd[-1])):
        await msg.reply_text(str(joined_result))
        sleep(0.02)



# Команда COPY
@app.on_message(filters.command('copy', prefixes='.') & filters.me)
async def copy(client, msg):
    await msg.delete()
    # Отримуємо повідомлення, на яке користувач відповів
    replied_message = msg.reply_to_message

    # Отримуємо ідентифікатор співрозмовника
    user_id = msg.chat.id
    
    cmd = msg.text.split()
    word = cmd[0:-1]

    for i in range(int(cmd[-1])):
        if replied_message.text:
            await client.send_message(chat_id=user_id, text=f"{replied_message.text}")
            sleep(0.02)

        elif replied_message.animation:
            await client.send_animation(chat_id=user_id, animation=replied_message.animation.file_id)
            sleep(0.02)

        elif replied_message.photo:
            await client.send_photo(chat_id=user_id, photo=replied_message.photo.file_id)
            sleep(0.02)

        elif replied_message.sticker:
            await client.send_sticker(chat_id=user_id, sticker=replied_message.sticker.file_id)
            sleep(0.02)



# Команда VOICE
@app.on_message(filters.command('voice', prefixes='.') & filters.me)
def voice(client, msg):
    # Перевіряємо, чи відповідь на голосове повідомлення
    replied_message = msg.reply_to_message
    if replied_message and replied_message.voice:
        # Отримуємо інформацію про файл
        file_info = replied_message.voice

        # Завантажуємо голосове повідомлення
        voice_path = f"temporary_{replied_message.id}.ogg"
        client.download_media(file_info, file_name=voice_path)

        # Читання файлу .ogg
        ogg_data, samplerate = sf.read(rf"D:\Python\pyrogram\accounts\waterfrog\downloads\temporary_{replied_message.id}.ogg")

        # Збережіть файл .wav
        sf.write(rf"D:\Python\pyrogram\accounts\waterfrog\downloads\temporary_{replied_message.id}.wav", ogg_data, samplerate)

        # Видалити файл .ogg
        os.remove(rf"D:\Python\pyrogram\accounts\waterfrog\downloads\temporary_{replied_message.id}.ogg")

        # Функція для розпізнавання тексту з аудіофайлу
        def transcribe_audio(file_path):
            recognizer = sr.Recognizer()
        
            with sr.AudioFile(file_path) as source:
                audio_data = recognizer.record(source)
            
            try:
                # Розпізнавання тексту
                text = recognizer.recognize_google(audio_data, language="uk-UA")
                return text
            except sr.UnknownValueError:
                return "Розпізнавання мови не вдалося"
            except sr.RequestError as e:
                return f"Помилка сервісу розпізнавання мови: {e}"

        # Щлях до вашого аудіофайлу
        audio_file_path = rf"D:\Python\pyrogram\accounts\waterfrog\downloads\temporary_{replied_message.id}.wav"
        
        # Виклик функції та виведення результату
        transcription_result = transcribe_audio(audio_file_path)
        msg.edit(f"Результат: {transcription_result}")

        # Видалити файл .ogg
        os.remove(rf"D:\Python\pyrogram\accounts\waterfrog\downloads\temporary_{replied_message.id}.wav")
    else:
        msg.reply_text("Відповідь на голосове повідомлення потрібна.")
        
app.run()