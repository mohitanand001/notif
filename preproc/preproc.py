"""Preprocessing utilities
"""

from io_.readers.json_reader import JsonReader


def _preprocess(data: dict, config_path="./config_/configs.json"):
    """preprocess data to attach values like channels and gateway to it.

    Args:
        data (dict): input data
        config_path (str, optional): config_file path where config
        for each enterprise channel and gateway is kept.
         Defaults to "./config_/configs.json".

    Returns:
        dict: data with additional information.
    """
    _enterprise_id = str(data["enterprise_id"])
    _status = data["status"]

    try:
        print(_enterprise_id)
        _processed = JsonReader().read(config_path)[_enterprise_id]
    except KeyError:
        return None

    if _status not in _processed["status"]:
        return None

    print(_processed)

    data["channels"] = _processed["channels"]
    return data
