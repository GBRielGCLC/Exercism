from string import ascii_lowercase

alphabet = list(ascii_lowercase)
reversed_alphabet = list(reversed(alphabet))

def encode(plain_text):
    plain_text = plain_text.replace(' ', '').replace(',', '').replace('.', '')
    encoded_text = []

    for letter in plain_text:
        letter = letter.lower()

        if letter in alphabet:
            encoded_text.append(reversed_alphabet[alphabet.index(letter)])
        else:
            encoded_text.append(letter)

    count_letters = 1
    for index, letter in enumerate(encoded_text):
        if count_letters % 5 == 0 and count_letters != len(plain_text):
            encoded_text.insert(index + 1, ' ')

        if letter in alphabet or letter.isdigit():
            count_letters += 1

    return ''.join(encoded_text)

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ', '').replace(',', '').replace('.', '')
    decoded_text = ''

    for letter in ciphered_text:
        letter = letter.lower()

        if letter.lower() in reversed_alphabet:
            decoded_text += alphabet[reversed_alphabet.index(letter)]

        else:
            decoded_text += letter

    return decoded_text