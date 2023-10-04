#!/usr/bin/python3

def init_function(mode):
    try :
        f = open("datadir.c","x")
    except:
        f = open("datadir.c","w")
    f.write("void Init_PORTA_DIR(void)\n{\n\tDDRA = 0b")
    for i in range(8):
        if mode[i] == 'out':
            f.write("1")
        else:
            f.write("0")
    f.write("\n}")

map = {"in": 0, "out": 1}

ls = []

for i in range(8):
    ls.append(input(f"Please enter Bit {i} mode: ").lower().strip())
    
ls.reverse()
init_function(ls)
