'''Your goal is to return multiplication table for number that is always an integer
from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
P. S. You can use \n in string to jump to the next line.

Note: newlines should be added between rows, but there should be no trailing
newline at the end. If you're unsure about the format, look at the sample tests.'''


def multi_table(number):
    result = ''
    n = 1
    for n in range(1, 11):
        multi = n * number
        result1 = '{0} * {1} = {2}\n'.format(n, number, multi)
        if n == 10:
            result1 = '{0} * {1} = {2}'.format(n, number, multi)
        result += result1
    return result


def multi_table(number):
    result = ''
    for n in range(1, 11):
        multi = n * number
        result1 = f'{n} * {number} = {n*number}\n'
        if n == 10:
            result1 = f'{n} * {number} = {n*number}'
        result += result1
    return result


print(multi_table(5))