'''Definition
Balanced number is the number that * The sum of all digits to the left of
the middle digit(s) and the sum of all digits to the right of the middle digit(s)
are equal*.

Task
Given a number, Find if it is Balanced or not .
Notes
If the number has an odd number of digits then there is only one middle digit,
e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301
has middle digits 3 and 0

The middle digit(s) should not be considered when determining whether a number is
balanced or not, e.g 413023 is a balanced number because the left sum and right
sum are both 5.

Number passed is always Positive .

Return the result as String

Input >> Output Examples
(balanced-num 7) ==> return "Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digit (0)

and the sum of all digits to the right of the middle digit (0) are equal , then
It's Balanced

(balanced-num 295591) ==> return "Not Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (11)

and the sum of all digits to the right of the middle digits (10) are Not equal,
then It's Not Balanced

Note : The middle digit(s) are 55 .

(balanced-num 959) ==> return "Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (9)

and the sum of all digits to the right of the middle digits (9) are equal , then
It's Balanced

Note : The middle digit is 5 .

(balanced-num 27102983) ==> return "Not Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (10)

and the sum of all digits to the right of the middle digits (20) are Not equal,
then It's Not Balanced

Note : The middle digit(s) are 02 .'''


def balanced_num(number):
    oddeven = len(str(number))%2
    mid = len(str(number))//2
    sumleft, sumright = '', ''
    resultleft, resultright = 0, 0
    if len(str(number)) > 2:
        if oddeven == 1:
            sumleft = str(number)[:mid]
            sumright = str(number)[mid+1:]
        elif oddeven == 0:
            sumleft = str(number)[:mid-1]
            sumright = str(number)[mid+1:]
    for i in sumleft:
        for j in sumright:
            resultleft += int(i)
            resultright += int(j)
    if resultleft == resultright:
        return 'Balanced'
    return 'Not Balanced'

print(balanced_num(7))
print(balanced_num(959))
print(balanced_num(13))
print(balanced_num(432))
print(balanced_num(424))
print(balanced_num(1024))
print(balanced_num(66545))
print(balanced_num(295591))
print(balanced_num(1230987))
print(balanced_num(56239814))