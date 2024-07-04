from NpFunctions import *
import valuepool.ValuePool as vP


def generate():
    for (func, additions) in assertFunctions.items():
        types = additions[0]
        implementation = additions[1]
        pools = []

        for t in types:
            pools.append(vP.ValuePoolFuzzer(t))

        for i in range(600):
            arguments = []
            for pool in pools:
                arguments.append(pool.fuzz())

            result = func(arguments)
            result_assertion = implementation(*arguments)

            if result != result_assertion:
                print("AssertionError: " + np.array2string(result) + "!=" + str(result_assertion) + " for func " + str(
                    func) + " with args " + str(arguments))
            # else:
            #    print(result)
