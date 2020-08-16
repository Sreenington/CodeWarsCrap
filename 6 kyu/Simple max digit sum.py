def digitSum(n):
    num = n
    nSum = 0
    for i in str(num):
        nSum += int(i)
        num = num//10
    return nSum

def diglet(n):
    count = len(str(n))
    return count

def solve(n):
    num = n
    count = diglet(n)
    varnum = str(num)

    if diglet(n) == 1:
        print(num)
        return (num)

    if varnum[1] == '9':
        ans = varnum[0] + '8' + '9'*(count-2)
        print((int(ans)))
        return(int(ans))
    elif int(varnum[1]) < 9:
        ans = str(int(varnum[0])-1) + '9'*(count-1)
        if digitSum(int(ans)) <= digitSum(num):
            print(num)
            return (num)
        else:
            print((int(ans)))
            return((int(ans)))
solve(9899999999)