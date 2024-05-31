#!/usr/bin/env python3
"""
Module Docstring
"""
import numpy as np

import ValuePool as v

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

numpy_functions = [
    np.sum, np.prod, np.mean, np.std, np.var,
    np.min, np.max, np.argmin, np.argmax, np.sort
]

functions2 = {
    np.sum: [int, int]

}


def generate():
    for (func, types) in functions2.items():
        pools = []

        for type in types:
            pools.append(v.ValuePoolFuzzer(type))

        arguments = []
        for pool in pools:
            arguments.append(pool.fuzz())

        result = func(*arguments)
        print(result)


def test_sum():
    intPool1 = v.ValuePoolFuzzer(int)
    intPool2 = v.ValuePoolFuzzer(int)
    for i in range(10):
        val1 = intPool1.fuzz()
        val2 = intPool2.fuzz()
        result = np.sum([val1, val2])
        assert result == val1 + val2
        print(result)


def test_numpy_functions(fuzzer, functions):
    for func in functions:
        try:

            arg = fuzzer.fuzz()
            result = func(arg)
            print(f"Function: {func.__name__}, Argument: {arg}, Result: {result}")
        except Exception as e:
            print(f"Function: {func.__name__}, Argument: {arg}, Exception: {e}")


def main():
    fuzzer = v.ValuePoolFuzzer(int)
    generate()
    return
    test_numpy_functions(fuzzer, numpy_functions)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
