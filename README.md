# Log Parser
Python CLI application that helps parsing logs of various kinds.


# Usage

`./logparser.py [OPTION]... [FILE]`

## Options

* -h, --help         Print help
* -f, --first NUM    Print first NUM lines
* -l, --last NUM     Print last NUM lines
* -t, --timestamps   Print lines that contain a timestamp in HH:MM:SS format
* -i, --ipv4         Print lines that contain an IPv4 address, matching IPs are highlighted
* -I, --ipv6         Print lines that contain an IPv6 address (standard notation), matching IPs are highlighted

If FILE is omitted, standard input is used instead.

If multiple options are used at once, the result is the intersection of their
results.

## Examples

`cat test_0.log | ./logparser.py --first 10`

`./logparser.py -l 5 test_1.log`

`./logparser.py --timestamps test_2.log`

`./logparser.py --ipv4 test_3.log`

`./logparser.py --ipv6 test_3.log`

`./logparser.py --ipv4 --last 50 test_3.log`


# Testing

Testing is executed with pytest as usual, Makefile is present with some options: 

`make test`

Or, test with coverage

`make cov-test`

**Note**: Test files were generated using [logs.to](https://www.logs.to/) tool.
