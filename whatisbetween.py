def between(a,b):
    if a < b:
        b += 1
        f = [i for i in range(a, b)]
        return f

'''
Complete the function that takes two integers (a, b, where a < b) and return 
an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
'''