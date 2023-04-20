import json

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