
from sympy import symbols, Or, Not, And
from sympy.logic.boolalg import to_cnf

def fol_to_cnf():

    print("FOL to CNF Conversion")
    print("---------------------")

    x = symbols('x')

    Human = symbols('Human(x)')
    Mortal = symbols('Mortal(x)')

    print("\nOriginal FOL Statement:")
    print("For all x: Human(x) -> Mortal(x)")

    print("\nStep 1: Eliminate Implication")

    expr = Or(Not(Human), Mortal)

    print(expr)

    print("\nStep 2: Move Negation Inward")
    print(expr)

    print("\nStep 3: Standardize Variables")
    print("Variable x is already standardized.")

    print("\nStep 4: Skolemization")
    print("No existential quantifier is present.")

    print("\nStep 5: Remove Universal Quantifier")
    print("Universal quantifier is removed.")

    print("\nStep 6: Convert into CNF")

    cnf = to_cnf(expr)

    print("\nFinal CNF:")
    print(cnf)


fol_to_cnf()
