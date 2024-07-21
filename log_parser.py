import re
from typing import List, Dict, Pattern
from pathlib import Path

# pattern for log lines in the format: "2021-01-01 12:00:00 INFO Message"
log_format_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
                                r'(?P<level>\w+) '
                                r'(?P<message>.*)')


def parse_log_line(line: str, log_pattern: Pattern[str] = log_format_pattern) -> dict:
    """
    Parses a log line and returns a dictionary with the timestamp, level, and message
    :arg line: log line to parse
    :arg log_pattern: compiled regular expression pattern for log lines
    :return: dictionary with the timestamp, level, and message
    :err return: empty dictionary if the line does not match the pattern
    """

    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return {}


def load_logs(logfile_path: str) -> list:
    """
    Loads log lines from a file, parses them, and returns a list of log dictionaries
    :arg logfile_path: path to the log file
    :return: list of log dictionaries with the timestamp, level, and message
    :err return: empty list if the file does not exist
    """

    if not Path(logfile_path).is_file() or not Path(logfile_path).exists():
        return []

    with open(logfile_path, 'r') as file:
        return [parse_log_line(line) for line in file]


def filter_logs_by_level(logs: list, log_level: str) -> list:
    """
    Filters log lines by the specified log level
    :arg logs: list of log dictionaries with the timestamp, level, and message
    :arg log_level: log level to filter by
    :return: list of log dictionaries with the specified log level
    """

    return [log for log in logs if log['level'] == log_level]


def count_logs_by_level(logs: list) -> dict:
    ...


def display_log_counts(counts: dict):
    ...
