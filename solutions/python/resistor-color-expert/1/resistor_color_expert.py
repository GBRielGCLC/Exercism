# For some reason the result is not rounding down in exercism

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

tolerance_dict = {
    'grey': '0.05%',
    'violet': '0.1%',
    'blue': '0.25%',
    'green': '0.5%',
    'brown': '1%',
    'red': '2%',
    'gold': '5%',
    'silver': '10%',
}

def resistor_label(colors):

    if(len(colors) < 2):
        return '0 ohms'

    *colors, multiplayer, tolerance  = colors
    
    colors = [colors_list.index(color) for color in colors]

    multiplayer = colors_list.index(multiplayer)
    multiplayer = 10 ** multiplayer

    tolerance = tolerance_dict[tolerance]

    ohms = 'ohms'

    index = int(''.join(str(i) for i in colors)) * multiplayer

    if index >= 1000000:
        ohms = 'megaohms'
        index /= 1000000
    elif index >= 1000:
        ohms = 'kiloohms'
        index /= 1000

    if isinstance(index, float) and index.is_integer():
        index = int(index)

    return f'{index} {ohms} ±{tolerance}'