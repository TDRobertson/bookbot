"""
This function returns the number of words in the text.
"""
def get_words(text):
    words = []
    for word in text.split():
        words.append(word)
    return len(words)

"""
This function returns a dictionary with the number of times a character appears in the text.
The key is the character and the value is the number of times it appears.
The character is converted to lowercase to avoid case sensitivity.
"""
def get_num_chars(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

"""
This function returns a sorted list of characters and their counts.
The characters are sorted by their count in descending order.
The non-alphabetic characters are removed.
"""
def sorted_dict(num_chars):
    sorted_chars = sorted(num_chars.items(), key=lambda x: x[1], reverse=True)
    # remove non-alphabetic characters
    sorted_chars = [char for char in sorted_chars if char[0].isalpha()]
    return sorted_chars