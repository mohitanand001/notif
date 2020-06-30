from io_.writers.json_writer import JsonWriter

import logging 
logger = logging.getLogger(__name__)


class WriterWorker:
    """Writer worker writes data into different formats as required by
        different gateways.
    """    

    def __init__(self):
        pass

    def _contract_modify(self, contract, data):
        pass

    def _writer(self, data, path):
        wrtr = JsonWriter()
        wrtr.write(path, data)

    def main_driver(self, p_data, data, path):
        if p_data is None:
            return None

        for channel in p_data["channels"]:
            for gateway in channel:
                try:
                    self._writer(data, path)
                except EnvironmentError:
                    logging.exception(
                        f"Error occurred while "
                        + "write data for {channel} - {gateway} combination."
                    )
                except Exception as e:
                    raise e
        
