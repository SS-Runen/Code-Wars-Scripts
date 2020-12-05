input = [5, 3, 2, 8, 1, 4]
print("Input: ", input)


def sort_array(source_array):
    dict_odd_numbers = {}
    for index in range(len(source_array)):
        if (source_array[index] % 2) != 0:
            dict_odd_numbers[index] = source_array[index]
    """
    Try sort using both method and some sorting algorithm,
    probably Bubble Sort due to lack of information.
    """
    keys = list(dict_odd_numbers.keys())
    print("Odd keys' Indexes:", keys, sep='')

    while True:
        found_unordered = False

        for index in range(len(keys) - 1):
            one = dict_odd_numbers[keys[index]]
            two = dict_odd_numbers[keys[index + 1]]

            if one > two and one != 0 and two != 0:
                dict_odd_numbers[keys[index]] = two
                dict_odd_numbers[keys[index + 1]] = one
                found_unordered = True
        if not found_unordered:
            break
    # Return numbers in order to list.
    for index, value in dict_odd_numbers.items():
        source_array[index] = value

    return source_array


print("Output:", sort_array(input))
