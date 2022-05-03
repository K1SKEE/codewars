'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and
the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should
return [10, -65].'''



def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    if len(arr) > 0:
        for x in arr:
            if x >= 0:
                count += 1
            elif x < 0:
                sum += x
        return [count,sum]
    return arr



print(count_positives_sum_negatives([52, 69, 92, 61, 75, 50, -38, 100, -59, 22, 84, -15, 71, -41, -34, 7, 54, 5, 47, 6]))
print(count_positives_sum_negatives([-38, 89, -99, -16, -96, 39, -49, -84, 31, 52, -15, 65, 78, -41, 67, 67, 31, 100, -15, -22, 65, 45, -78, 94, 19, 95, -95, 32, -62, -35, -21, -26, -64, 83, -47]))

