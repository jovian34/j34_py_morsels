import sys

def escape(line_text):
    output = ""
    for char in line_text:
        if ord(char) <= 127:
            output = f"{output}{char}"
        else:
            output = f"{output}\\{char.encode('unicode-escape')}"
    return output

filename = sys.argv[0]

with open(filename) as text:
    for line in text:
        escape(line)