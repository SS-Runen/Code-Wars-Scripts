"""
Input: String containing different "words" separated by spaces.

1. More than one word? Reverse each word and combine first with seconds,
third with fourth and so on.
An odd number of words means last one stays alone but has to be reversed too.

2. Start it again until there's only one word without spaces.

3. Return your result.

Ex:
"abc def" => "cbafed"
"""


def reverse_word(word):
    lst_word = [char for char in word]
    lst_word = reversed(lst_word)
    return ''.join(lst_word)


def reverse_word_manually(word):
    reversed_word = ""

    for index in range((len(word) - 1), -1, -1):
        reversed_word += word[index]

    return reversed_word


def combine_words(lst_words):
    lst_new_words = []

    for index in range(0, len(lst_words), 2):
        try:
            lst_new_words.append(lst_words[index] + lst_words[index + 1])
        except Exception as e:
            lst_new_words.append(lst_words[index])
    return lst_new_words


def reverse_string(string):
    lst_string = string.split(' ')
    print("\n*Function Start\nSplit Input:\n", lst_string)

    while(len(lst_string) != 1):

        for index in range(len(lst_string)):
            lst_string[index] = reverse_word_manually(lst_string[index])

        lst_string = combine_words(lst_string)
        print("Input at length", len(lst_string), ':', lst_string)

    return ''.join(lst_string)


input_2 = "abc def"
input_3 = "abc def hij"
input_6 = "abc def hij abc def hij"

for string in [input_2, input_3, input_6]:
    print("""\nInput: "{}":\n"{}" """.format(string, reverse_string(string)))

# print("""\nInput: "{}":""".format(reverse_string())
# print("""\nInput: "{}":""".format(reverse_string(input_3)))
# print("\nInput:", input_6, ':', reverse_string(input_6))
