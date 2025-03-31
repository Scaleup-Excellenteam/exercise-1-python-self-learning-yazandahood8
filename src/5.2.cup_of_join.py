def cup_of_join(*lists, sep=None):
    """
    Combines multiple lists into one.
    If 'sep' is given, adds it after each list (even if empty), including after the last.
    If no lists are given, returns None.
    """
    if not lists:
        return None

    result = []

    for lst in lists:
        result.extend(lst)
        if sep is not None:
            result.append(sep)

    return result


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [4, 5]

    print(cup_of_join(list1, list2, list3))
    print(cup_of_join(list1, list2, list3, sep=','))
    print(cup_of_join())
