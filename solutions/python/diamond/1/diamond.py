from string import ascii_uppercase as alphabet
from itertools import islice

alphabet = list(alphabet)
space_char = " "

def build_line(i, alphabet_index):
    letter = alphabet[i]

    if i == 0:
        spaces = space_char * (alphabet_index)
        return spaces + letter + spaces
    else:
        side_spaces = space_char * (alphabet_index - i)
        middle_spaces = space_char * (2 * i - 1)

        return side_spaces + letter + middle_spaces + letter + side_spaces

def rows(letter):
    letter = letter.upper()
    alphabet_index = alphabet.index(letter)

    result = [build_line(i, alphabet_index) for i in range(alphabet_index + 1)]
    result += [build_line(i, alphabet_index) for i in range(alphabet_index - 1, -1, -1)]
 
    return result