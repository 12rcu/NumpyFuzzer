import time
from threading import *

import numpy as np

import generator.BasicGenerator as Gen
import NpFunctions


def testGenerator():
    generator = Gen.BasicGenerator()
    interrupt = Event()

    t = Thread(target=generateValues, args=(generator, interrupt))
    t.start()

    time.sleep(10)

    interrupt.set()
    t.join()

    generated_int_pool = generator.generate_pool(np.int64)
    print(generator.type_dir.get(np.int64))
    print(generator.type_dir.keys())


def generateValues(generator: Gen.BasicGenerator, interrupt: Event):
    for func in NpFunctions.functionHeaders:
        generator.generate(func, interrupt)
