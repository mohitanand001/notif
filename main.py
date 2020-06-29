from io_.readers.json_reader import JsonReader
from io_.writers.json_writer import JsonWriter

class Notify:
    """
    """

    def __init__(self, rd_path, wrt_path):
        self.read_path = rd_path
        self.write_path = wrt_path
        self._data = JsonReader().read(self.read_path)
        self._processed_data = self._get_processed_data(self._data)

    def _get_processed_data(self, data):
        
        return data

    def _get_enterprise(self):
        return self._processed_data["enterprise"]

    def _get_channels(self):
        return self._processed_data["channels"]

    @property
    def enterprise(self):
        return self._get_enterprise()

    @property
    def channels(self):
        return self._get_channels()
        

    def _write(self):
        wrtr = JsonWriter()
        for channel in self.channels:
            for gateway in channel:
                try:
                    wrtr.write(self.write_path, self._processed_data)
                except IOError as e:
                    print(e)
                except Exception as e:
                    raise e
    


ntf = Notify("input.json", "outp.json")
ntf._write()
