from fuzzingbook.Fuzzer import *
from fuzzingbook.Grammars import * 
import subprocess
import numpy as np
import ast

import GrammarRunner


NUMPY_GRAMMAR: Grammar = {
    "<start>":
        ["<function>"],

    "<function>":
        ["np.exp(<arg>)", "np.add(<arg>, <arg>)", "np.multiply(<arg>, <arg>)"],

    "<arg>":
        ["<int>", "<float>", "<array>"],

    "<int>":
        [str(i) for i in range(0, 100)],

    "<float>":
        [str(round(random.uniform(0.0, 100.0), 2)) for _ in range(100)],
    "<array>":
        ["np.array([" + ", ".join([str(random.uniform(0.0, 100.0)) for _ in range(random.randint(1, 10))]) + "])" for _ in range(100)],
}

class GrammarFuzzer():
    def __init__(self, grammar: Grammar) -> None:
        self.grammar = grammar

    def generate(self, start="<start>") -> str:
        """Generate a random string based on the grammar"""
        def _generate(symbol):
            if symbol not in self.grammar:
                return symbol
            expansion = random.choice(self.grammar[symbol])
            parts = re.findall(r"<[^>]+>|[^<]+", expansion)
            return "".join(_generate(part) for part in parts)
        return _generate(start)

    def fuzz(self):
        """Return fuzz input"""
        return self.generate()

    def run(self, runner: GrammarRunner) -> Tuple[subprocess.CompletedProcess, str]:
        """Run `runner` with fuzz input"""
        fuzz_input = self.fuzz()
        result = runner.run(fuzz_input)
        print(f"Fuzzed input: {fuzz_input}, Result: {result}")
        return result


    def runs(self, runner: GrammarRunner, trials: int = 10) -> List[Tuple[subprocess.CompletedProcess, str]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for _ in range(trials)]