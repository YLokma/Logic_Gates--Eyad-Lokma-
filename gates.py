# /usr/bin/python3
class LogicGates:
    def AND(input_1, input_2):
        """This is a function to represent the AND gate.

        Args:
            input_1 ([int]): [this is an input to determine the output of AND gate]
            input_2 ([int]): [this is an input to determine the output of AND gate]
        """ """"""
        if input_1 and input_2 == 1:
            return True
        elif input_1 + input_2 <= 1:
            return False

    def NOT(input_1):
        """This is a function to represent the NOT gate

        Args:
            input_1 ([Int]): [this is an input to determine the output of NOT gate]
        """
        if input_1 == 0:
            return True
        elif input_1 == 1:
            return False

    def OR(input_1, input_2):
        """This is a function to represent the AND gate.

        Args:
            input_1 ([int]): [this is an input to determine the output of OR gate]
            input_2 ([int]): [this is an input to determine the output of OR gate]
        """ """"""
        if input_1 or input_2 == 1:
            return True
        elif input_1 and input_2 == 0:
            return False

    def NAND(input_1, input_2):
        """This is a function to represent the AND gate.

        Args:
         input_1 ([int]): [this is an input to determine the output of NAND gate]
         input_2 ([int]): [this is an input to determine the output of NAND gate]
        """
        if input_1 and input_2 == 1:
            return False
        elif input_1 + input_2 <= 1:
            return True

    def NOR(input_1, input_2):
        """This is a function to represent the AND gate.

        Args:
         input_1 ([int]): [this is an input to determine the output of NOR gate]
         input_2 ([int]): [this is an input to determine the output of NOR gate]
        """
        if input_1 or input_2 == 1:
            return False
        elif input_1 and input_2 == 0:
            return True

    def XOR(input_1, input_2):
        """This is a function to represent the AND gate.

        Args:
            input_1 ([int]): [this is an input to determine the output of OR gate]
            input_2 ([int]): [this is an input to determine the output of OR gate]
        """ """"""
        if input_1 + input_2 == 1:
            return True
        else:
            return False
