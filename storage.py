from datetime import datetime
import json
from config import LOG_MSG


def log_data(msg, filename):
    """
    this function tracks errors and transaction and logs it when it happens
    :param msg: this is the string message that is being logged
    :param filename: this is the text file where the message is logged
    """
    with open(filename, mode="a", encoding="utf-8") as log_writer:
        log_writer.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {msg}\n")


def load_data(filename):
    """
    this function deserializes our json data into python object for usage
    :param filename: json file/document
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file_reader:
            return json.load(file_reader)
    except Exception as e:
        log_data(str(e), LOG_MSG)
        return []


def save_data(data, filename):
    """
    this function updates every change made in our data object and saves/writes it
    to our json file for serialization
    :param data: our updated python object e.g. list/dictionary
    :param filename: json file/document
    """
    with open(filename, mode="w", encoding="utf-8") as file_writer:
        json.dump(data, file_writer, indent=4)
