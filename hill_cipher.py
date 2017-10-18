import sys
import numpy as np
import math
from numpy.linalg import inv

def encypt(output):
    en=""
    for i in output:
        en+=chr((i%26)+97)
    return en
def decrypt(output):
    dc=""
    for i in output:
        dc+=chr(int(math.fmod(i,26)+97))
    return dc
param = sys.argv[1]
if param == "enc":
    for_decrypt=[]
    print(" Enter plain text:",end="")
    plaintext = str(input())
    if len(plaintext) % 3 != 0:
        if (len(plaintext)%3) == 2:
            plaintext+="xx"
        else:   plaintext+="x"
    #print(plaintext)
    print(" Enter key matrix 3x3 : ",end="")
    k = str(input())
    key = [int(i) for i in k.split()]
    key = np.matrix(key).reshape(3,3)
    #print(key)
    enc=""
    for i in range(0,len(plaintext),3):
        temp = [(i-97) for i in plaintext[i:i+3].encode("ascii")]
        temp = np.matrix(temp).reshape(3,1)
        #print(temp)

        output = np.dot(key,temp)
        output = np.array(output).reshape(-1).tolist()
        for_decrypt.append(output)
        #print(for_decrypt)
        enc+=encypt(output)
    print(" Ciphered Text:",end="")
    print(enc)

    print(" Enter ciphered text:",end="")
    plaintext = str(input())
    
    #print(key)
    key = inv(key)
    #print(key)
    dec=""
    ctr=0
    for i in range(0,len(plaintext),3):
        #temp = [int(i) for i in plaintext[i:i+3]]
        #temp = np.matrix(temp).reshape(3,1)
        #print(temp)
        temp = for_decrypt[ctr]
        #print(temp)
        output = np.dot(key,temp)
        output = np.array(output).reshape(-1).tolist()
        #print(output)
        dec+=decrypt(output)
        ctr+=1
    print(" Plain Text:",end="")
    print(dec)
