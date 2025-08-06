def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    array = set(string)
    return (len(array) == len(string))