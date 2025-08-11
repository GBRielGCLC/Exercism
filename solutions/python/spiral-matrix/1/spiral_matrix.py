def spiral_matrix(size):
    if size <= 0:
        return []

    number_of_spaces = len(str(size ** 2))
    result = [[0] * size for _ in range(size)]

    top, bottom = 0, size - 1
    left, right = 0, size - 1
    num = 1

    while left <= right and top <= bottom:
        # Esquerda → Direita
        for col in range(left, right + 1):
            result[top][col] = num
            num += 1
        top += 1

        # Cima ↓ Baixo
        for row in range(top, bottom + 1):
            result[row][right] = num
            num += 1
        right -= 1

        # Direita ← Esquerda (se ainda houver linha para percorrer)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result[bottom][col] = num
                num += 1
            bottom -= 1

        # Baixo ↑ Cima (se ainda houver coluna para percorrer)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result[row][left] = num
                num += 1
            left += 1

    # Formatar resultado como string
    string_result = ""
    for row in result:
        string_result += " ".join(
            ' ' * (number_of_spaces - len(str(v))) + str(v)
            for v in row
        ) + "\n"

    return result

print(spiral_matrix(4))