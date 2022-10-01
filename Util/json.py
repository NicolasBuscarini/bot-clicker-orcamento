import json

class Json :
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
        try:
            return self.config[key]
        except KeyError:
            return key

    def set(self, key, value) :
        self.config[key] = value