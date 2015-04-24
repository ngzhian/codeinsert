import os
import sys

matches = []

def find(name, start='.'):
    """Returns the path of a file relative to start"""
    for root, dirnames, filenames in os.walk(start):
        if name in filenames:
            return os.path.join(start, name)
        else:
            for dirname in dirnames:
                found = find(name, start=os.path.join(start, dirname))
                if found:
                    return found
    return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <filename> [top_dir]' % sys.argv[0])
    if len(sys.argv) == 2:
        filename = find(sys.argv[1])
    elif len(sys.argv) > 2:
        filename = find(sys.argv[1], sys.argv[2])
    if (filename):
        print(filename)
    sys.exit()
