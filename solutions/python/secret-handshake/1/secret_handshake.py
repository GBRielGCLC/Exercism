handshakes = {
    '10000': 'Reverse the order of the operations in the secret handshake.',
    '01000': 'jump',
    '00100': 'close your eyes',
    '00010': 'double blink',
    '00001': 'wink',
}

def commands(binary_str):
    handshakes_keys = list(handshakes.keys())

    actions = []

    for i in range(4, -1, -1):


        if binary_str[i] == '1':

            print(handshakes[handshakes_keys[i]])
            print(i)
            print('=======================')

            if(i == 0):
                actions.reverse()
            else:
                actions.append(handshakes[handshakes_keys[i]])
        if(i == 0):
            break

    return actions