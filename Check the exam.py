'''The first input array is the key to the correct answers to an exam, like
["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this
array of answers, giving +4 for each correct answer, -1 for each incorrect answer,
and +0 for each blank answer, represented as an empty string (in C the space
character is used).

If the score < 0, return 0.
For example:
checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
'''

def check_exam(arr1,arr2):
	result = 0
	for i in range(len(arr2)):
		if arr2[i] == arr1[i]:
			result += 4
		elif arr2[i] == '':
			continue
		else:
			result -= 1
	if result < 0:
		return 0
	return result

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))



def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr2)):
        if arr2[i] == arr1[i]:
            result += 4
        if not arr2[i] in arr1[i]:
            result -= 1
        if arr2[i] == '':
            result += 0
    if result < 0:
        return 0
    return result