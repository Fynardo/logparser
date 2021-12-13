# -*- coding: utf-8 -*-

from logparser import parse_args


def test_file_arg():
    args = parse_args(['test_file.log'])
    assert args.file is not None


def test_first_arg():
    args = parse_args(['-f', '5'])
    assert args.first is not None
    assert args.first == 5
    args = parse_args(['--first', '3'])
    assert args.first is not None
    assert args.first == 3


def test_last_arg():
    args = parse_args(['-l', '5'])
    assert args.last is not None
    assert args.last == 5
    args = parse_args(['--last', '3'])
    assert args.last is not None
    assert args.last == 3


def test_timestamps_arg():
    args = parse_args(['-t'])
    assert args.filters == ['t']
    args = parse_args(['--timestamps'])
    assert args.filters == ['t']


def test_ipv4_arg():
    args = parse_args(['-i'])
    assert args.filters == ['i']
    args = parse_args(['--ipv4'])
    assert args.filters == ['i']


def test_ipv6_arg():
    args = parse_args(['-I'])
    assert args.filters == ['I']
    args = parse_args(['--ipv6'])
    assert args.filters == ['I']
