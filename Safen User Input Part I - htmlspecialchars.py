'''Safen User Input Part I - htmlspecialchars
Mission
Your mission is to implement a function htmlspecialchars() that converts the
following potentially harmful characters:

< --> &lt;
> --> &gt;
" --> &quot;
& --> &amp;
Good luck :D

Extension
If you are an experienced Javascript programmer, try shortening your code as much
as possible and optimise it to minimise run time. Experienced programmers should be
able to complete this exercise in one line of code.
'''

def html_special_chars(data):
    chars = '<', '>', '"', '&'
    for chars in data:
        if chars == '<':
            data = data.replace('<', '&lt;')
        if chars == '>':
            data = data.replace('>', '&gt;')
        if chars == '"':
            data = data.replace('"', '&quot;')
        if chars == '&':
            data = data.replace('&', '&amp;')
        if '&amp;gt;' in data:
            data = data.replace('&amp;gt;', '&gt;')
        if '&amp;lt;' in data:
            data = data.replace('&amp;lt;', '&lt;')
        if '&amp;quot;' in data:
            data = data.replace('&amp;quot;', '&quot;')
        if '&amp;amp;' in data:
            data = data.replace('&amp;amp;', '&amp;')
    return data


print(html_special_chars('How was "The Matrix"?  Did you like it?'))
print(html_special_chars("<script>alert('Website Hacked!');</script>"))
print(html_special_chars("<h2>Hello World</h2>"))
print(html_special_chars("Hello, how would you & I fare?"))
print(html_special_chars('j>&<AS'))
