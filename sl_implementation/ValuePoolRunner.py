from fuzzingbook.Fuzzer import *
import subprocess
import numpy as np
from typing import Tuple, Any, Callable, List

class ValuePoolRunner:
     def __init__(self, method: Callable, arg_types: List[type] = None):
         self.method = method
         self.arg_types = arg_types if arg_types else []

     def run(self, *args) -> Tuple[subprocess.CompletedProcess, str]:
         try:
             result = self.method(*args)
             return subprocess.CompletedProcess(args=args, returncode=0), f"Success: {result}"
         except Exception as e:
             return subprocess.CompletedProcess(args=args, returncode=1), f"Exception: {e}"