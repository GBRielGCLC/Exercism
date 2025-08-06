"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value = 0
    
    if (card == 'J' or card == 'Q' or card == 'K'):
        value = 10
    elif card == 'A':
        value = 1
    else:
        value = int(card)

    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_one_value < card_two_value:
        return card_two
    else:
        return (card_one, card_two)

def has_an_ace(card_one, card_two):
    """Determine if the hand has an ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - does the hand contain an ace card?

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    return (card_one == 'A' or card_two == 'A')

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ace_value = 0

    if has_an_ace(card_one, card_two):
        ace_value = 1
    else:
        card_one_value = value_of_card(card_one)
        card_two_value = value_of_card(card_two)

        print (card_one_value , card_two_value)

        if card_one_value + card_two_value + 11 > 21:
            ace_value = 1
        else: 
            ace_value = 11

    return ace_value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    has_ace = has_an_ace(card_one, card_two)

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    
    if(has_ace and (card_one_value == 10 or card_two_value == 10)):
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    pairs = ['K', 'Q']

    if (card_one_value == card_two_value or (card_one in pairs and card_two in pairs)):
        return True

    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if(card_one == 'A'):
        card_one_value = value_of_ace(card_one, card_two)
    if(card_two == 'A'):
        card_two_value = value_of_ace(card_one, card_two)

    card_value_sum = card_one_value + card_two_value

    if (card_value_sum in (9, 10, 11)):
        return True

    return False