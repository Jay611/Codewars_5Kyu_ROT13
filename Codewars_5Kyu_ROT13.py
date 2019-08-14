"""
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia,
ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example."
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
"""


def rot13(string):
    message = []
    for c in string:
        if ('N' <= c <= 'Z') or ('n' <= c <= 'z'):
            changed_char = chr(ord(c) - 13)
        elif ('A' <= c <= 'M') or ('a' <= c <= 'm'):
            changed_char = chr(ord(c) + 13)
        else:
            changed_char = c
        message.append(changed_char)
    return "".join(message)


"""
def rot13(message):
  return message.encode('rot13')
"""
"""
def rot13(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c, c) for c in message)
"""
print(rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()))
print(rot13('EBG13 rknzcyr.'))
print(rot13('This is my first ROT13 exercise!'))
