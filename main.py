#!/usr/bin/env python3

import ValuePool as v

__version__ = "0.1.0"
__license__ = "Apache2"

def func2test(lel: int, lul: float):
    pass

def main():
    frunner = v.FunctionRunner(func2test)
    fuzzer = v.ValuePoolFuzzer(v.vpools, func2test)
    # print(fuzzer.fuzz())
    results = fuzzer.runs(frunner, max_trials=100)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
