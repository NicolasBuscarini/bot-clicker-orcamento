import json as native_json


class JsonUtil:
    def __init__(self, path):
        self.path = path
        self.config = self.read()

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return native_json.load(f)

    def write(self):
        with open(self.path, 'w') as f:
            native_json.dump(self.config, f, indent=4)

    def get(self, key):
        try:
            return self.config[key]
        except KeyError:
            return key

    def set(self, key, value):
        self.config[key] = value
