import logging

from io_.readers.json_reader import JsonReader
from io_.writers.json_writer import JsonWriter

from preproc.preproc_main import PreprocessMain
from logger_.configure_logging import configure_logging

from io_.writer_workers.write_workers_main import WriterWorker


class Notify:
    def __init__(self, rd_path: str, wrt_path: str):
        """Reads input data and preprocesses it.

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
        try:
            _processed = PreprocessMain()._preprocess_worker_main(data)
        except Exception as e:
            LOGGER.exception(
                "Could not preprocess data."
            )
            raise e

        return _processed

    def _writer_worker(self):
        LOGGER.info(f"Writing data begin")
        WriterWorker().main_driver(self._processed_data, self._data, self.write_path)
        LOGGER.info(f"Writing data complete.")



if __name__ == "__main__":
    configure_logging()
    LOGGER = logging.getLogger(__name__)

    LOGGER.info("Started sending notifications.")

    ntf = Notify("input.json", "outp.json")
    ntf._writer_worker()
