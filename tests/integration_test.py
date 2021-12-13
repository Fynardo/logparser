# -*- coding: utf-8 -*-

from tests.base import *
from logparser import parse_args, parse_log


def test_log_0_timestamp():
    args = parse_args(['tests/test_0.log', '-t'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 25


def test_log_0_ipv4():
    # Every line in test_0 has IPV4 addresses
    args = parse_args(['tests/test_0.log', '-i'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 25


def test_log_0_ipv4_first():
    args = parse_args(['tests/test_0.log', '-i', '-f', '10'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 10


def test_log_0_ipv4_last():
    args = parse_args(['tests/test_0.log', '-i', '-l', '15'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 15

def test_log_0_ipv6():
    # There is no valid ipv6 in test_0.log
    args = parse_args(['tests/test_0.log', '-I'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert parsed_lines == []

def test_log_3_ipv6():
    args = parse_args(['tests/test_3.log', '-I', '-l', '15'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 2


def test_log_3_ipv4_ipv6():
    args = parse_args(['tests/test_3.log', '-i', '-I', '-l', '5'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 0
    args = parse_args(['tests/test_3.log', '-i', '-I', '-l', '15'])
    parsed_lines = parse_log(args.file, args.first, args.last, args.filters)
    assert len(parsed_lines) == 1

