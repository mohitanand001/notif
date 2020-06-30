from io_.read_write import Reader

import json
import logging

logger = logging.getLogger(__name__)


class JsonReader(Reader):
    """Simple Json Reader class.
    """

    def __init__(self):
        self._inp = None

    def read(self, path: str):
        """Reads json data from `path`

        Args:
            path [str]: path to be read from.

        Returns:
            json: json output after reading.
        """

        with open(path) as f:
            try:
                logger.info(f"Reading input from {path}.")
                self._inp = json.loads(f.read())
            except EnvironmentError:
                logger.exception(f"Could not read {path}.")

        logger.info(f"Reading from {path} successful.")
        return self._inp
