from io_.read_write import Writer

import json
import logging

logger = logging.getLogger(__name__)


class JsonWriter(Writer):
    """Simple Json writer
    """

    def __init__(self):
        pass

    def write(self, path: str, data: dict):
        """Writes json data to path.

        Args:
            path (str): path to be written output to.
            data (dict): data in the form of dictionary.
        """
        with open(path, "a", encoding="utf-8") as f:
            try:
                logging.info(f"Writing data to {path}.")
                json.dump(data, f, indent=4)
            except EnvironmentError:
                logging.exception(f"Exception occurred while wrting data")

        logging.info(f"Writing data to {path} successful.")
