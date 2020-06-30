from preproc.preproc import _preprocess
from preproc.validate import _validate_args, _validate_bounds

import logging

logger = logging.getLogger(__name__)


class PreprocessMain:
    def __init__(self):
        pass

    def _preprocess_worker(self, data):
        try:
            _validate_args(data)
            _validate_bounds(data)
        except ValueError:
            logger.exception(f"Invalid argument type(s)")
        processed_data = _preprocess(data)

        return processed_data

    def _preprocess_worker_main(self, data):
        return self._preprocess_worker(data)




