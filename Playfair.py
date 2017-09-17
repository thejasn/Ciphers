import sys
import numpy as np 
def_char = 'x'
def_char2 = 'z'
alphabets="abcdefghijklmnopqrstuvwxyz"
param = sys.argv[1]

def process_input(input):
    processed=""
    for i in range(0,len(input)-1):
        if input[i] == input[i+1]:
            processed+=input[i]
            if input[i] == def_char:
                processed+=def_char2
            else:
                processed+=def_char
        else:
            processed+=input[i]
    if len(processed) % 2 ==0:
        if input[len(input)-1]==def_char:
            processed+=input[len(input)-1]+def_char2
        else:   processed+=input[len(input)-1]+def_char; 
    else: processed+=input[len(input)-1]
     
    processed = list(processed)
    [processed.append(i) for i in alphabets if i not in processed] 
    keymap = [[ processed[i+j*5] for i in range(0,5)] for j in range(0,5)]
    return keymap

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
    key_matrix = process_input(input)
    
