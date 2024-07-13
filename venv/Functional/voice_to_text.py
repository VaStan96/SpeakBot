import os
import requests
import time

from aiogram import types
from settings import bot, Secret

async def audio_to_text(message: types.Message, lang):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = ".\Data\\audio-" + file_id + ".mp3"
    await bot.download(file_id, file_name)

    headers = {"keyId": Secret.audio_key_id, "keySecret": Secret.audio_key_secret}
    create_url = f"https://api.speechflow.io/asr/file/v1/create?lang={lang}"
    query_url = "https://api.speechflow.io/asr/file/v1/query?taskId="
    files = {"file": open(file_name, "rb")}

    response = requests.post(create_url, headers=headers, files=files)
    if response.status_code == 200:
        create_result = response.json()
        query_url += create_result["taskId"] + "&resultType=4"
        while True:
            response = requests.get(query_url, headers=headers)

            if response.status_code == 200:
                query_result = response.json()
                if query_result["code"] == 11000:
                    if query_result["result"]:
                        result = query_result["result"].replace("\n\n", " ")
                        files.clear()
                        os.remove(file_name)
                        print(result)####################
                        return result
                    break
                elif query_result["code"] == 11001:
                    time.sleep(3)
                    continue
                else:
                    break
            else:
                break