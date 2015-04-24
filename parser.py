import sys

def parse_insertion(string):
    """Given a string, extract the bits we are interested in,
    namely the filename, file extension, start line number and
    end line number.

    The end line number is optional, and will be set to the start number
    if not given.

    Returns a tuple (filename, ext, start_line, end_line)
    """
    # string should look something like this
    # ``@filename.ext#start-end
    if not string.startswith('`@'):
        raise Exception('Does not start with "`@"')

    # string now looks like this filename.ext#start-end
    string = string[2:]

    if string.endswith('`'):
        string = string[:-1]

    if '#' not in string:
        raise Exception('Line numbers not given')

    filename, line_nums = string.split('#')

    if not filename or not line_nums:
        raise Exception('Missing file name or line numbers')

    ext = ''
    if '.' in filename:
        _, ext = filename.split('.')

    if '-' in line_nums:
        start, end = line_nums.split('-')
    else:
        start = end = line_nums

    start = int(start.replace('L', ''))
    end = int(end.replace('L', ''))

    return filename, ext, start, end


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <string_to_parse>' % sys.argv[0])
    if len(sys.argv) == 2:
        results = parse_insertion(sys.argv[1])
    if (results):
        print(results)
