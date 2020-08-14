'''

                                                WORK IN PROGRESS, TRYING TO LEARN NEW STUFF FOR THIS

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
            return key'''

def validBraces(string):
    braces = {
        '(' : ')',
        '{' : '}',
        '[' : '}'
    }
    get_key = lambda d, v: [key for key,value in d.items() if v == value]
    openBraces = ['(', '{', '{']
    closeBraces = [')', '}', '}']


p1 = "()" # True check
p2 =  "[]{}" # True check
p3 = "([}{])" # False check
p4 = "[(])" # False check
p5 = "(}" # False
p6 = "(({{[[]]}}))" # True check
validBraces(p5)

############### REDUNDANT ###########33
'''if braces.get(i) == string[-(string.index(i) + 1)] or braces.get(i) == string[(string.index(i) + 1)]:
    return print(True)
else:
    return print(False)'''