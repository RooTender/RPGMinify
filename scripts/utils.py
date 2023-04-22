import os
import math
import json


def get_files(path: str):
    result = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            result.extend(get_files(file_path))
        else:
            result.append(file_path)

    return result


def get_filename(path: dict):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]


def jsonify(data: str):
    return str(data.replace('\'', '"'))


def find_values(data: str, property: str):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[property])
        except KeyError:
            pass
        return a_dict

    json.loads(data, object_hook=_decode_dict)
    return results


def get_game_size():
    total_size = 0
    for dirpath, _, filenames in os.walk('.'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def print_with_unit(size):
    unit = ['B', 'KB', 'MB', 'GB']

    exponent = 0
    while (math.floor(size / 1024) > 0):
        size /= 1024
        exponent += 1

    return '{size}{unit}'.format(size=round(size, 2), unit=unit[exponent])
