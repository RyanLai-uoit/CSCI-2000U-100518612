
def has_no_e( str line):
    if "e" in line:
        return False
    return True
f = open('gadsby_stripped.txt',w)
for line in f:
    has_no_e(line)

