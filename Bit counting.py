def countBits(n):
    num = n
    binary = ''
    while (num != 0):
        bit = num % 2
        num = int(num/2)
        binary += str(bit)
    print(binary[::-1]) # [::-1] reverse the string
    return print(numSum(int(binary)))

def numSum(n):
    num = n
    nSum = 0
    for i in str(num):
        nSum += int(i)
        num = num//10
    #print('nSum: ' + str(nSum)) #debug purposes
    return nSum
countBits(1234)
def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
print(countSetBits(1234))

def countBeets(n):
    return bin(n).count("1")
print(countBeets(1234))
10011010010