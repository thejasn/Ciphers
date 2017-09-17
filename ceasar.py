import sys

offset = int(sys.argv[1])
output=""
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
# values = en
# for i in range(0,len(input)-1):