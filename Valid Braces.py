'''

                                                WORK IN PROGRESS, DIDNT SOLVE YET

#################################
###### P5 CASE DOESN'T WORK #####
#################################

def validBraces(string):
    braces = {
        '(' : ')',
        '{' : '}',
        '[' : '}'
    }
    openBraces = ['(', '{', '{']
    closeBraces = [')', '}', '}']
    for i in string:
        if i in closeBraces and (string.index(i) < string.find(get_key(i, braces))):
            print('caught')
            return print(False)
        else:
            print('whoops')

        if i in openBraces and (string.index(i) + string.rfind(braces.get(i), -1, 0))%2 == 0:
            return print(False)
        else:
            print('Ooffed')
    return print(True)


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key    '''

def validBraces(string):
    braces = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    check = []
    for i in string:
        if i in braces:
            check.append(braces[i])  # appends closing brackets in order they are supposed to appear
            continue
        if i == check.pop():  # checks if closing brackets appears in the order specified in the list
            continue
        return print(False)
    print(check)
    return print(True)


# Test values
p1 = "()"  # True passes
p2 = "[]{}"  # True passes
p3 = "([}{])"  # False passes
p4 = "[(])"  # False passes
p5 = "(}"  # False passes
p6 = "(({{[[]]}}))"  # True passes
p7 = "(((({{"  # False fails
validBraces(p6)

############### REDUNDANT ###########33
'''if braces.get(i) == string[-(string.index(i) + 1)] or braces.get(i) == string[(string.index(i) + 1)]:
    return print(True)
else:
    return print(False)'''
