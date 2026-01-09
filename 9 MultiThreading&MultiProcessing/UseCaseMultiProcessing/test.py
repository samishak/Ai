import multiprocessing
import math
import sys
import time

# Allow printing very large integers
sys.set_int_max_str_digits(100000)

# Function to compute factorial
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} computed")
    return result

if __name__ == "__main__":

    numbers = [6000, 500, 959]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print("\nResults:")
    for r in results:
        print(r)

    print("\nTime taken:", end_time - start_time, "seconds")
