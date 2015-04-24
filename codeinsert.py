import sys

from findfile import find
from parser import parse_insertion
from grablines import grab

"""
takes input file name, outputfile name

reads input line by line, when it sees the magic symbol

parse it to get filename, ext, start, end
find file by filename

if can find file, extract lines[start:end] and appends to output
"""

def codeinsert(input_file, output_file):
    lines = []
    with open(input_file) as input_f:
        for i, line in enumerate(input_f):
            if line.startswith('`@'):
                code_lines = expand_insertion(line, i)
                lines.extend(code_lines)
            else:
                lines.append(line)

    with open(output_file, 'w') as output_f:
        output_f.writelines(lines)

    return lines

def expand_insertion(line, line_no):
    """Given a line that is possibly an insertion command,
    we parse it and try to grab the specified lines from the requested file.
    If we succeed, surround the code block with backticks "```",
    and optionally a file ext that represents the language
    """
    try:
        filename, ext, start, end = parse_insertion(line.strip())
    except Exception as e:
        # parsing fail, return the current line as a list
        raise Exception('Parsing failed at: [%s] %s' % (line_no, line))

    path_to_file = find(filename)

    # we cannot find the file, make some noise
    if path_to_file is None:
        raise Exception('Cannot find file %s at %s' % (filename, line))

    print(path_to_file, start, end)
    lines = grab(path_to_file, start, end)
    print(lines)

    # add the backticks
    lines.insert(0, '```%s\n' % ext)
    lines.append('```\n')

    return lines


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: %s <input_file> <output_file>' % sys.argv[0])
    if len(sys.argv) == 3:
        inserted = codeinsert(sys.argv[1], sys.argv[2])
    if (inserted):
        print(inserted)
