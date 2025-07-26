def count_letters(text):
    """
    Calculate the number of letters in the supplied string.
    Only counts alphabetic characters (a-z, A-Z).
    """
    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count += 1
    return letter_count


# Example usage
if __name__ == "__main__":
    # Test with some sample strings
    test_string = input("Enter a string: ")
    result = count_letters(test_string)
    print(f"Number of letters in '{test_string}': {result}")
