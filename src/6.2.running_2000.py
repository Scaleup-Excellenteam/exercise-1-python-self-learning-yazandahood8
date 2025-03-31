import time

def running_2000(f, *args, **kwargs):
    """
    Measures execution time of function f with given args and kwargs.
    Returns the time in seconds as a float.
    """
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    
    return end_time - start_time


def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    elapsed_time = running_2000(sample_function, 1000000)
    print(f"Execution time: {elapsed_time:.6f} seconds")
