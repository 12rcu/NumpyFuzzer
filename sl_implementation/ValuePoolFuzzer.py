from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np
import inspect

import ValuePoolRunner

class ValuePool:
    pool = []
    index = 0

    def __init__(self) -> None:
        """Constructor"""
        pass

    def getNextValue(self):
        ret = self.pool[self.index]
        self.index = self.index + 1
        if len(self.pool) == self.index:
            self.index = 0
        return ret

class FullValuePool(ValuePool):
    pool = [
            True, False, None, 
            0, 1, -1, 10, 100, 100_000_000_000_000, 0.0, 
            -1.0, 1.0, float("inf"), float("-inf"),
            np.array([]), np.array([1, 2, 3]), np.array([-1, 1, 0]), 
            np.array([0]), np.array([100_000, -100_000]), np.zeros((10, 10))
           ]

class BoolValuePool(ValuePool):
    pool = [True, False, None]

class IntValuePool(ValuePool):
    pool = [0, 1, -1, 10, 100, 100_000_000_000_000]


class FloatValuePool(ValuePool):
    pool = [0.0, -1.0, 1.0, float("inf"), float("-inf")]


class ArrayValuePool(ValuePool):
    pool = [
        np.array([]),
        np.array([1, 2, 3]),
        np.array([-1, 1, 0]),
        np.array([0]),
        np.array([100_000, -100_000]),
        np.zeros((10, 10))
    ]


class ValuePoolFuzzer(Fuzzer):

    def __init__(self, t: type = None) -> None:
        self.t = t
        if t == int:
            self.valuePool = IntValuePool()
        elif t == float:
            self.valuePool = FloatValuePool()
        elif t == np.array:
            self.valuePool = ArrayValuePool()
        else:
            self.valuePool = FullValuePool()

    def fuzz(self):
        """Return fuzz input"""
        return self.valuePool.getNextValue()

    def run(self, runner: ValuePoolRunner) -> Tuple[subprocess.CompletedProcess, str]:
        """Run `runner` with fuzz input"""
        method = runner.method
        args = [self.fuzz() for _ in runner.arg_types]
        result = runner.run(*args)
        print(f"Fuzzed method: {method}, Fuzzed input: {args}, Result: {result}")
        return result

    def runs(self, runner: ValuePoolRunner, trials: int = 10) -> List[Tuple[subprocess.CompletedProcess, str]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for _ in range(trials)]