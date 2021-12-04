# /usr/bin/python3
from gates import LogicGates
from cie import cie_list

gate_values = {
   'AND': LogicGates.AND,
   'NAND': LogicGates.NAND,
   'OR': LogicGates.OR,
   'XOR': LogicGates.XOR,
   'NOR': LogicGates.NOR,
   'NOT': LogicGates.NOT
}

cie_list(3)

def get_statement():
    print(
        """
        GUIDELINES TO STATMENT:
            1. Convert to level 1 statement if not already
            2. Make the X gate the subject
                eg: (NOT A)OR(NOT C) ===> OR(NOT(A), NOT(C))
            3. Replace the inputs to their respective number
                eg: (A, B, C) ==> (1, 2, 3)
        WARNING:
            The script has not been setup for level 3 as of now...
        """
    )
    global statement
    statement = input("Enter your statment: ")
    return statement


def filter_statement(statement):
    if '1' in statement:
        statement.replace('1', '{cie[0][0]}')
        return statement


print(filter_statement(get_statement()))


"""
x = eval(statement, {
   '__builtins__': None
}, gate_values)
print(x)
"""
