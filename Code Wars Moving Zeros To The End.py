def move_zeros(array):
    targets = []
    for ctr in range(len(array) - 1, -1, -1):
        if (array[ctr] == 0) and (not isinstance(array[ctr], bool)):
            targets += [ctr]
    print(targets)

    """
    targets.reverse()
    for num in range( len(targets) - 1, -1, -1):
        del array[ targets[num] ]
        array.append(0)
    """

    for num in range(len(targets)):
        del array[targets[num]]
        array.append(0)

    return array


second_test = [
    False, 9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3,
    0, 1, 9, 0, 0, 0, 0, 9
        ]
backup = second_test.copy()

move_zeros(second_test)

print(backup)
print(second_test)
