import sys
param = sys.argv[1]
IP = [  58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17,  9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

IP1 = [  40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41,  9, 49, 17, 57, 25    
]
EP = [  32,  1,  2,  3,  4,  5,
         4,  5,  6,  7,  8,  9,
         8,  9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32,  1 
     ]
PF = [
        16,  7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26,  5, 18, 31, 10,
         2,  8, 24, 14, 32, 27,  3,  9,
        19, 13, 30,  6, 22, 11,  4, 25
]
S = 8 * [ 64 * [0]]
S[0] = [
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
         0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
         4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]
S[1] = [
         5,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
         3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
         0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
]
S[2] = [
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
         1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 1
]
S[3] = [
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
         3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
]
S[4]=[
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
         4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
]
S[5]=[
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
         9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
         4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
]
S[6]=[
         4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
         1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
         6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
]
S[7] = [
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
         1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
         7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
         2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
]

PC1 = [
        57, 49, 41, 33, 25, 17,  9,
        1, 58, 50, 42, 34, 26, 18,
        10,  2, 59, 51, 43, 35, 27,
        19, 11,  3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14,  6, 61, 53, 45, 37, 29,
        21, 13,  5, 28, 20, 12,  4
]
PC2 = [
        14, 17, 11, 24,  1,  5,  3, 28,
        15,  6, 21, 10, 23, 19, 12,  4,
        26,  8, 16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
]
schedule = [
    1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1
]
keys = 16 * [48 *[0] ] 

def process_key(key):
    pc1=[0]*56
    for i in range(56):
        pc1[i] = key[PC1[i]-1]
    return pc1
def l_shift(input,round_no):
    shifted = input[schedule[round_no-1]:]+input[:schedule[round_no-1]]
    return shifted
def process_key2(next):
    op=[0]*48
    for i in range(48):
        op[i] = next[PC2[i]-1]
    return op

def round_func(bits32,key):
        ep = [0]*48
        F = [0] * 48
        for i in range(48):
                ep[i] = bits32[EP[i]-1]
        #print(ep)
        for i in range(48):
                F[i] = ep[i] ^ key[i]
        sbox=""
        ctr=0
        for i in range(0,48,6):
                row = F[i:i+1]+F[(i+6)-1:i+6]
                row = "".join(str(i) for i in row )
                row = int(row,2)

                col = F[i+1:(i+6)-1]
                col = "".join(str(i) for i in col)
                col = int(col,2)
                sbox+= "{0:04b}".format(S[ctr][ row * 16 + col])
                sbox+=" "
                ctr+=1
        sbox = "".join(sbox.split())
        sbox = [int(i) for i in sbox]
        P = [0] * 32
        for i in range(32):
                P[i] = sbox[PF[i]-1]
        return P
        
key = [0] * 64
print(" Enter key:",end="")
k = str(input())
k = "".join(k.split())
for i in range(64):
    key[i] = int(k[i],10)
#print(key)

if param == "enc":
        print(" Enter plain text in hexadecimal:",end="")

        pt = str(input())
        pt = "".join(pt.split())
        #print(len(pt))
        plaintext = "".join( str("{0:04b}".format(int(pt[i],16))) for i in range(16))
        #print(plaintext)
        plaintext = [int(i) for i in plaintext]
        #apply ip on plain text
        ip=[0]*64
        for i in range(64):
                ip[i] = plaintext[IP[i]-1]

        R = ip[32:]
        L = ip[:32]



        pc1 = process_key(key)
        #print(pc1)
        c = pc1[:28]
        d = pc1[28:]
        next = l_shift(c,1)
        next += l_shift(d,1)
        keys[0] = process_key2(next)

        exchg = round_func(R,keys[0])
        #print(exchg)
        temp = list(R)

        for i in range(32):
                R[i] = L[i] ^ exchg[i] 
        L = list(temp)
        #print(R,end="  ")
        #print(L)

        #print(keys[0])
        for i in range(15):
            c = next[:28]
            d = next[28:]
            next = l_shift(c,i+2)
            next += l_shift(d,i+2)
            keys[i+1] = process_key2(next)
            print(keys[i+1])
            exchg  =  round_func(R,keys[i+1])
            temp = list(R)
            for i in range(32):
                    R[i] = L[i] ^ exchg[i]
            L = list(temp)
            #print(R,end="  ")
            #print(L)
           #print(keys[i+1]) R+L
        temp = R+L
        ip1 = [0]*64
        for i in range(64):
                ip1[i] = temp[IP1[i]-1]
        temp=""
        temp = "".join(str(i) for i in ip1)
        #print(temp)
        print(" Encrypted string is:",end="")
        print(hex(int(temp,2))[2:])
if param == "dec":
        print(" Enter cipher text in hexadecimal:",end="")

        pt = str(input())
        pt = "".join(pt.split())
        #print(len(pt))
        plaintext = "".join( str("{0:04b}".format(int(pt[i],16))) for i in range(16))
        #print(plaintext)
        plaintext = [int(i) for i in plaintext]
        #apply ip on plain text
        ip=[0]*64
        for i in range(64):
                ip[i] = plaintext[IP[i]-1]

        R = ip[32:]
        L = ip[:32]



        pc1 = process_key(key)
        #print(pc1)
        c = pc1[:28]
        d = pc1[28:]
        next = l_shift(c,1)
        next += l_shift(d,1)
        keys[0] = process_key2(next)
        temp = list(next)
        for i in range(1,16):
                a = temp[:28]
                b = temp[28:]
                temp = l_shift(a,i+1)
                temp += l_shift(b,i+1)
                keys[i]=process_key2(temp)
                print(keys[i])
        exchg = round_func(R,keys[15])
        #print(exchg)
        temp = list(R)

        for i in range(32):
                R[i] = L[i] ^ exchg[i] 
        L = list(temp)
        #print(R,end="  ")
        #print(L)

        #print(keys[0])
        for i in range(15):
            c = next[:28]
            d = next[28:]
            next = l_shift(c,i+2)
            next += l_shift(d,i+2)
            #keys[i+1] = process_key2(next)
            exchg  =  round_func(R,keys[15-(i+1)])
            temp = list(R)
            for i in range(32):
                    R[i] = L[i] ^ exchg[i]
            L = list(temp)
            #print(R,end="  ")
            #print(L)
           #print(keys[i+1]) R+L
        temp = R+L
        ip1 = [0]*64
        for i in range(64):
                ip1[i] = temp[IP1[i]-1]
        temp=""
        temp = "".join(str(i) for i in ip1)
        #print(temp)
        print(" Decrypted string is:",end="")
        print(hex(int(temp,2))[2:])