import os
import json
import utils

title = 'TooManyFilesRPGM'
dependencies_maps = os.path.join('www', 'data')

if not os.path.exists(dependencies_maps):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    #exit(1)

for dependency_map in os.listdir(dependencies_maps):
    with open(os.path.join(dependencies_maps, dependency_map), 'r') as file:
        data = file.read()
        
    print(utils.find_values(data, 'bgm'))

    break