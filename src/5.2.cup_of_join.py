

def join(*lists, sep='-'):
    """
    Combines multiple lists into one, adding a separator between them.
    If no lists are given, returns None.
    """
    if not lists:
        return None
    
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(sep)
    
    return result

if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [4, 5]

    # Test with multiple lists and default separator
    print(join(list1, list2, list3))
    
    # Test with multiple lists and custom separator
    print(join(list1, list2, list3, sep=','))
    
    # Test with no lists
    print(join())