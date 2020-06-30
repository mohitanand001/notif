import logging

from io_.readers.json_reader import JsonReader
from io_.writers.json_writer import JsonWriter

from preproc.preproc import Preprocess
from logger_.configure_logging import configure_logging


class Notify:

    def __init__(self, rd_path: str, wrt_path: str):
        """Simple notification writer.

        Args:
            rd_path (str): path from which input json is read.
            wrt_path (str): path to which output is written.
        """        
        self.read_path = rd_path
        self.write_path = wrt_path
        self._data = JsonReader().read(self.read_path)
        self._processed_data = self._get_processed_data(self._data.copy())

    def _get_processed_data(self, data):
        LOGGER.info(
            "Return processed data after adding information about "
            + "channels and gateways."
        )
        _processed = Preprocess()._preprocess(data)
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
            return None

        for channel in self.channels:
            for gateway in channel:
                try:
                    wrtr.write(self.write_path, self._data)
                except EnvironmentError:
                    logging.exception(
                        f"Error occurred while "
                        + "write data for {channel} - {gateway} combination."
                    )
                except Exception as e:
                    raise e


if __name__ == "__main__":
    configure_logging()
    LOGGER = logging.getLogger(__name__)

    LOGGER.info("Started sending notifications.")

    ntf = Notify("input.json", "outp.json")
    ntf._write()
