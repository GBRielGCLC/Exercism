def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    sentence = ''.join(x for x in sentence if x.isalpha()).lower()
    hasEvery = True

    for letter in alphabet:
        if not letter in sentence:
            hasEvery = False

    return hasEvery