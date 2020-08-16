def to_camel_case(text):
    text = (text.replace('_', '-')).split('-')
    text = ''.join(a.capitalize() if text.index(a) > 0 else a for a in text)
    print(text)


p1 = "the-stealth-warrior"
p2 = "The_Stealth_Warrior"
to_camel_case(p2)