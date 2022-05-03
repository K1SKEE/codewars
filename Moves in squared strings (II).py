"""
Moves in squared strings (II)
You are given a string of n lines, each substring being n characters 
long: For example:
s = "abcd\nefgh\nijkl\nmnop"
We will study some transformations of this square of strings.
Clock rotation 180 degrees: rot
rot(s) => "ponm\nlkji\nhgfe\ndcba"
selfie_and_rot(s) (or selfieAndRot or selfie-and-rot) It is initial 
string + string obtained by clock rotation 180 degrees with dots 
interspersed in order (hopefully) to better show the rotation when 
printed.
Task:
Write these two functions rotand selfie_and_rot and high-order function
oper(fct, s) where

fct is the function of one variable f to apply to the string s(fct
will be one of rot, selfie_and_rot)
"""

def rot(strng):
    return '\n'.join(strng[::-1].split('/n'))
def selfie_and_rot(strng):
    s = strng.split('\n')[0]
    dot_str = f'{"."*len(s)}'
    return f'{dot_str}\n'.join(strng.split('\n')) + \
f'{dot_str}\n{dot_str}' + f'\n{dot_str}'.join(strng[::-1].split('\n'))
def oper(fct, s):
    return rot(s) if fct == rot else selfie_and_rot(s)

print(oper(rot, r"fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"))
print(oper(rot, r"rkKv\ncofM\nzXkh\nflCB"))
print(oper(selfie_and_rot, r"xZBV\njsbS\nJcpN\nfVnP"))
print(oper(selfie_and_rot, r"uLcq\nJkuL\nYirX\nnwMB"))