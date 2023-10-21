import json

def dict_has_keys(dct: dict,  keys: [str]) -> bool:
    return  any(key in keys for key in dct)


def load_json_content(json_file_path: str) -> [dict]:
    with open(json_file_path) as json_file:
        data =  json.loads(json_file.read())

        return data
