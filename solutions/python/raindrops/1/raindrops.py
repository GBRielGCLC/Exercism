def convert(number):
    if type(number) != int:
        return "Error: The input must be an integer"

    msg = ""

    if (number % 3 == 0):
        msg += 'Pling'

    if (number % 5 == 0):
        msg += 'Plang'

    if (number % 7 == 0):
        msg += 'Plong'

    if msg == "":
        msg = str(number)

    return msg