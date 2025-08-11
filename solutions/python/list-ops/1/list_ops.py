def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

def concat(lists):
    result = []

    for item in lists:
        result = append(result, item)

    return result

def filter(function, list):
    result = []

    for item in list:
        if function(item):
            result.append(item)

    return result

def length(list):
    return len(list)

def map(function, list):
    result = []

    for item in list:
        result.append(function(item))

    return result

def foldl(function, list, initial):
    result = initial

    for item in list:
        result = function(result, item)

    return result

def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)

def reverse(list):
    list.reverse()
    return list

print(concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]))