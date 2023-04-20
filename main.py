import os
import json
import utils

title = 'TooManyFilesRPGM'
maps_path = os.path.join('www', 'data')

if not os.path.exists(maps_path):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    #exit(1)

audio_files_path = os.path.join('www', 'audio')
image_files_path = os.path.join('www', 'img')

audio_files = utils.get_files(audio_files_path)
image_files = utils.get_files(image_files_path)

audio_obsoletes = []
image_obsoletes = []

for map in os.listdir(maps_path):
    with open(os.path.join(maps_path, map), 'r') as file:
        map_data = file.read()
    
    for file in audio_files:
        if not utils.get_filename(file) in map_data and file not in audio_obsoletes:
            audio_obsoletes.append(file)

    for file in image_files:
        if not utils.get_filename(file) in map_data and file not in image_files:
            image_obsoletes.append(file)


print(audio_obsoletes)
#print(audio_obsoletes)