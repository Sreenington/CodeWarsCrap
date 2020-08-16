def generate_hashtag(s):
    s = (s).split(' ')
    s = ''.join(a.capitalize() if s.index(a) >= 0 else a for a in s)

    if len(s) > 140 or len(s) == 0:
        return False
    return '#' + s


'''
A simpler solution
'''


def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


# TEST CASES
s1 = ''  # False passed
s2 = 'Do We have A Hashtag'  # #DoWeHaveAHashtag passed
s3 = 'c i n'  # #CIN passed
s4 = 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'  # False passed
print(generate_hashtag(s4))
