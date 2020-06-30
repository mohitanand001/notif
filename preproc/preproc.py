from io_.readers.json_reader import JsonReader


class Preprocess:
    """Simple preprocessing functionalities.
    """    
    def __init__(self):
        pass

    def _preprocess(self, data, config_path="./config_/configs.json"):
        _enterprise_id = str(data["enterprise_id"])
        _status = data["status"]

        try:
            print(_enterprise_id)
            _processed = JsonReader().read(config_path)[_enterprise_id]
        except KeyError as e:
            return None

        if _status not in _processed["status"]:
            return None

        print(_processed)

        data["channels"] = _processed["channels"]
        return data
