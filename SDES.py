import sys

param = sys.argv[1]
# global definitions
IP = [2,6,3,1,4,8,5,7]
EP = [4,1,2,3,2,3,4,1]
P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
IP1 = [4,1,3,5,7,2,8,6]
P4= [2,4,3,1]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

# key generation 
def key_generate(k,key1,key2):
    k10 = [0] * len(k)
    sub_key1 = [0] * (len(k)//2)
    sub_key2 = [0] * (len(k)//2)
    for i in range(len(k)):
        k10[i]=k[P10[i]-1]
    for i in range(len(k)//2):
        sub_key1[i]=k10[i]
        sub_key2[i]=k10[i+5]
    #left shift by 1 place
    sub_key1 = sub_key1[1:]+sub_key1[:1]
    sub_key2 = sub_key2[1:]+sub_key2[:1]
    temp = sub_key1+sub_key2
    k8 = [0] * 8
    for i in range(8):
        key1[i]=temp[P8[i]-1]
   
    #LEFT SHIFT BY 2 BITS
    sub_key1 = sub_key1[2:]+sub_key1[:2]
    sub_key2 = sub_key2[2:]+sub_key2[:2]
    temp = []
    temp = sub_key1+sub_key2
    for i in range(8):
        key2[i]=temp[P8[i]-1]
    
    
def generate_sbox(left,s0,boxno):
    #left = ep[:4]
    #right = ep[4:]
    s0_row = left[:1]+left[3:4]
    s0_row = ''.join(str(i) for i in s0_row)
    s0_row = int(s0_row,2)
    #print(s0_row)
    s0_col = left[1:2]+left[2:3]
    
    s0_col = ''.join(str(i) for i in s0_col)
    s0_col = int(s0_col,2)
    #print(s0_col)
    if boxno == 0:
       s0 = "{0:b}".format(S0[s0_row][s0_col])
       if s0 == "1":
           s0="01"
    else:
       s0 = "{0:b}".format(S1[s0_row][s0_col])
       if s0 == "1":
           s0="01"

    return s0
def SDES(ip,output,key):
    #print(plaintext)
   
    #plaintext=temp
    #ip = plaintext
    p1 = ip[:4]
    p2 = ip[4:]
    ep=[0]*8
    for i in range(8):
        ep[i]=p2[EP[i]-1]
    
    for i in range(8):
        ep[i] = int(ep[i],2) ^ int(key[i],2)
    #print(ep)
    s0=""
    s1=""
    s0 = generate_sbox(ep[:4],s0,0)
   
    s1 = generate_sbox(ep[4:],s1,1)

    sbox = s0+s1
    sbox = [int(i) for i in sbox]
    #print(sbox)
    p4=[0]*4
    for i in range(4):
        p4[i] = sbox[P4[i]-1]
    #print(p4)
    p1 = [int(i) for i in p1]
    #print(p1)
    for i in range(4):
        output[i] = p1[i] ^ p4[i]
        #print(p1)

if param == "enc":
    print(" Enter Key:",end="")
    key = str(input())
    key = "".join(key.split())
    key = list(key)
    k1=[0]*8
    k2=[0]*8
    key_generate(key,k1,k2)
    print(" Enter Plain text:",end="")
    plaintext = list(input())
    right=[0]*4
    left =[0]*4
    ip=[0]*8
    for i in range(8):
        ip[i]=plaintext[IP[i]-1]
    ##print(ip)
    SDES(ip,right,k1)
    temp = ip[4:]+right
    print(right)
    ip = [str(i) for i in temp]
    #print(ip)
    SDES(ip,left,k2)
    print(left)
    ip1 = left + right
    print(ip1)
    enc=[0]*8
    for i in range(8):
        enc[i]=ip1[IP1[i]-1]
    print(enc)
if param == "dec":
    print(" Enter Key:",end="")
    key = str(input())
    key = "".join(key.split())
    key = list(key)
    k1=[0]*8
    k2=[0]*8
    key_generate(key,k1,k2)
    print(" Enter Cipher text:",end="")
    ciphertext = list(input())
    right=[0]*4
    left =[0]*4
    ip=[0]*8
    for i in range(8):
        ip[i]=ciphertext[IP[i]-1]
    ##print(ip)
    SDES(ip,right,k2)
    temp = ip[4:]+right
    print(right)
    ip = [str(i) for i in temp]
    #print(ip)
    SDES(ip,left,k1)
    print(left)
    ip1 = left + right
    print(ip1)
    enc=[0]*8
    for i in range(8):
        enc[i]=ip1[IP1[i]-1]
    print(enc)