# -*- coding: utf-8 -*-


from tests.base import base_path, get_fd, load_log
from logparser import _first, _last, _all


def test_first():
    log = load_log('test_0.log')

    fd = get_fd('test_0.log')
    lines = _first(fd, 3)
    assert len(lines) == 3
    for i in range(len(lines)):
        assert lines[i] == log[i] 


def test_last():
    log = load_log('test_0.log')

    fd = get_fd('test_0.log')
    lines = _last(fd, 2)
    assert len(lines) == 2
    for i in range(len(lines)):
        assert lines[-(i+1)] == log[-(i+1)] 


def test_all():
    log = load_log('test_0.log')

    fd = get_fd('test_0.log')
    lines = _all(fd)
    assert len(lines) == 25
    for i in range(len(lines)):
        assert lines[i] == log[i]

