"""
Notes:
In the encrypt method, making char_array either a list or string
does not affect the output. However, it was determined that
it would be better to make it a list instead since an str instance
has 76 methods as of python 3.4 versus a list instance' 45.
The assumption is that the less methods, the less memory space used.
It is assumed that processing speed is the same for either instance
type.

Called len(dir(method)) on both str and list.
"""


def decrypt(encrypted_text, n):
    if not (isinstance(encrypted_text, str)):
        return encrypted_text

    char_array = [char for char in encrypted_text]
    integerdiv_half = len(char_array) // 2
    has_extra = False
    iterations = 0

    if (integerdiv_half * 2) < len(char_array):
        has_extra = True

    print("Input to Decrypt:", encrypted_text, "Iter:", n, sep='')
    print(
        "Integer division by two:", integerdiv_half,
        "Has extra?:", has_extra)

    while(iterations < n):
        firsts, seconds = [], []

        seconds = char_array[0: integerdiv_half]
        firsts = char_array[integerdiv_half: (integerdiv_half * 2)]

        if has_extra:
            firsts += [char_array[-1]]

        # print("Firsts:", ''.join(firsts), "Seconds:", ''.join(seconds))

        char_array.clear()

        for index in range(integerdiv_half):
            char_array.append(firsts[index])
            # print(index, ':', firsts[index])

            char_array.append(seconds[index])
            # print(index, ':', seconds[index])

        # char_array += firsts
        # char_array += seconds

        if has_extra:
            char_array += firsts[-1]

        # print("Char array at iter", iterations, "\n:", char_array)
        iterations += 1

    return ''.join(char_array)


def encrypt(text, n):
    if not (isinstance(text, str)):
        return text

    char_array = [char for char in text]
    iterations = 0

    print("Input to Encrypt:`", text, "`. Iter:", n, sep='')

    while(iterations < n):
        firsts, seconds = [], []

        for index in range(len(char_array)):
            if (index & 1 == 0):
                firsts += char_array[index]
            else:
                seconds += char_array[index]

        iterations += 1
        # print('\nSecs:', ''.join(seconds), "\nFirs:", ''.join(firsts))

        char_array.clear()

        char_array += (''.join(seconds))
        char_array += (''.join(firsts))

    return ''.join(char_array)


def test_input(dict_inputs, iterations=5):
    dict_results = {}

    for input_alias, string in dict_inputs.items():
        encrypted_text = encrypt(string, n=iterations)
        decrypted_text = decrypt(encrypted_text, n=iterations)
        dict_results[input_alias] = [string, encrypted_text, decrypted_text]

        print(
            """
            \n* Results for Input Alias: "{}".
            \nIterations:{}
            \nOriginal:\n\t"{}"
            \nEncrypted:\n\t"{}"
            \nDecrypted:\n\t"{}".""".format(
                    input_alias, iterations, string,
                    encrypted_text, decrypted_text
                    )
            )

    return dict_results


even_input = "This is even! End."
odd_input = "This is odd. End."

input_dict = {
    "even": even_input,
    "odd": odd_input
    }

test_input(input_dict)

test_input(input_dict, 8)
