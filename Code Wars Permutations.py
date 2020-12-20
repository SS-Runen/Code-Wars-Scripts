import random


def rotate_right(A, n_times=1, return_string=False):
    if(len(A) == 0):
        return A
    if not (isinstance(A, list)):
        A = list(A)

    backup = [n for n in A]
    iterations = 0

    while(iterations < n_times):
        array_length = len(backup)
        for i in range(1, array_length):
            A[i] = backup[i - 1]

        A[0] = backup[-1]
        backup = A.copy()
        # print(iterations + 1, ':', A)
        iterations += 1

    return A

# def permutations(string:str):
    
#     counter = len(string)
#     lst_indexes = list(range(counter))
#     dict_combinations = dict()

#     while counter > 1:
#         lst_indexes = list(range(counter))

#     return None


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    

def permutations_b(string:str):
    dict_combinations = dict()
    lst_indexes = list(range(len(string)))
    dict_unique_combinations = dict()

    string_length = len(string)
    r = string_length
    possible_index_index_permutations = factorial(string_length) / factorial(string_length - (r-1))
    possible_index_index_permutations += factorial(string_length)
    
    index_index_permutations = 0
    while index_index_permutations < possible_index_index_permutations:
        random.shuffle(lst_indexes)
        index_permutation = "".join([str(integer) for integer in lst_indexes])
        if index_permutation not in dict_combinations:
            dict_combinations[index_permutation] = None
            str_permutation = "".join([string[index] for index in lst_indexes])
            if str_permutation not in dict_unique_combinations:
                dict_unique_combinations[str_permutation] = None
    
    return list(dict_unique_combinations.keys())


def permutations_c(string:str):
    dict_combinations = dict()
    lst_indexes = list(range(len(string)))
    dict_unique_combinations = dict()

    repeated_combinations = 0
    while repeated_combinations < (2 ** 20):
        random.shuffle(lst_indexes)
        pseudorandom_seed = random.randint(1, 105)
        random.seed(pseudorandom_seed)
        index_permutation = "".join([str(integer) for integer in lst_indexes])
        if index_permutation not in dict_combinations:
            dict_combinations[index_permutation] = None
            str_permutation = "".join([string[index] for index in lst_indexes])
            if str_permutation not in dict_unique_combinations:
                dict_unique_combinations[str_permutation] = None
        else:
            repeated_combinations += 1
    
    return list(dict_unique_combinations.keys())
