from gtts import gTTS
import datetime


async def message_to_voice(message, lang):
    tts = gTTS(text=message, lang=lang)
    uniqName = str(datetime.datetime.now().time()).replace(":", ".")
    file_name = ".\Data\\" + lang + "-" + uniqName +".mp3"
    tts.save(file_name)

    return file_name
