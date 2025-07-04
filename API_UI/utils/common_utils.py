import os
import json

def load_json(path:str ,file_name: str) -> dict:
    with open(f"{path}{file_name}.json", "r") as f:
        body = json.load(f)

    mi_dict = {item["id"]: item for item in body}
    return mi_dict

def save_json(path:str ,file_name: str, content: dict):
    with open(f"{path}{file_name}.json", "w") as f:
        json.dump(content, f, indent=2)

def set_type(entity_type: int) -> str:
    if entity_type == 2:
        return "elements"
    elif entity_type == 3:
        return "devices"
    else:
        return "elements"