def reverse(text):
    reversed_text = ""
    text_length = len(text)

    for index in range(text_length-1, -1, -1):
        reversed_text += text[index]

    return reversed_text