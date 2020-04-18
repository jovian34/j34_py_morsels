import sys


def escape(line_text):
    output = ""
    for char in line_text:
        if ord(char) == 10:
            output = ''
        elif ord(char) <= 127:
            output = f"{output}{char}"
        elif ord(char) <= 65536:
            output = rf"{output}\u{hex(ord(char))[2:]:0>4}"
        else:
            output = rf"{output}\U{hex(ord(char))[2:]:0>8}"
    return output


filename = sys.argv[1]
result = ''

with open(filename, mode='rt', encoding='utf-8') as text:
    for line in text.read():
        result += escape(line)

print(result, end='')



