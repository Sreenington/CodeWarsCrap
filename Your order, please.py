p = "is2 Thi1s T4est 3a"
def order(phrase):
    arr = phrase.split()
    arr.sort(key=lambda p: check_int(p))
    return print(' '.join(arr))

def check_int(phrase):
    for elem in phrase:
        for letter in elem:
            if letter.isnumeric():
                return letter
    pass

'''Whack '''
def orderz(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: str(filter(str.isdigit, x))))

'''HOLY SHIT WHACK '''
def orderzz(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

