#!/usr/bin/env python
# -*- coding: utf-8 -*-


from logparser import _first, _last, _all
from pathlib import Path


_base_path = Path('tests')

def get_fd(logfile):
    return open(_base_path / logfile)

def load_log(logfile):
    with get_fd(logfile) as f:
        return f.read().splitlines()


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
    assert len(lines) == 5
    for i in range(len(lines)):
        assert lines[i] == log[i]

