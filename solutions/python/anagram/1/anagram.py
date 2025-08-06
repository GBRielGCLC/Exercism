def find_anagrams(word, candidates):
    anagrams = []
    
    for c in candidates:
        if sorted(word.lower()) == sorted(c.lower()) and word.lower() != c.lower():
            anagrams.append(c)

    return anagrams