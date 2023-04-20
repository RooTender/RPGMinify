import os
import json

def get_files(path:str):
    result = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            result.extend(get_files(file_path))
        else:
            result.append(file_path)

    return result

def get_filename(path:dict):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]

def jsonify(data:str):
    return str(data.replace('\'', '"'))

def find_values(data:str, property:str):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[property])
        except KeyError:
            pass
        return a_dict

    json.loads(data, object_hook=_decode_dict) # Return value ignored.
    return results