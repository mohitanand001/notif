from io_.readers.json_reader import JsonReader
from io_.writers.json_writer import JsonWriter

from preproc.preproc import Preprocess


class Notify:
    """
    """

    def __init__(self, rd_path, wrt_path):
        self.read_path = rd_path
        self.write_path = wrt_path
        self._data = JsonReader().read(self.read_path)
        self._processed_data = self._get_processed_data(self._data.copy())

    def _get_processed_data(self, data):
        _processed = Preprocess()._preprocess(data)
        print(_processed)
        return _processed

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

        if self._processed_data is None:
            return

        for channel in self.channels:
            for gateway in channel:
                try:
                    wrtr.write(self.write_path, self._data)
                except IOError as e:
                    print(e)
                except Exception as e:
                    raise e


ntf = Notify("input.json", "outp.json")
ntf._write()
