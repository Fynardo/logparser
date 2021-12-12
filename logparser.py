#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import argparse
from collections import deque
import re


# Partition functions
def _all(fd):
    return fd.read().splitlines()


def _first(fd, n):
    return [fd.readline()[:-1] for _ in range(n)]


def _last(fd, n):
    q = deque(maxlen=n)
    for line in fd:
        q.append(line if line[-1] != '\n' else line[:-1])
    return q


def partition(fd, f, l):
    if f and l:
        raise argparse.ArgumentTypeError('I think this is not the expected usage.')
    elif f:
        lines = _first(fd, f)
    elif l:
        lines = _last(fd, l)
    else:
        lines = _all(fd)
    return lines


# Input selection
def _get_fd(path=None):
    if path:
        return open(path, 'r')
    else:
        return sys.stdin


# Filters
def _filter_timestamp(line):
    s = r'(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]'
    return re.search(s, line) is not None


def _predicates_list(filters):
    predicates = []
    for f in filters:
        if f == 't':
            predicates.append(_filter_timestamp)
    return predicates


# Main
def filter_log(lines, predicates):
    return [line for line in lines if all([pred(line) for pred in predicates])]


def parse_log(file_, f, l, filters):
    fd = _get_fd(file_)
    lines = partition(fd, f, l)
    filtered_lines = filter_log(lines, _predicates_list(filters))
    return filtered_lines


if __name__ == '__main__':

    def positive_int(value):
        v = int(value)
        if v > 0:
            return v
        else:
            raise argparse.ArgumentTypeError('only positive numbers.') 

    parser = argparse.ArgumentParser(description='Parse logs.')
    parser.add_argument('file', metavar='FILE', nargs='?', 
                        help='an integer for the accumulator')
    parser.add_argument('-f','--first', metavar='NUM', type=positive_int, 
                        help='Print first NUM lines')
    parser.add_argument('-l','--last', metavar='NUM', type=positive_int,
                        help='Print last NUM lines')
    parser.add_argument('-t','--timestamps', dest='filters', action='append_const', const='t',
                        help='Print lines that contain a timestamp in HH:MM:SS format')
    parser.set_defaults(filters = [])
    args = parser.parse_args()

    print('\n'.join(parse_log(args.file, args.first, args.last, args.filters)))

