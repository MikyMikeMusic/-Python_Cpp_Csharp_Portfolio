# -*- coding: utf-8 -*-

from unittest import result


class Computer_Architecture:
    def __init__(self):
        self.cache = {}
        self.cache_size = 4
    
    def calculate_max_binary_value(self, n):
        return 2**n - 1

    def binary_to_decimal(self, binary_str):
        decimal_value = 0
        for i, digit in enumerate(reversed(binary_str)):
            if digit == "1":
                decimal_value += 2**i
        return decimal_value
    
    def represent_number_with_base(self, number, base):
        return f"{number}_{base}"

    def decimal_to_binary(self, decimal_value):
        binary_str = ""
        while decimal_value > 0:
            remainder = decimal_value % 2
            binary_str = str(remainder) + binary_str
            decimal_value = decimal_value // 2
        return binary_str

    def add_binary_numbers(self, binary_str1, binary_str2):
        max_length = max(len(binary_str1), len(binary_str2))
        binary_str1 = binary_str1.zfill(max_length)
        binary_str2 = binary_str2.zfill(max_length)

        result = ""
        carry = 0

        for i in range(max_length - 1, -1, -1):
            r = carry
            r += 1 if binary_str1[i] == "1" else 0
            r += 1 if binary_str2[i] == "1" else 0

            result = ("1" if r % 2 == 1 else "0") + result
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = "1" + result

        return result

    def subtract_binary_numbers(self, binary_str1, binary_str2):
        max_length = max(len(binary_str1), len(binary_str2))
        binary_str1 = binary_str1.zfill(max_length)
        binary_str2 = binary_str2.zfill(max_length)

        result = ""
        borrow = 0

        for i in range(max_length - 1, -1, -1):
            sub = int(binary_str1[i]) - int(binary_str2[i]) - borrow
            if sub < 0:
                sub += 2
                borrow = 1
            else:
                borrow = 0
            result = str(sub) + result

        return result.lstrip("0") or "0"

    def multiply_binary_numbers(self, binary_str1, binary_str2):
        result = 0

        decimal_value1 = self.binary_to_decimal(binary_str1)
        decimal_value2 = self.binary_to_decimal(binary_str2)

        decimal_result = decimal_value1 * decimal_value2

        binary_result = self.decimal_to_binary(decimal_result)

        return binary_result

    def divide_binary_numbers(self, dividend, divisor):
        decimal_dividend = self.binary_to_decimal(dividend)
        decimal_divisor = self.binary_to_decimal(divisor)

        if decimal_divisor == 0:
            raise ValueError("La divisione per zero non e' permessa.")

        decimal_quotient = decimal_dividend // decimal_divisor

        binary_quotient = self.decimal_to_binary(decimal_quotient)

        return binary_quotient

    def Logic_gate(self, type, a, b=None):
        Truth_tables = {
            "AND": {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1},
            "OR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1},
            "NAND": {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 0},
            "NOR": {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 0},
            "XOR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},
            "XNOR": {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1},
        }

        if type == "NOT":
            if a == 0:
                return 1
            else:
                return 0
        else:
            return Truth_tables[type][(a, b)]
    
    def simulate_ISA(self, instruction, architecture_type):
        # Definition of OPCODE for MIPS instructions
        MIPS_OPCODES = {
            "000000": "R-Type",
            "001000": "Addi (Add Immediate)",
            "000010": "J (Jump)",
        }
        
        if architecture_type == "RISC":
            # RISC is characterized by a fixed-length instruction set with simple operations
            opcode = instruction[:6]
            operation = MIPS_OPCODES.get(opcode, "Invalid instruction")
            if operation == "R-Type":
                return "Operation defined by func field"
            else:
                return operation
        elif architecture_type == "CISC":
            # CISC is characterized by a variable-length instruction set with complex operations
            if instruction.startswith("110") or instruction.startswith("111"):
                return "Complex operation based on variable-length instruction"
            else:
                return "Invalid instruction"
        else:
            return "Invalid architecture type"
        
    def high_level_to_machine_code(self, instruction):
        instruction_to_binary = {
            "ADD": "100000",  
            "SUB": "100010",  
            "MULT": "011000", 
        }

        register_to_binary = {
            "$0": "00000",
            "$1": "00001",
            "$2": "00010",
            "$3": "00011",
        }

        parts = instruction.split()
        opcode = parts[0]
        registers = parts[1:]

        binary_opcode = instruction_to_binary.get(opcode, "Unknown")

        binary_registers = [register_to_binary.get(reg, "Unknown") for reg in registers]

        machine_code = binary_opcode + ''.join(binary_registers)

        return machine_code
    
    def access_cache(self, address, data=None):
        if address in self.cache:
            if data != None:
                self.cache[address] = data
            return self.cache[address]
        else:
            if data != None:
                if len(self.cache) >= self.cache_size:
                    self.cache.pop(next(iter(self.cache)))
                self.cache[address] = data
            return data
    
    def simd_vector_addition(self, vector1, vector2):
        if len(vector1) != len(vector2):
            raise ValueError("Vectors have the same length")
        result_vector = [a + b for a, b in zip(vector1, vector2)]
        
        return result_vector

My_computer = Computer_Architecture()
print(My_computer.multiply_binary_numbers("100", "111"))

print(My_computer.Logic_gate("AND", 1, 0))
print(My_computer.Logic_gate("OR", 1, 0))
print(My_computer.Logic_gate("NAND", 1, 0))
