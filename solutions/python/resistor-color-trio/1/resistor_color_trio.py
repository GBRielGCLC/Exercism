colors_list = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
]

def label(colors):
    color_1, color2, color_3, *rest = colors

    index = [colors_list.index(color_1), colors_list.index(color2)]
    index = int(''.join(str(i) for i in index))

    power = colors_list.index(color_3)

    index = index * (10 ** power)

    ohms = ' ohms'
    divisor = 1
    
    print(power)

    if power >= 9:
        divisor = 10 ** 9
        ohms = ' gigaohms'
    elif power >= 6:
        divisor = 10 ** 6
        ohms = ' megaohms'
    elif power >= 2:
        divisor = 10 ** 3
        ohms = ' kiloohms'

    return str(index//divisor) + ohms

print(label(["red", "black", "red"]))