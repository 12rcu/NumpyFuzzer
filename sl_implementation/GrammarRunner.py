from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np
from typing import Tuple, Any, Callable, List

class GrammarRunner:
    def __init__(self):
        pass

    def run(self, args) -> Tuple[subprocess.CompletedProcess, str]:
        try:
            result = eval(args)
            return subprocess.CompletedProcess(args=args, returncode=0), f"Success: {result}"
        except Exception as e:
            return subprocess.CompletedProcess(args=args, returncode=1), f"Exception: {e}"