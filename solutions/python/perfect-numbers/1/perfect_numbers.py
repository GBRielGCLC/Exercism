def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if isinstance(number, int) == False or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0

    for index in range(1, number):
        if number % index == 0:
            print(str(aliquot_sum) + " + " + str(index) + " = " + str(aliquot_sum + index))
            aliquot_sum += index

    if aliquot_sum == number:
        return "perfect"
    elif number < aliquot_sum:
        return "abundant"
    else:
        return "deficient"