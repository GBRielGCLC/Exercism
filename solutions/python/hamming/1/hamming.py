def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    diference_counter = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            diference_counter += 1

    return diference_counter
