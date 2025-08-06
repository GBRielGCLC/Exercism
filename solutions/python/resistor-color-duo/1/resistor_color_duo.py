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

def value(colors):
    color_1, color2, *rest = colors

    index = [colors_list.index(color_1), colors_list.index(color2)]

    return int(''.join(str(i) for i in index))

print(value(["green", "brown", "orange"]))