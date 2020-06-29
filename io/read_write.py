class Reader:

    def __init__(self, resource_type):
        self.resource_type = resource_type

    def read(self, path):
        pass

class Writer:
    
    def __init__(self, resource_type):
        self.resource_type = resource_type

    def write(self, path):
        pass
    
