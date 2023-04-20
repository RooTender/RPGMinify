import copy
import os
import re
import utils

title = 'TooManyFilesRPGM'
maps_path = os.path.join('www', 'data')

if not os.path.exists(maps_path):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    #exit(1)

audio_files_path = os.path.join('www', 'audio')
image_files_path = os.path.join('www', 'img')

audio_obsoletes = utils.get_files(audio_files_path)
image_obsoletes = utils.get_files(image_files_path)

for map in os.listdir(maps_path):
    with open(os.path.join(maps_path, map), 'r') as file:
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

for script in scripts:
    with open(script, 'r', encoding="utf8") as file:
        script_data = file.read();

    files = copy.copy(audio_obsoletes)
    for file in files:
        if re.search("(?<![a-zA-Z\d]){}(?![a-zA-Z\d])".format(utils.get_filename(file)), script_data):
            audio_obsoletes.remove(file)

    files = copy.copy(image_obsoletes)
    for file in files:
        if re.search("(?<![a-zA-Z\d]){}(?![a-zA-Z\d])".format(utils.get_filename(file)), script_data):
            image_obsoletes.remove(file)

obsoletes = audio_obsoletes + image_obsoletes
for obsolete in obsoletes:
    os.remove(obsolete)