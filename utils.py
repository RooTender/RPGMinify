import os
import json

def get_directories(path:str):
    result = []
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            result.append(directory)

    return result

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