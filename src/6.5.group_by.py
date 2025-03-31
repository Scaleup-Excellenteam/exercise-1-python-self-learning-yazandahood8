def group_by(func, iterable):
    result = {}
    for item in iterable:
        key = func(item)  # Apply the function to the item
        if key not in result:
            result[key] = []  # Initialize a list for the new key if not already present
        result[key].append(item)  # Append the item to the list of the correct key
    return result

# Test the function with if __name__ == "__main__"
if __name__ == "__main__":
    # Example usage: Group words by their lengths
    words = ["hi", "bye", "yo", "try"]
    grouped = group_by(len, words)
    
    print("Grouped by length:", grouped)
