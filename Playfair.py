import sys
import numpy as np 
def_char = 'x'
def_char2 = 'z'
alphabets="abcdefghjklmnopqrstuvwxyz"
param = sys.argv[1]

def process_key(input):
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
    processed = [ i for i in processed if i != 'j']
    [processed.append(i) for i in alphabets if i not in processed] 
    keymap = [[ processed[i+j*5] for i in range(0,5)] for j in range(0,5)]
    return keymap

def encrypt(message,keymap):
    first=""
    second=""
    ciphered=""
    for letter in range(1,len(message),2):
        for i in range(0,5):
            if message[letter-1] in key_matrix[i]:
                first = key_matrix[i].index(message[letter-1])
                ciphered += key_matrix[(i+1)%5][first]
                break
        for i in range(0,5):
            if message[letter] in key_matrix[i]:
                second = key_matrix[i].index(message[letter])
                ciphered += key_matrix[(i+1)%5][second]
                break

    print(ciphered)
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
    key_matrix = process_key(key)
    cipher_text = encrypt(input,key_matrix)
    print(key_matrix)
