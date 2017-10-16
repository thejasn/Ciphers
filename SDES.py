import sys

# global definitions
IP = [2,6,3,1,4,8,5,7]
EP = [4,1,2,3,2,3,4,1]
P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
IP1 = [2,6,3,1,4,8,5,7]
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
    
    


print(" Enter Key:",end="")
key = str(input())
key = "".join(key.split())
key = list(key)
k1=[0]*8
k2=[0]*8
key_generate(key,k1,k2)
print(" Enter Plain text:",end="")
plaintext = list(input())
temp=[0]*8
for i in range(8):
    temp[i]=plaintext[IP[i]-1]
plaintext=temp
p1 = plaintext[:4]
p2 = plaintext[4:]
for i in range(8):
    plaintext[i]=p2[EP[i]-1]
for i in range(8):
    temp[i] = int(plaintext[i],2) ^ int(k1[i],2)
print(temp)
