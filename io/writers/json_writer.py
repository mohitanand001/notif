from io.read_write import Writer

class JsonWriter(Writer):
    def __init__(self):
        self._inp = None

    def read(self, path):
        with open(path) as f:
            self._inp = json.loads(f)
        return self._inp
            

    


