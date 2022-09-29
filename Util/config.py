import json

class ConfigJson :
    def __init__(self, path) :
        self.path = path
        self.config = self.read()

    def read(self) :
        with open(self.path, 'r') as f :
            return json.load(f)

    def write(self) :
        with open(self.path, 'w') as f :
            json.dump(self.config, f, indent=4)

    def get(self, key) :
        return self.config[key]

    def set(self, key, value) :
        self.config[key] = value