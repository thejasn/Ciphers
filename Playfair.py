import sys
import numpy as np 
def_char = 'x'
def_char2 = 'z'
alphabets="abcdefghjklmnopqrstuvwxyz"
param = sys.argv[1]

def process_key(input):
    processed=""
    i=0
    while i < len(input)-1:
        if input[i] == input[i+1]:
            processed+=input[i]
            if input[i] == def_char:
                processed+=def_char2
            else:
                processed+=def_char
        else:
            processed+=input[i]+input[i+1]
            i+=1
        i+=1
 #       print(processed)
    if len(processed) % 2 ==0:
        if input[len(input)-1]==def_char:
            processed+=input[len(input)-1]+def_char2
        else:   processed+=input[len(input)-1]+def_char; 
    else: processed+=input[len(input)-1]
    
    return processed

def encrypt(message,key_matrix):
    first=""
    second=""
    re_message ="" 
    message = [i for i in message]
    for i in range(len(message)):
        if message[i]=='i':
            message[i]='j'
        re_message+=message[i]
    print(re_message)
    ciphered=""
    for letter in range(1,len(message),2):
        row1=-1
        row2=-1
       
        for i in range(0,5):
            if message[letter-1] in key_matrix[i]:
                row1 = i
                first = key_matrix[i].index(message[letter-1])
                
                break
        for i in range(0,5):
            if message[letter] in key_matrix[i]:
                row2 = i
                second = key_matrix[i].index(message[letter])
                break
        if row1 == row2 and row1 != -1 and row2 != -1 : 
            ciphered += key_matrix[row1][(first+1)%5]
            ciphered += key_matrix[row2][(second+1)%5]
        elif first == second:
            ciphered += key_matrix[(row1+1)%5][first]
            ciphered += key_matrix[(row2+1)%5][second]
        else:
            ciphered += key_matrix[row1][second]
            ciphered += key_matrix[row2][first]
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
    input = "".join(input.split())
    input = process_key(input)
    processed = list(key)
    processed = [ i for i in processed if i != 'j']
    [processed.append(i) for i in alphabets if i not in processed] 
    keymap = [[ processed[i+j*5] for i in range(0,5)] for j in range(0,5)]
    print(keymap)
    #print(key_matrix)
    cipher_text = encrypt(input,keymap)
   # print(key_matrix)
