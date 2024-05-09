import decimal
from itertools import permutations, combinations
import math
import stat
from tokenize import Exponent 

class DiscreteMath:
    def __init__(self):
        pass
    
    @staticmethod
    def mod(a, b):
        """Returns the modulus of a by b."""
        return a % b
    
    @staticmethod
    def congruent(a, b, n):
        """Checks if a is congruent to b modulo n."""
        return DiscreteMath.mod(a - b, n) == 0
    
    @staticmethod
    def caesar_cipher(text, shift=3):
        """Encrypts text using the Caesar cipher with an optional shift (default is 3)."""
        encrypted = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                encrypted += chr(shifted)
            else:
                encrypted += char
        return encrypted
    
    @staticmethod
    def factorial(n):
        """Returns the factorial of n."""
        return math.factorial(n)
    
    @staticmethod
    def permutation_count(n, r):
        """Returns the number of permutations of n items taken r at a time."""
        return math.perm(n, r)
    
    @staticmethod
    def combination_count(n, r):
        """Returns the number of combinations of n items taken r at a time."""
        return math.comb(n, r)
    
    @staticmethod
    def pascals_triangle(n):
        """Generates Pascal's triangle up to row n."""
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
    
    @staticmethod
    def sum_of_natural_numbers(n):
        """Calculates the sum of the first n natural numbers."""
        if n == 1:
            return 1
        else:
            sum_ = n + DiscreteMath.sum_of_natural_numbers(n-1)
            assert sum_ == n * (n + 1) / 2, "The proof fails for n = {}".format(n)
            return sum_
        
    @staticmethod
    def sum_of_odd_numbers(n):
        """Calculates the sum of the first n odd numbers."""
        sum_ = 0
        last_odd = 1
        for _ in range(n):
            sum_ += last_odd
            last_odd += 2
        return sum_
    
    @staticmethod
    def verify_sum_of_odd_numbers_k_plus_1(k):
        """Verifies if the sum of the first k+1 odd numbers equals (k+1)^2."""
        sum_ = 0
        for i in range(1, k + 2):
            sum_ += 2 * i - 1
        return sum_ == (k + 1) ** 2
    
    @staticmethod
    def verify_sum_triplet(n):
        """Verifies if (n+1) + n + (n-1) = 3n for a given positive integer n."""
        return (n + 1) + n + (n - 1) == 3 * n
    
    @staticmethod
    def convert_to_decimal(number, base):
        if number.startswith("0b"):
            number = number[2:]
        elif number.startswith("0o"):
            number = number[2:]
        elif number.startswith("0x"):
            number = number[2:]
        
        decimal_value = 0
        exponent = len(number) - 1
        for digit in number:
            if digit in '0123456789ABCDEFabcdef':
                digit_value = int(digit, base)
                decimal_value += digit_value * (base ** exponent)
                exponent -= 1
            else:
                raise ValueError("Invalid digit" + digit)
        return decimal_value

    @staticmethod
    def decimal_to_binary(decimal_number):
        if decimal_number == 0:
            return "0b0"
        
        binary_digits = []
        
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_digits.append(str(remainder))
            decimal_number = decimal_number // 2
            
        binary_digits.reverse()
        
        binary_number = "0b" + "".join(binary_digits)
        
        return binary_number
    
    @staticmethod
    def decimal_to_octal(decimal_number):
        if decimal_number == 0:
            return "0"
        
        octal_digits = []
        
        while decimal_number > 0:
            remainder = decimal_number % 8
            octal_digits.append(str(remainder))
            decimal_number = decimal_number // 8
            
        octal_digits.reverse()
        
        octal_number = "".join(octal_digits)
        
        return octal_number
    
    @staticmethod
    def octal_to_decimal(octal_number):
        if octal_number.startswith("0o"):
            octal_number = octal_number[2:]
        
        decimal_value = 0
        exponent = 0
        
        octal_number_reversed = octal_number[::-1]
        
        for digit in octal_number_reversed:
            digit_value = int(digit)
            decimal_value += digit_value * (8 ** exponent)
            exponent += 1
            
        return decimal_value
    
    @staticmethod
    def binary_to_octal(binary_number):
        decimal_value = DiscreteMath.convert_to_decimal(binary_number, 2)
        octal_number = DiscreteMath.decimal_to_octal(decimal_value)
        return octal_number
       
    @staticmethod
    def decimal_to_hexadecimal(decimal_number):
        if decimal_number == 0:
            return "0x0"
        
        hexadecimal_digits = []
        hex_map = "0123456789ABCDEF"
        
        while decimal_number > 0:
            remainder = decimal_number % 16
            hexadecimal_digits.append(hex_map[remainder])
            decimal_number = decimal_number // 16
            
        hexadecimal_digits.reverse()
        
        hexadecimal_number = "0x" + "".join(hexadecimal_digits)
        
        return hexadecimal_number
    
    @staticmethod
    def hexadecimal_to_decimal(hex_number):
        if hex_number.startswith("0x"):
            hex_number = hex_number[2:]
        
        decimal_value = 0
        exponent = 0
        
        hex_number_reversed = hex_number[::-1].upper()
        
        hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        
        for digit in hex_number_reversed:
            if digit in hex_map:
                decimal_value += hex_map[digit] * (16 ** exponent)
                exponent += 1
            else:
                raise ValueError("Invalid digit" + digit)
            
        return decimal_value
    
    @staticmethod
    def hexadecimal_to_octal(hex_number):
        decimal_value = DiscreteMath.hexadecimal_to_decimal(hex_number)
        octal_number = DiscreteMath.decimal_to_octal(decimal_value)
        return octal_number
    
    @staticmethod
    def set_demonstration(U, A, B):
        union = A.union(B)
        print(f"Union of A and B: {union}")
        
        intersection = A.intersection(B)
        print(f"Intersection of A and B: {intersection}")
        
        difference = A.difference(B)
        print(f"Difference of A and B: {difference}")
        
        complement = U.difference(A)
        print(f"Complement of A: {complement}")
        
        cardinality = len(A)
        print(f"Cardinality of A: {cardinality}")
        
    @staticmethod
    def combinatorial_examples():
        # Enumeration
        print("Enumeration: Selecting an element from a set of 3 elements.")
        elements = ['a', 'b', 'c']
        for element in elements:
            print(element)

        # Principle of Addition and Multiplication
        print("\nAddition Principle: Choosing between 2 sets of 3 elements each.")
        set1 = ['a', 'b', 'c']
        set2 = ['d', 'e', 'f']
        total_choices = len(set1) + len(set2)
        print(f"Total possible choices: {total_choices}")

        print("\nMultiplication Principle: Choosing one element from each of 2 sets of 3 elements.")
        total_combinations = len(set1) * len(set2)
        print(f"Total possible combinations: {total_combinations}")

        # Permutations and Combinations
        n = 5
        r = 3
        print(f"\nPermutations of {n} elements taken {r} at a time: {DiscreteMath.permutation_count(n, r)}")
        print(f"Combinations of {n} elements taken {r} at a time: {DiscreteMath.combination_count(n, r)}")

        # Permutations of a Multiset
        # Example: Calculating permutations of 'AAB'
        multiset = {'A': 2, 'B': 1}
        n = sum(multiset.values())
        r_values = multiset.values()
        multiset_permutations = math.factorial(n) / math.prod([math.factorial(r) for r in r_values])
        print(f"\nPermutations of the multiset 'AAB': {multiset_permutations}")

        # Decomposition into Subcases and Allowed vs Not Allowed Cases
        # Example: Calculating the number of strings of length 3 with at least one 'A'
        total_strings = 3**3  # Total possible strings with 3 letters (A, B, C)
        strings_without_A = 2**3  # Strings without 'A' (only B and C)
        strings_with_at_least_one_A = total_strings - strings_without_A
        print(f"\nStrings of length 3 with at least one 'A': {strings_with_at_least_one_A}")
             
