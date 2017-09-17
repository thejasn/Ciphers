import sys
output=""
offset = int(sys.argv[1])
param = sys.argv[2]
if param == "enc":
    print(" Plain text:",end="")
    input = str(input())
    for i in input.encode('ascii'):
        if chr(i).isupper():
            if i>=(90-offset+1):
                output+=chr((i+offset)%91+65)
            else:
                output+=chr((i+offset)%91)
        elif chr(i).islower():
            if i>(122-offset+1):
                output+=chr((i+offset)%123+97)
            else:
                output+=chr((i+offset)%123)
        else:   output+=chr(i)
    print(" Cipher Text:",end="")
    print(output)
elif param == "dec":
    print(" Ciphered Text:",end="")
    input = str(input())
    for i in input.encode('ascii'):
        if chr(i).isupper():
            if i < (65+offset):
                output+=chr((i-offset)+26)
            else:
                output+=chr((i-offset))
        elif chr(i).islower():
            if i < (97+offset):
                output+=chr((i-offset)+26)
            else:
                output+=chr(i-offset)
        else: output+=chr(i)
    print(" Decipherd Text:",end="")
    print(output)
else:
    print(" Error: Usage")
    print(" py ceasar.py arg0 arg1 | arg0 = offset, arg1 = enc/dec")
# values = en
# for i in range(0,len(input)-1):