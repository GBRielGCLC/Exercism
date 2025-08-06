def is_paired(input_string):
    stack = []
    matching_bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in input_string:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack.pop() != matching_bracket[char]:
                return False

    return not stack