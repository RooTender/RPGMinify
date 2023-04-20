import os
import json
import utils

title = 'TooManyFilesRPGM'
dependencies_maps = os.path.join('www', 'data')

if not os.path.exists(dependencies_maps):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    #exit(1)

audio_files_path = os.path.join('www', 'audio')
image_files_path = os.path.join('www', 'img')

audio_dirs = utils.get_directories(audio_files_path)
image_dirs = utils.get_directories(image_files_path)

dependencies = []
for dependency_map in os.listdir(dependencies_maps):
    with open(os.path.join(dependencies_maps, dependency_map), 'r') as file:
        json_file = file.read()
    
    for directory in audio_dirs:
        for value in utils.find_values(json_file, directory):
            data = utils.jsonify(str(value))
            data = json.loads(data.encode('utf-8'))['name'] 
            
            if data not in dependencies and data is not '':
                dependencies.append(data)

    

    