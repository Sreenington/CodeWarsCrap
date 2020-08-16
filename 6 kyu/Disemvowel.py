'''

Removes vowel from string.

'''

vowels = ['a', 'e', 'i', 'o', 'u']
def disemvowel(string):
    new_string = string.lower()
    for i in string:
        if i in vowels:
            new_string = {string.replace(i, '') for i in string}
    return print(new_string)

disemvowel('Hahah Lolol')