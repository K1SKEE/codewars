'''
You will be given an array a and a value x. All you need to do is check whether the
provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.
'''

def check(seq, elem):
	if elem in seq:
		print('True')
		return True
	if not elem in seq:
		print('False')
		return False
    
check([66, 101], 66)
check([78, 117, 110, 99, 104, 117, 107, 115], 8)
check(["anyone", "want", "to", "hire", "me?"], "me?")
check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)