def flatten(iterable):
    flattened = []
    for item in iterable:
        if item is None:
            continue

        if isinstance(item, list):
            flattened += flatten(item)
        else:
            flattened.append(item)

    return flattened