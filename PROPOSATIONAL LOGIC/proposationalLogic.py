
from itertools import product

def implies(p, q):
    return not p or q


def check_entailment():

    symbols = ['P', 'Q']

    print("Knowledge Base:")
    print("1. P -> Q")
    print("2. P")

    query = 'Q'

    print("\nQuery:", query)

    print("\nTruth Table:")
    print("P\tQ\tP->Q\tKB\tQuery")

    entailment = True

    for values in product([False, True], repeat=2):

        model = dict(zip(symbols, values))

        P = model['P']
        Q = model['Q']

        rule = implies(P, Q)

        KB = rule and P

        print(P, "\t", Q, "\t", rule, "\t", KB, "\t", Q)

        if KB and not Q:
            entailment = False

    print("\nResult:")

    if entailment:
        print("KB entails the query.")
        print("KB |= Q : TRUE")
    else:
        print("KB does not entail the query.")
        print("KB |= Q : FALSE")


check_entailment()
