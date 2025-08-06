def is_vowel(letter):
    return letter.lower() in "aeiou"

def has_consonant_sequenced_byQU(word):
    if(word.startswith("qu")):
        return True

    if "qu" not in word:
        return False

    index = word.find("qu")
    return index > 0 and not is_vowel(word[index - 1])

def has_consonant_sequenced_by_Y(word):
    if "y" not in word:
        return False
    index = word.find("y")
    return index > 0 and all(not is_vowel(c) for c in word[:index])

def rule_1(word):
    return word + "ay"

def rule_2(word):
    for i, letter in enumerate(word):
        if is_vowel(letter):
            return word[i:] + word[:i] + "ay"
    return word + "ay"

def rule_3(word):
    for i in range(len(word) - 1):
        if word[i] == 'q' and word[i + 1] == 'u':
            return word[i + 2:] + word[:i + 2] + "ay"
    return word + "ay"

def rule_4(word):
    for i, letter in enumerate(word):
        if letter == 'y':
            return word[i:] + word[:i] + "ay"
    return word + "ay"

def check_rules(text):

    if text.startswith(("xr", "yt")) or is_vowel(text[0]):
        return rule_1(text)

    elif has_consonant_sequenced_byQU(text):
        return rule_3(text)

    elif has_consonant_sequenced_by_Y(text):
        return rule_4(text)

    elif not is_vowel(text[0]):
        return rule_2(text)

    return rule_1(text)

def translate(text):
    splited_text = text.split(" ")
    
    if len(splited_text) == 1:
        return check_rules(text)

    phrase = []
    for word in splited_text:
        phrase.append(check_rules(word))
        
    return " ".join(phrase)