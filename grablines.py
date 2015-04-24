import sys

def grab(filename, start, end=None):
    """Returns a lines `start` to `end` of a file
    Line numbers are 1-based and end is inclusive
    If end is None, return just one line
    """
    start = int(start)
    end = start if end is None else int(end)

    with open(filename) as f:
        lines = []

        f_iter = iter(f)

        # since start is 1-based, we don't want to lose any lines in the file
        # e.g. start is 1, we shouldn't call next at all
        for skip in range(start - 1):
            next(f_iter)

        for skip in range(end - start + 1):  # end is inclusive so add 1
            lines.append(next(f_iter))

    return lines


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: %s <filename> <start> [end]' % sys.argv[0])
    if len(sys.argv) == 3:
        lines = grab(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3:
        lines = grab(sys.argv[1], sys.argv[2], sys.argv[3])
    if (lines):
        print(lines)
