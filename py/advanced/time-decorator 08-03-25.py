"""
📘 Mini-Project: Timing Function Execution

We'll build a decorator called @timer to measure execution time of functions!
🚩 Project Requirements:

    Implement a @timer decorator.
    Display the execution time in seconds.
    Test with different functions (e.g., factorial, sorting).
    """

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end-start}")
    return wrapper

@timer
def sum(n):
    s=0
    for i in range(n):
        s+=i
    return s

sum(100000000)