"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""
characters = "cbaccba\n123A  "
phrase = "aabbccc\n  1A"

def generate_dict(a):
    dict = {}
    for key in a:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    return dict

def generate_phrase():
    dict_phrase = generate_dict(phrase)
    dict_chars = generate_dict(characters)
    for key, value in dict_phrase.items():
        if key not in dict_chars:
            return False
        if value > dict_chars[key]:
            return False
    return True


print(generate_phrase())


