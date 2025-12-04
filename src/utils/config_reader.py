import json
import os

def load_config():
    config_path = os.path.join("config","config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, "r") as file:
        config = json.load(file)

    return config