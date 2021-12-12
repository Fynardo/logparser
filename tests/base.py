# -*- coding: utf-8 -*-


from pathlib import Path


base_path = Path('tests')


def get_fd(logfile):
    return open(base_path / logfile)

def load_log(logfile):
    with get_fd(logfile) as f:
        return f.read().splitlines()

