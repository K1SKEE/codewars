'''Complete the solution so that it reverses all of the words within the string
passed in.
Example:
"The greatest victory is that which requires no battle" --> "battle no requires
which that is victory greatest The"
'''

def reverse_words(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)

reverse_words("hello world!")