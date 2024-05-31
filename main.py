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
    np.sum: [[int, int], lambda x, y: x + y],
    np.prod: [[int, int], lambda x, y: x * y],
    np.min: [[int, int], lambda x, y: x if x < y else y],
    np.max: [[int, int], lambda x, y: x if x > y else y]
}


def generate():
    for (func, additionals) in functions2.items():
        types = additionals[0]
        implementation = additionals[1]
        pools = []

        for type in types:
            pools.append(v.ValuePoolFuzzer(type))

        for i in range(600):
            arguments = []
            for pool in pools:
                arguments.append(pool.fuzz())

            result = func(arguments)
            result_assertion = implementation(*arguments)

            if result != result_assertion:
                print("AssertionError: " + np.array2string(result) + "!=" + str(result_assertion))
            else:
                print(result)


def main():
    generate()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
