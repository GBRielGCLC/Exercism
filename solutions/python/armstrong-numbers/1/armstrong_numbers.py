def is_armstrong_number(number):
    if not isinstance(number, (int)):
        raise TypeError("Input must be a number")

    char_numbers = []
    for digit in str(number):
        char_numbers.append(int(digit))

    length = len(char_numbers)
    sum = 0
    
    print(char_numbers)

    print("\n-------------------------")
    for char_number in char_numbers:
        print(f"{char_number}^{length} = {pow(char_number, length)}")
        print(f"{sum} + {pow(char_number, length)} = {sum + pow(char_number, length)}")

        print("-------------------------")

        sum += pow(char_number, length)

    print(f"{sum} == {number}")
    return sum == number