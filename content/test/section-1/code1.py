#!/usr/bin/env python3

"""
This script finds the first 10 prime numbers and calculates their sum.
A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.
"""

import math

def is_prime(num: int) -> bool:
    """
    Checks if a given integer is a prime number efficiently.

    Args:
        num: An integer to check for primality.

    Returns:
        True if the number is prime, False otherwise.
    """
    # Prime numbers must be greater than 1.
    if num <= 1:
        return False
    
    # Check for factors from 2 up to the integer square root of the number.
    # We only need to check up to the square root because if a number `n` has a 
    # divisor larger than its square root, it must also have one smaller.
    # math.isqrt() is used for an efficient integer square root calculation.
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
            
    return True

def main():
    """
    Main function to find the first 10 primes, sum them, and print the result.
    """
    # --- Configuration ---
    primes_to_find = 10
    
    # --- Logic ---
    primes_found = []
    current_number = 2

    # Loop until we have found the desired number of primes
    while len(primes_found) < primes_to_find:
        if is_prime(current_number):
            primes_found.append(current_number)
        current_number += 1

    # Calculate the sum of the found prime numbers
    total_sum = sum(primes_found)

    # --- Output ---
    print(f"The first {primes_to_find} prime numbers are: {primes_found}")
    print(f"Their sum is: {total_sum}")

# This standard boilerplate checks if the script is being run directly
# and, if so, calls the main() function.
if __name__ == "__main__":
    main()
