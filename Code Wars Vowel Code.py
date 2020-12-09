"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
"""


def encode(string:str):
    new_string = ""
    dict_vowel_table = {
        'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5
    }

    for char in string:
        if char in dict_vowel_table:
            new_string += str(dict_vowel_table[char])
        else:
            new_string += char
    
    return new_string


def decode(string:str):
    new_string = ""
    lst_vowels = ['a', 'e', 'i', 'o', 'u']

    for char in string:
        if char.isdigit():
            index = int(char)
            new_string += lst_vowels[index - 1]
        else:
            new_string += char
    
    return new_string


def main():
    print(f"Encode `hi there`:\n{encode('hi there')}")
    print(f"Decode `h3 th2r2`\n{decode('h3 th2r2')}")

    return None


if __name__ == "__main__":
    main()