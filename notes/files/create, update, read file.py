# Modes - w(create a file or overwrite the existing one), r(read the file), a(add something to the existing file or create a new file if that fil doesn't exist)

def add():
    with open('file.txt', 'a') as f:
        f.write("line\n")
def read():
    with open('file.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())


