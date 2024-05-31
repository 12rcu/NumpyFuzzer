from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np
from random import randrange

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
            self.index = randrange(len(self.pool))
        return ret


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

    def __init__(self, t: type) -> None:
        super().__init__()
        if t == int:
            self.valuePool = IntValuePool()
        elif t == float:
            self.valuePool = FloatValuePool()
        else:
            raise NotImplemented()

    def fuzz(self):
        """Return fuzz input"""
        return self.valuePool.getNextValue()

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for i in range(trials)]
