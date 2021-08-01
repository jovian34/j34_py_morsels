from argparse import ArgumentParser, FileType


def escape(line_text):
    output = ""
    for char in line_text:
        if ord(char) <= 127:
            output = f"{output}{char}"
        elif ord(char) <= 65536:
            output = rf"{output}\u{hex(ord(char))[2:]:0>4}"
        else:
            output = rf"{output}\U{hex(ord(char))[2:]:0>8}"
    return output


def escape_html(line_text):
    output = ""
    for char in line_text:
        if ord(char) <= 127:
            output = f"{output}{char}"
        elif ord(char) <= 65536:
            output = rf"{output}&#{hex(ord(char))[1:]};"
        else:
            output = rf"{output}&#{hex(ord(char))[1:]};"
    return output


def escape_file(text_file):
    contents = text_file.read()
    return ''.join(
        escape(c)
        for c in contents
    )


def escape_file_html(text_file):
    contents = text_file.read()
    return ''.join(
        escape_html(c)
        for c in contents
    )


parser = ArgumentParser(description='Process UTF-8 text')
parser.add_argument("--style", help="allow customization of the output style")
parser.add_argument("file", help="text file",
                    type=FileType('rt'))
args = parser.parse_args()
# filename = args.filename
style = 'default'
if args.style:
    style = args.style
result = ''

'''
with open(filename, mode='rt', encoding='utf-8') as text:
    for line in text.read():
        if style == 'default':
            result += f"{escape(line)}"
        elif style == 'html':
            result += f"{escape_html(line)}"
'''

if style == 'default':
    result += f"{escape_file(args.file)}"
elif style == 'html':
    result += f"{escape_file_html(args.file)}"
print(result, end='')



