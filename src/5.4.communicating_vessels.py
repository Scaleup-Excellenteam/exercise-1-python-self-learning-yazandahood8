def interleave(*iterables):
    """
    Function to interleave multiple iterables into a single list.
    This version returns the result as a list.
    """
    result = []
    if not iterables:
        return result

    max_len = max(len(iterable) for iterable in iterables)
    
    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):
                result.append(iterable[i])
    
    return result


def generator_interleave(*iterables):
    """
    Generator version of the interleave function.
    Yields elements from the iterables one by one.
    """
    if not iterables:
        return
    max_len = max(len(iterable) for iterable in iterables)
    
    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):
                yield iterable[i]


if __name__ == "__main__":
    iterable1 = [1, 3, 5]
    iterable2 = ['a', 'b', 'c', 'd']
    iterable3 = ['A', 'B']

    print("Interleaved List:", interleave(iterable1, iterable2, iterable3))
    print("Interleaved Generator:", list(generator_interleave(iterable1, iterable2, iterable3)))
