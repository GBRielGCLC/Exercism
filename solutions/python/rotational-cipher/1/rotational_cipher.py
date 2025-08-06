from string import ascii_lowercase
from string import ascii_uppercase

alphabet_lower = list(ascii_lowercase)
alphabet_upper = list(ascii_uppercase)

"""
for index, letter in enumerate(alphabet_upper):
    print(str(index) + ': ' + letter)
"""

def find_index(actual_index, key):
    index = actual_index + key

    if (index > 25):
        index = index - 26

    """
    print('actual_index: ' + str(actual_index))
    print('key: ' + str(key))
    print('index: ' + str(index))
    """
    return index

def rotate(text, key):
    text = text

    shifted_text = ''

    for char in text:
        if char.isupper():
            shifted_text += alphabet_upper[find_index(alphabet_upper.index(char), key)]
        elif char.islower():
            shifted_text += alphabet_lower[find_index(alphabet_lower.index(char), key)]
        else:
            shifted_text += char

    return shifted_text