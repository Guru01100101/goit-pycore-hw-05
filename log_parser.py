import re
from typing import List, Dict
from pathlib import Path


# pattern for log lines in the format: "2021-01-01 12:00:00 INFO Message"
log_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
                         r'(?P<level>\w+) '
                         r'(?P<message>.*)')


def parse_log_line(line: str) -> dict:
    ...


def load_logs(logfile_path: str) -> list:
    ...


def filter_logs_by_level(logs: list, log_level: str) -> list:
    ...


def count_logs_by_level(logs: list) -> dict:
    ...


def display_log_counts(counts: dict):
    ...