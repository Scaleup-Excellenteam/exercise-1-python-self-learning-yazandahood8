def interleave(*iterables):
    """
    Function to interleave multiple iterables into a single list.
    This version returns the result as a list.
    """
    result = []
    # Find the length of the largest iterable
    max_len = max(len(iterable) for iterable in iterables)
    
    # Interleave the elements from each iterable
    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):  # Only append if there's an element at this position
                result.append(iterable[i])
    
    return result

def interleave_generator(*iterables):
    """
    Generator version of the interleave function.
    Yields elements from the iterables one by one.
    """
    # Find the length of the largest iterable
    max_len = max(len(iterable) for iterable in iterables)
    
    # Interleave the elements from each iterable
    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):  # Only yield if there's an element at this position
                yield iterable[i]
                
                
if __name__ == "__main__":
    # Test data
    iterable1 = [1, 3, 5]
    iterable2 = ['a', 'b', 'c', 'd']
    iterable3 = ['A', 'B']

    # Test interleave function
    interleaved_list = interleave(iterable1, iterable2, iterable3)
    print("Interleaved List:", interleaved_list)

    # Test interleave_generator function
    interleaved_gen = interleave_generator(iterable1, iterable2, iterable3)
    print("Interleaved Generator:", list(interleaved_gen))