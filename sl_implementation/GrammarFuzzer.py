from fuzzingbook.Fuzzer import *
from fuzzingbook.Grammars import * 
import subprocess
import numpy as np
import ast

import GrammarRunner


UFUNC_GRAMMAR: Grammar = {
    "<start>":
        ["<function>"],

    "<function>":
        ["np.add(<arg>, <arg>)", "np.subtract(<arg>, <arg>)", "np.multiply(<arg>, <arg>)", "np.divide(<arg>, <arg>)", "np.matmul(<array>, <array>)", "np.exp(<arg>)"],

    "<arg>":
        ["<int>", "<float>", "<array>"],

    "<int>":
        [str(i) for i in range(-100, 100)],

    "<float>":
        [str(round(random.uniform(-100.0, 100.0), 2)) for _ in range(100)],
    "<array>":
        ["np.array([" + ", ".join([str(random.uniform(-100.0, 100.0)) for _ in range(random.randint(1, 10))]) + "])" for _ in range(100)],
}

DATETIME_GRAMMAR: Grammar = {
    "<start>": ["<function>"],
    "<function>":
            ["<date> - <date>", "<date> - <timespan>", "<timespan> / <timespan>", "np.busday_offset(<date>, <number>)", "np.is_busday(<date>)", "np.busday_count(<date>, <date>)"],
    "<date>": ["np.datetime64('<formated_date>')"],
    "<timespan>": ["np.timedelta64(<formated_timespan>)"],
    "<formated_date>": ["<year>-<monthday>"],
    "<formated_timespan>": ["NAT", "<number>, '<interval>'"],
    "<year>": [str(i) for i in range(-1, 3000)],
    "<monthday>": ["<month28>-<days28>", "<month30>-<days30>", "<month31>-<days31>"],
    "<month28>": ["02"],
    "<month30>": ["04", "06", "07", "09", "11"],
    "<month31>": ["01", "03", "05", "08", "10", "12"],
    "<days28>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 28)],
    "<days30>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 30)],
    "<days31>": ["0" + str(i) for i in range(1, 9)] + [str(i) for i in range(10, 31)],
    "<number>": [str(i) for i in range(-100, 100)],
    "<interval>": ["D", "M", "Y", "h", "m", "s"],
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

    def run(self, runner: GrammarRunner, print_successful: bool = True) -> Tuple[subprocess.CompletedProcess, str]:
        """Run `runner` with fuzz input"""
        fuzz_input = self.fuzz()
        result = runner.run(fuzz_input)
        process, outcome = result
        if print_successful == False and process.returncode == 0:
            return result
        print(f"Result: {result}")
        return result


    def runs(self, runner: GrammarRunner, trials: int = 10, print_successful: bool = True) -> List[Tuple[subprocess.CompletedProcess, str]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner, print_successful) for _ in range(trials)]