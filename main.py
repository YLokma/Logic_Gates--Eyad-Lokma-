# This is the work of Eyad Mohamed & Youssof Lokma on 24th of Nov 2021
from Gates import *

def main():
    inputs = []
    inputs_n = int(input("Insert the number of inputs: "))
    print("Input format: n, n, n")
    for num in range(2**inputs_n):
        input_value = input(f"Insert [{num + 1}] row with inputs: ")
        inputs.append(list(int(input_row) for input_row in input_value.split(",")))
    for i in list(inputs):
        print(i)
    print(inputs)

if __name__ == "__main__":
    inputs = []
    no_input = int(input("Insert the number of inputs: "))
    for i in range(no_input):
        value = int(input(f"Insert the {[i - 1]} input: "))
        inputs.append(value)
    
    print("*** *** *** *** *** *** *** ***")
    print(f"\n\tNOT-Gate: {not_gate(inputs[0])}\n")
    print(f"\tAND-GATE: {and_gate(inputs[0], inputs[1])}\n")
    print(f"\tOR-GATE: {or_gate(inputs[0], inputs[1])}\n")
    print(f"\tNAND-GATE: {nand_gate(inputs[0], inputs[1])}\n")
    print(f"\tNOR-GATE: {nor_gate(inputs[0], inputs[1])}\n")
    print(f"\tXOR-GATE: {xor_gate(inputs[0], inputs[1])}\n")