# Load-testing-cli

A simple CLI load testing tool.

## Installation

Install using `pip`:

```
$ pip install load-tester
```

## Usage

The simplest usage of `load-tester` requires only a URL to test against and 500 requests synchronously (one at a time). This is what it would look like:

```
$ load-tester https://example.com
.... Done!
--- Results ---
Successful requests     500
Slowest                 0.010s
Fastest                 0.001s
Average                 0.003s
Total time              0.620s
Requests Per Minute     48360
Requests Per Second     806
```

If we want to add concurrency, we'll use the `-c` option, and we can use the `-r` option to specify how many requests that we'd like to make:

```
$ load-tester -r 3000 -c 10 https://example.com
.... Done!
--- Results ---
Successful requests     3000
Slowest                 0.010s
Fastest                 0.001s
Average                 0.003s
Total time              2.400s
Requests Per Minute     90000
Requests Per Second     1250
```
