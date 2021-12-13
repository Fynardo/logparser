# -*- coding: utf-8 -*-


from tests.base import base_path, get_fd, load_log
from logparser import _filter_timestamp, _filter_ipv4, _filter_ipv6


def test_all_valid_timestamps():
    log = load_log('test_valid_timestamps.log')

    for line in log:
        assert _filter_timestamp(line)


def test_all_invalid_timestamps():
    log = load_log('test_invalid_timestamps.log')

    for line in log:
        assert not _filter_timestamp(line)


def test_all_valid_ipv4():
    log = load_log('valid_ipv4.log')

    for line in log:
        assert _filter_ipv4(line)


def test_all_invalid_ipv4():
    log = load_log('invalid_ipv4.log')

    for line in log:
        assert not _filter_ipv4(line)


def test_all_valid_ipv6():
    log = load_log('valid_ipv6.log')

    for line in log:
        assert _filter_ipv6(line)


def test_all_valid_ipv6():
    log = load_log('invalid_ipv6.log')

    for line in log:
        assert not _filter_ipv6(line)

