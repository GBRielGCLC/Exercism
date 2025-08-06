"""Functions to automate Conda airlines ticketing system."""

seat_letters = ['A', 'B', 'C', 'D']

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for i in range(number):
        yield seat_letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    
    for i in range(number):
        row_index = i // 4 + 1
        if row_index >= 13:
            row_index += 1

        letter = seat_letters[i % 4]
        yield f'{row_index}{letter}'

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    
    seats = generate_seats(len(passengers))

    passengers_seats = []
    for passenger in passengers:
        passengers_seats.append((passenger, next(seats)))

    return dict(passengers_seats)

def complete_with_0(code):
    """Complete a 12 character long ticket code.

    :param code: str - a 12 character long ticket code.
    :return: str - a 12 character long ticket code.

    """
    len_0_code = 12 - len(code)
    if len_0_code > 0:
        code = code + ('0' * len_0_code)

    return code

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        code = complete_with_0(f'{seat_number}{flight_id}')
        yield code
