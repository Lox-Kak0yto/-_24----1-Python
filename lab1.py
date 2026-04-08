
def sum_of_prime_divisors(n):
    "Функия 1"
    if n <= 1:
        return 0
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime_divisors_sum = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors_sum += i
    
    return prime_divisors_sum

def count_odd_digits_greater_than_3(n):
    "Функия 2"
    n = abs(n)
    
    if n == 0:
        return 0
    
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1 and digit > 3:
            count += 1
        n //= 10
    
    return count


            product *= divisor
            found = True
    
    return product if found else 0

def product_of_divisors_with_digit_sum_less_than_original(n):
    "Функия 3"
    if n == 0:
        return 0
    
    def digit_sum(num):
        num = abs(num)
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total
    
    original_sum = digit_sum(n)
    
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    
    product = 1
    found = False
    
    for divisor in divisors:
        if digit_sum(divisor) < original_sum:
