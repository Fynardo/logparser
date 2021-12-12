# Log Parser
Python CLI application that helps parsing logs of various kinds.


# Usage

`./logparser.py [OPTION]... [FILE]`

## Options

* -h, --help         Print help
* -f, --first NUM    Print first NUM lines
* -l, --last NUM     Print last NUM lines
* -t, --timestamps   Print lines that contain a timestamp in HH:MM:SS format

If FILE is omitted, standard input is used instead.

If multiple options are used at once, the result is the intersection of their
results.

## Examples

`cat test_0.log | ./logparser.py --first 10`

`./logparser.py -l 5 test_1.log`

`./logparser.py --timestamps test_2.log`



# Testing

Testing is executed with pytest as usual, Makefile is present with some options: 

`make test`

Or, test with coverage

`make cov-test`

**Note**: Test files were generated using [logs.to](https://www.logs.to/) tool.
