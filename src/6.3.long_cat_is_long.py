
def count_words(text):
    # Remove non-letter characters and split the text into words
    cleaned_text = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in text)
    words = cleaned_text.lower().split()

    # Use dictionary comprehension to count word lengths
    word_lengths = {word: len(word) for word in words}

    return word_lengths

# Test the function with if __name__ == "__main__"
if __name__ == "__main__":
    sample_text = """
   Hello World
    """
    
    result = count_words(sample_text)
    print("Word lengths:", result)
