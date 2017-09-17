import sys
import numpy as np 
def_char = 'x'
def_char2 = 'z'
param = sys.argv[1]
if param == "enc":
    print(" Enter Key:",end="")
    key = str(input())
    key = "".join(key.split()) #removing whitespaces
    unique = []
    processed=""
    [unique.append(i) for i in key if i not in unique] # removing duplicates
    key = unique
    print(" Plain Text:",end="")
    input = str(input())
    for i in range(0,len(input)-1):
        if input[i] == input[i+1]:
            processed+=input[i]
            if input[i] == def_char:
                processed+=def_char2
            else:
                processed+=def_char
        else:
            processed+=input[i]
    processed+=input[len(input)-1]

    print(processed)


