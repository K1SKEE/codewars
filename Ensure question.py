'''Given a string, write a function that returns the string with a question
mark ("?") appends to the end, unless the original string ends with a question
mark, in which case, returns the original string.
For example (Input --> Output)
"Yes" --> "Yes?" 
"No?" --> "No?"
'''

def ensure_question(s):
    if s.endswith('?'):
        return s
    else:
        return s.replace(s, s+'?')

ensure_question("")
ensure_question("Yes")
ensure_question("No?")
ensure_question("Well????")