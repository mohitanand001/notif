"""Modules that configures the logger.
"""

import logging.config
import os
import json


def configure_logging_util(config_file_path: str):
    """Configures the logging module.

    Configures the logging module using the json file present in
    `config_file_path`.

    Args:
        config_file_path (str): The path for file containing the configuration.
    """

    with open(config_file_path, "r") as logging_json_config_f:
        try:
            logging_config = json.load(logging_json_config_f)
            logging.config.dictConfig(logging_config)
        except EnvironmentError:
            logging.critical("Unable to load configurations.")


def configure_logging():
    """ Configure the logging module using `configure_logging_util` function"""
    config_file_path = "logger_/logger_conf.json"

    configure_logging_util(config_file_path)
    logging.info("Finish configuring logger")
