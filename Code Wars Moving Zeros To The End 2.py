

def move_zeroes(array):
    new_array = []

    for number in array:
        if number != 0 or (isinstance(number, bool)):
            new_array.append(number)

    diff = len(array) - len(new_array)
    for i in range(diff):
        new_array.append(0)

    return new_array


second_test = [
    False, 9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0,
    3, 0, 1, 9, 0, 0, 0, 0, 9
    ]
backup = second_test.copy()

second_test = move_zeroes(second_test)

print(backup)
print(second_test)