# ///////////////////////////////////////////////////////////////////// #

if __name__ == "__main__":
    
    # Test the DiscreteMath class
    test_hex = "0x19BCF"
    result = DiscreteMath.hexadecimal_to_decimal(test_hex)
    
    octal_number = "0o771"
    decimal_value = DiscreteMath.octal_to_decimal(octal_number)
    
    hexadecimal_number = "0x3ad"
    octal_number = DiscreteMath.hexadecimal_to_octal(hexadecimal_number)
    
    decimal_number = 6218
    binary_number = DiscreteMath.decimal_to_hexadecimal(decimal_number)
    
    decimal_number_2 = 143
    binary_number_2 = DiscreteMath.decimal_to_binary(decimal_number_2)
    
    binary_number =  "0b1000010111001"
    octal_value = DiscreteMath.binary_to_octal(binary_number)

# Print results
    
    print(f"Decimal value of {test_hex} is {result}")
    print(f"Decimal value of {octal_number} is {decimal_value}")
    print(f"Octal value of {hexadecimal_number} is {octal_number}")
    print(f"Binary value of {decimal_number} is {binary_number}")
    print(f"Binary value of {decimal_number_2} is {binary_number_2}")
    print(f"Octal value of {binary_number} is {octal_value}")                                              


        
        
    

              