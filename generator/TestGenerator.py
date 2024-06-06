import time
from threading import *
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

    generated_int_pool = generator.generate_pool(int)
    print(generator.type_dir.get(int))


def generateValues(generator: Gen.BasicGenerator, interrupt: Event):
    for func in NpFunctions.functionHeaders:
        generator.generate(func, interrupt)
