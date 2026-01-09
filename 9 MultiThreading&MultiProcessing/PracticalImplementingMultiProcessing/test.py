##Threads: “I want to do many tasks that mostly wait (I/O), without freezing.”
#Processes: “I want to use multiple CPU cores for real parallel computation.”

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    p1.start()
    p2.start()

    # ✅ wait for BOTH processes
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print("Finished in:", finished_time)
