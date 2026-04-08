import re
from fractions import Fraction
def find_max_float(text):
    pattern = r'-?\d+\.\d+|-?\.\d+'
    matches = re.findall(pattern, text)
    if not matches:
        return None  
    floats = [float(num) for num in matches]
    return max(floats)


def find_min_rational(text):
    pattern = r'-?\d+/\d+|-?\d+\.\d+|-?\.\d+|-?\d+'
    
    matches = re.findall(pattern, text)
    
    if not matches:
        return None
    
    rationals = []
    for num_str in matches:
        if '/' in num_str:
            rationals.append(Fraction(num_str))


def find_longest_digit_sequence(text):
    max_length = 0
    current_length = 0
    
    for char in text:
        if char.isdigit():
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0
    
    return max_length
        else:
            rationals.append(Fraction(float(num_str)).limit_denominator())
    
    return min(rationals)
