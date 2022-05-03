def solve(a, b):
    result = 0
    is_prime = True
    for x in range(a, b + 1):
        strx = str(x)[:2]
        strsquared = str(x * x)[:2]
        lastx = str(x)[-1:-2]
        lastsquared = str(strsquared)[-1:-2]
        for i in range(2, int(strx)):
            if int(strx) % i == 0:
                is_prime = False
                break
            if is_prime == 'True':
                for n in range(2, int(strsquared)):
                    if int(strsquared) % n == 0:
                        is_prime = False
                        break
        if is_prime is True:
            if lastx == lastsquared:
                result += 1
    return result


print(solve(2, 1200))
print(solve(1176, 1200))
print(solve(2, 100000))
print(solve(2, 1000000))
print(solve(100000, 1000000))
