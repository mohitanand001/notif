from io_.read_write import Writer

import json


class JsonWriter(Writer):
    def __init__(self):
        pass

    def write(self, path, data: dict):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)        

        