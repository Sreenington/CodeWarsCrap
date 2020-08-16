from collections import Counter
def duplicate_encode(word):
    counts = Counter(word.lower())
    dic = {}
    ans = ''
    for i in word.lower():
        dic[i] = counts[i]
        if dic.get(i) > 1:
            ans += ')'
        else:
            ans += '('
    return (ans)
w1 = "Success"
print(duplicate_encode(w1))