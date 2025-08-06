def raise_unknow_error():
    raise ValueError('unknown operation')

def raise_syntax_error():
    raise ValueError('syntax error')

def is_digit(value):
    return value.lstrip('-').isdigit()

def answer(question):
    if question == 'What is?':
        raise_syntax_error()

    question = question.replace('What is ', '').replace('?', '')
    question = question.replace(' by ', ' ')

    operations = ['plus', 'minus', 'multiplied', 'divided']

    result = 0

    if len(question.split(' ')) == 1:
        return int(question)

    question = question.split(' ')

    if question == 'What is?':
        raise_syntax_error()

    for index, word in enumerate(question):
        isNumber = is_digit(word)

        if not (index + 1 > len(question) - 1):
            if (is_digit(word) and is_digit(question[index + 1])) or ((not is_digit(word) and not is_digit(question[index + 1]))):
                raise_syntax_error()

        if index == 0 and isNumber:
            result = int(word)
            continue

        if not isNumber and word not in operations:
            raise_unknow_error()

        if isNumber:
            operation = question[index - 1]

            number = int(word)

            if operation == 'plus':
                result += number
            elif operation == 'minus':
                result -= number
            elif operation == 'multiplied':
                result *= number
            elif operation == 'divided':
                result /= number

        if not isNumber:

            if word not in operations:
                raise_unknow_error()
            if (index + 1 > len(question) - 1):
                raise_syntax_error()

    return result