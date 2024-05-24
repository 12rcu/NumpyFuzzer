from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np

from typing import Any, TypeVar
from enum import Enum
import inspect
import itertools

class RunOutcome(Enum):
    PASS       = 1
    FAIL       = 2
    UNRESOLVED = 3

ValuePool = list[Any]
ValuePools = dict[type, ValuePool]
RunResult = tuple[Any, RunOutcome]

vpools: ValuePools = {
    int: [0, 1, -1, 10, 100, 100_000_000_000_000],
    str: ["lel", "lol", "lul"],
    float: [0.0, -1.0, 1.0, float("inf"), float("-inf")],
    list: [[], [1,2,3], [-1,1,0], [0], [100_000, -100_000], [[0]*100]*100,
           [""], [None], ["lel"], [r""], [[]], [{}], [set()]],
    np.ndarray: [np.array([]), np.array([1, 2, 3]), np.array([-1, 1, 0]),
            np.array([0]), np.array([100_000, -100_000]), np.zeros((10, 10))]
}

class FunctionRunner(Runner):
    def __init__(self, function):
        self.function2fuzz = function

    def run(self, inp: list[Any]) -> RunResult:
        outcome: RunOutcome = RunOutcome.UNRESOLVED
        try:
            self.function2fuzz(*inp)
            outcome = RunOutcome.PASS
        except Exception as e:
            # TODO(jso): possibly also log the exception
            outcome = RunOutcome.FAIL
        finally:
            return (inp, outcome)

class ValuePoolFuzzer(Fuzzer):
    def __init__(self, vpools: ValuePools, function):
        assert(not vpools is None)
        self.vpools: ValuePools = vpools
        assert(not function is None)
        self.argspec: inspect.FullArgSpec = inspect.getfullargspec(function)
        self.__iter_init()

    def fuzz(self) -> str:
        return next(self.iter_values)

    def reset(self) -> None:
        self.__iter_init()

    def __iter_init(self) -> None:
        self.iter_values: Iterable[Any] = itertools.product(
                *[self.vpools.get(t) for t in self.argspec.annotations.values()])

    def run(self, runner: Runner) -> RunResult:
        fuzz_input: Any = self.fuzz()
        return runner.run(inp=fuzz_input)

    def runs(self, runner: Runner, max_trials: int = 10) -> list[RunResult]:
        results: list[RunResult] = list()
        for i in range(max_trials):
            try:
                results.append(self.run(runner))
            except StopIteration:
                break
        return results

