import copy
import os
import re
import utils
from tqdm import tqdm

title = 'RPGMinify'
maps_path = os.path.join('www', 'data')

if not os.path.exists(maps_path):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    exit(1)
else:
    print('Game files found!')

print('Removing unused files...')

audio_files_path = os.path.join('www', 'audio')
image_files_path = os.path.join('www', 'img')

audio_obsoletes = utils.get_files(audio_files_path)
image_obsoletes = utils.get_files(image_files_path)

for map in tqdm(os.listdir(maps_path), desc="Game assets dependencies"):
    with open(os.path.join(maps_path, map), 'r', encoding='latin-1') as file:
        map_data = file.read()
        file_path = os.path.join(maps_path, map)

    previous_audio_obsoletes = copy.copy(audio_obsoletes)
    previous_image_obsoletes = copy.copy(image_obsoletes)
    pattern = '"{}"'

    for audio in previous_audio_obsoletes:
        filename = utils.get_filename(audio)
        if pattern.format(filename) in map_data:
            audio_obsoletes.remove(audio)

    for image in previous_image_obsoletes:
        filename = utils.get_filename(image)
        if pattern.format(filename) in map_data:
            image_obsoletes.remove(image)

scripts_path = os.path.join('www', 'js')
scripts = utils.get_files(scripts_path)

for script in tqdm(scripts, desc="Engine & plugin dependencies"):
    with open(script, 'r', encoding='latin-1') as file:
        script_data = file.read()

    previous_audio_obsoletes = copy.copy(audio_obsoletes)
    previous_image_obsoletes = copy.copy(image_obsoletes)
    pattern = r"(?<![a-zA-Z\d]){}(?![a-zA-Z\d])"

    for audio in previous_audio_obsoletes:
        filename = utils.get_filename(audio)
        if re.search(pattern.format(filename), script_data):
            audio_obsoletes.remove(audio)

    for image in previous_image_obsoletes:
        filename = utils.get_filename(image)
        if re.search(pattern.format(filename), script_data):
            image_obsoletes.remove(image)

previous_size = utils.get_game_size()

obsoletes = audio_obsoletes + image_obsoletes
for obsolete in tqdm(obsoletes, desc="Removing unused files"):
    os.remove(obsolete)

if previous_size == 0:
    previous_size = 1

current_size = utils.get_game_size()
saved_space = round((1 - current_size / previous_size) * 100)

print("\nReduced space by about {}% ({} => {})".format(
    saved_space,
    utils.print_with_unit(previous_size),
    utils.print_with_unit(current_size)
))
