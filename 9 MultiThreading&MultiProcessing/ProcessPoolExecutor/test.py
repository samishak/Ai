from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"square: {number * number}"

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5,56,3,2,66,61,2]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)
