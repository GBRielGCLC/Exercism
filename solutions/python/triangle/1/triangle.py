def one_side_is_zero(sides):
    if any(side == 0 for side in sides):
        return True
    else:
        return False
def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def remove_repeated_elements(sides):
    return list(set(sides))

def sides_equal(sides, equal_quantity):
    print(sides)
    unrepeated_sizes = remove_repeated_elements(sides)
    print(unrepeated_sizes)

    soma = 1
    if(len(unrepeated_sizes) == len(sides)):
        soma = 0
    if(len(unrepeated_sizes) == 1):
        soma = 1

    count_equal = (len(sides) - len(unrepeated_sizes)) + soma

    print(count_equal, equal_quantity)
    print(count_equal == equal_quantity)

    return count_equal == equal_quantity

def all_sides_equal(sides):
    return len(remove_repeated_elements(sides)) == 1

def equilateral(sides):
    if one_side_is_zero(sides) or not is_valid_triangle(sides):
        return False
    else:
        return all_sides_equal(sides)

def isosceles(sides):
    if one_side_is_zero(sides) or not is_valid_triangle(sides):
        return False
    else:
        return sides_equal(sides, 2) or all_sides_equal(sides)


def scalene(sides):
    if one_side_is_zero(sides) or not is_valid_triangle(sides):
        return False
    else:
        return sides_equal(sides, 0)

sides_equal([1, 2, 3], 3)