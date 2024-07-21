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
    ...


def filter_logs_by_level(logs: list, log_level: str) -> list:
    ...


def count_logs_by_level(logs: list) -> dict:
    ...


def display_log_counts(counts: dict):
    ...