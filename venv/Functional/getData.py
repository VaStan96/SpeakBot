from Functional import toAI, voice_to_text, text_to_voice, addWaveform
from aiogram.types import Message, FSInputFile
from BD_func import get_element


async def get_text(message: Message):
    chatID = get_element.get_chatID(message.from_user.id)
    text = message.text

    text_AI = await toAI.request_to_AI(text, chatID)
    return text_AI

async def get_voice(message: Message):
    tLang = get_element.get_treinLang(message.from_user.id)
    chatID = get_element.get_chatID(message.from_user.id)

    user_voice_to_text = await voice_to_text.audio_to_text(message, tLang)
    text_AI = await toAI.request_to_AI(user_voice_to_text, chatID)
    path_voice = await text_to_voice.message_to_voice(text_AI, tLang)
    path_voice = await addWaveform.generate_waveform(path_voice)
    voice = FSInputFile(path_voice)
    return voice, path_voice