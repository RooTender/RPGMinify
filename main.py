import os

title = 'TooManyFilesRPGM'

if not os.path.exists(os.path.join('www', 'data')):
    print('Please run {title} in the folder with Game.exe'.format(title=title))
    exit(1)

