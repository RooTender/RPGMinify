import copy
import os
import re
import utils
from tqdm import tqdm

title = 'TooManyFilesRPGM'
maps_path = os.path.join('www', 'data')

if not os.path.exists(maps_path):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    exit(1)

audio_files_path = os.path.join('www', 'audio')
image_files_path = os.path.join('www', 'img')

audio_obsoletes = utils.get_files(audio_files_path)
image_obsoletes = utils.get_files(image_files_path)

for map in tqdm(os.listdir(maps_path), desc="Game assets dependencies"):
    with open(os.path.join(maps_path, map), 'r', encoding='latin-1') as file:
        map_data = file.read()

    files = copy.copy(audio_obsoletes)
    for file in files:
        if '"{}"'.format(utils.get_filename(file)) in map_data:
            audio_obsoletes.remove(file)
    
    files = copy.copy(image_obsoletes)
    for file in files:
        if '"{}"'.format(utils.get_filename(file)) in map_data:
            image_obsoletes.remove(file)

scripts_path = os.path.join('www', 'js')
scripts = utils.get_files(scripts_path)

for script in tqdm(scripts, desc="Engine & plugin dependencies"):
    with open(script, 'r', encoding='latin-1') as file:
        script_data = file.read();

    files = copy.copy(audio_obsoletes)
    for file in files:
        if re.search("(?<![a-zA-Z\d]){}(?![a-zA-Z\d])".format(utils.get_filename(file)), script_data):
            audio_obsoletes.remove(file)

    files = copy.copy(image_obsoletes)
    for file in files:
        if re.search("(?<![a-zA-Z\d]){}(?![a-zA-Z\d])".format(utils.get_filename(file)), script_data):
            image_obsoletes.remove(file)

previous_size = utils.get_game_size()

obsoletes = audio_obsoletes + image_obsoletes
for obsolete in tqdm(obsoletes, desc="Removing unused files"):
    os.remove(obsolete)

if previous_size == 0:
    previous_size = 1

current_size = utils.get_game_size()
saved_space = round((1 - current_size / previous_size) * 100) 

print("\nReduced space by about {}% ({} => {})".format(saved_space, utils.print_with_unit(previous_size), utils.print_with_unit(current_size)))