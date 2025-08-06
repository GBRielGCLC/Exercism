def is_valid(isbn):
    isbn = isbn.replace('-','')

    formula_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sum = 0

    if len(isbn) != 10:
        return False

    for index, number in enumerate(isbn):
        if not number.isdigit() and (index != 9 or number != 'X'):
            return False
        elif number == 'X':
            number = 10
        else:
            number = int(number)

        sum += number * formula_numbers[index]

        print(number, sum)

    return sum % 11 == 0