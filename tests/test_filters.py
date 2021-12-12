# -*- coding: utf-8 -*-


from tests.base import base_path, get_fd, load_log
from logparser import filter_log, _filter_timestamp


def test_all_valid_timestamps():
    log = load_log('test_valid_timestamps.log')

    for line in log:
        assert _filter_timestamp(line)


def test_all_invalid_timestamps():
    log = load_log('test_invalid_timestamps.log')

    for line in log:
        assert not _filter_timestamp(line)
