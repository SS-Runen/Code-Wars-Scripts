

def encode(string):
    lst_binary = []
    for char in string:
        integer = ord(char)
        str_binary = bin(integer)
        lst_binary.append(str_binary)
    
    for index in range(len(lst_binary)):
        str_8bit = (lst_binary[index])[2:]
        
        for n in range(8 - len(str_8bit)):
            str_8bit = list(str_8bit)
            str_8bit.insert(0, '0')
            str_8bit = "".join(str_8bit)
        
        lst_binary[index] = str_8bit
    
    for index in range(len(lst_binary)):
        str_8bit = lst_binary[index]
        lst_triplebits = []
        for char in str_8bit:
            lst_triplebits.append(3 * char)
        
        lst_binary[index] = "".join(lst_triplebits)

    return ''.join(lst_binary)


def decode(bits):
    lst_bits = []
    lst_chars = []

    start_index = 0
    for triplet_index in range(3, len(bits), 3):
        triplet = bits[start_index:triplet_index]
        if triplet.count('1') > triplet.count('0'):
            lst_bits.append('1')
        else:
            lst_bits.append('0')                

        start_index += 3

    start_index = 0
    closest_multiple = ((len(lst_bits) // 8) + 1) * 8
    for eightbit_index in range(8, closest_multiple, 8):
        bits = ""
        if eightbit_index < len(lst_bits):
            bits = "".join(lst_bits[start_index:eightbit_index])
        else:
            bits = "".join(lst_bits[start_index: ])
        
        char = chr(int(bits, 2))
        lst_chars.append(char)

        start_index += 8

    return "".join(lst_chars)


def decode(bits):
    lst_bits = []
    lst_chars = []
    dict_ascii = {}
    str_alnum = r"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !.,{}'("):;\?$#@%&*"""
    dict_ascii = {ord(letter): letter for letter in str_alnum}

    start_index = 0
    for triplet_index in range(3, len(bits), 3):
        triplet = bits[start_index:triplet_index]
        if triplet.count('1') > triplet.count('0'):
            lst_bits.append('1')
        else:
            lst_bits.append('0')                

        start_index += 3

    start_index = 0
    closest_triplet_multiple = ((len(lst_bits) // 8) + 1) * 8
    for eightbit_index in range(8, closest_triplet_multiple, 8):
        bits = ""
        if eightbit_index < len(lst_bits):
            bits = "".join(lst_bits[start_index:eightbit_index])
        else:
            bits = "".join(lst_bits[start_index: ])

        char = dict_ascii[int(bits, 2)]
        lst_chars.append(char)

        start_index += 8

    return "".join(lst_chars)