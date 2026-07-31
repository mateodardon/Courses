# Function decorator that times execution
from time import time

def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper

@timer
def prueba():
    return [number**3 for number in range(20)]

print(prueba())
