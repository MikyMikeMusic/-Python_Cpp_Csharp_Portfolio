# from curses.ascii import isalpha 
from curses.ascii import isalpha, isdigit
from itertools import permutations, combinations
import math
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
                elif char.isupper(): # This elif should be aligned with if char.islower():
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
        if base < 2 or base > 16:
            return ValueError("The base must be between 2 and 16")
        
        decimal_value = 0
        exponent = 0
        
        number_reversed = number[::-1]  
        
        for digit in number_reversed:
            if digit.isdigit():
                digit_value = int(digit)
            elif digit.isalpha():
                digit_value = ord(digit.upper()) - ord('A') + 10
            else:
                raise ValueError("Invalid digit")
            
            if digit_value >= base:
                raise ValueError("Digit is greater than the base")
            
            decimal_value += digit_value * (base ** exponent)
            exponent += 1
            
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
    

              