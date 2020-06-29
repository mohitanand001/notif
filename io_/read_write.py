class Reader:
    def __init__(self, _resource_typ):
        self._resource_typ = _resource_typ

    def read(self, path):
        pass


class Writer:
    def __init__(self, _resource_typ):
        self._resource_typ = _resource_typ

    def write(self, path):
        pass
