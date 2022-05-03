"""Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:

the first two digits of 1176 form a prime.
the first two digits of the square 1382976 also form a prime.
the last two digits of 1176 and 1382976 are the same.
Given two numbers representing a range (a, b), how many numbers satisfy this property within that range? (a <= n < b)

Example
solve(2, 1200) = 1, because only 1176 satisfies this property within the range 2 <= n < 1200. See test cases for more
examples.
The upper bound for the range will not exceed 1,000,000.

Good luck!"""

def solve(a, b):
    result = 0
    for x in range(a, b):
        if len(str(x)) >= 4:
            op = str(x)[:2]
            lastx = str(x)[-1:-2]

            for i in range(2, int(op)):
                if int(op) % i == 0:
                    break
            else:
                squared = str(x * x)[:2]
                lastsquared = str(squared)[-1:-2]
                for n in range(2, int(squared)):
                    if int(squared) % n == 0:
                        break
                else:
                    if lastx==lastsquared:
                        result += 1
    return result

print(solve(2, 1200))
print(solve(1176, 1200))
print(solve(2, 100000))
print(solve(2, 1000000))
print(solve(100000 ,1000000))