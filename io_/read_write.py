class Reader:
    """Simple reader class which is extended by 
        JsonReader/TextReader/CSVReader 
    """

    def __init__(self, _resource_typ):
        self._resource_typ = _resource_typ

    def read(self, path):
        pass


class Writer:
    """Simple writer class extended by JSONWriter/
        TextWriter/CSVWriter.
    """

    def __init__(self, _resource_typ):
        self._resource_typ = _resource_typ

    def write(self, path):
        pass
