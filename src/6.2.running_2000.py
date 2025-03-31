

import time

def timer(f, *args, **kwargs):
    """
    This function measures the execution time of the provided function f with its arguments.
    """
    start_time = time.time()  # Record the start time
    f(*args, **kwargs)  # Call the function f with the provided arguments
    end_time = time.time()  # Record the end time
    
    return end_time - start_time  # Return the time difference


def sample_function(n):
     total = 0
     for i in range(n):
         total += i
     return total

if __name__ == "__main__":
   
    # Time the execution of sample_function
    elapsed_time = timer(sample_function, 1000000)
    print(f"Execution time: {elapsed_time:.6f} seconds")