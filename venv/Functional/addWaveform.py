import numpy as np
from pydub import AudioSegment
import json
import subprocess
import os


async def generate_waveform(mp3_file_path):
    # Чтение аудио и генерация данных для формы волны
    audio = await AudioSegment.from_mp3(mp3_file_path)
    samples = await np.array(audio.get_array_of_samples())
    samples = samples / np.max(np.abs(samples))  # Нормализация

    # Разбиение на 100 значений для формы волны
    waveform = await np.abs(samples[::len(samples) // 100]) * 100
    waveform = await waveform.astype(int).tolist()
    
    # собираем имя для ogg
    ogg_file_path = os.path.dirname(mp3_file_path) + '/' + os.path.basename(mp3_file_path)[:-3] + "ogg"
    # сохраняем прочитанный mp3 как ogg
    await audio.export(ogg_file_path, format="ogg", codec="libopus")

    # вызываем функцию вставки данных через Json и FFMPEG
    return await add_waveform_metadata(waveform, ogg_file_path)


async def add_waveform_metadata(waveform, file_path):
    # Waveform от NumPy
    metadata = {'waveform': waveform}

    # Создание временного JSON файла для метаданных
    metadata_file = "metadata.json"
    with open(metadata_file, 'w') as f:
        await json.dump(metadata, f)

    # имя для обновленного OGG
    output_file = os.path.dirname(file_path) + "/W-" + os.path.basename(file_path)
    
    # процесс добавления данных
    await subprocess.run(
        ['ffmpeg', '-i', file_path, '-c', 'copy', '-metadata', f'waveform={json.dumps(waveform)}', output_file])

    # Удаление временного JSON файла
    await os.remove(metadata_file)

    return output_file
