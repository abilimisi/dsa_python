def rev_str(inp):

    rev =""

    for i in inp:
        rev = i+rev
    return rev
inp_str = "SURANA"
print(rev_str(inp_str))