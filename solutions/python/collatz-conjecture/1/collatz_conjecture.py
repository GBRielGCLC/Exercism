def is_even(number):
    return number % 2 == 0

def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")

    number_steps = 0

    while number != 1:
        number_steps += 1

        if is_even(number):
            number /= 2
        else:
            number = 3 * number + 1

        print(number)

    return number_steps