import numpy as np
def rightrt(arr,n):
    ns_arr=''
    for i in range(n):
        n_arr=np.zeros(len(arr))
        for i in range(len(arr)-1,0,-1):
            n_arr[i]=arr[i-1]
        n_arr[0]=arr[len(arr)-1]
        arr=n_arr
    for i in range(len(arr)):
        temp=arr[i]
        tempi=int(temp)
        tempstr=str(tempi)
        ns_arr=ns_arr+tempstr
    return ns_arr
def rightsft(arr,n):
    ns_arr=''
    for i in range(n):
        n_arr=np.zeros(len(arr))
        for i in range(len(arr)-1,0,-1):
            n_arr[i]=arr[i-1]
        n_arr[0]=arr[len(arr)-1]
        arr=n_arr
    for i in range(n):
        arr[i]=0
    for i in range(len(arr)):
        temp=arr[i]
        tempi=int(temp)
        tempstr=str(tempi)
        ns_arr=ns_arr+tempstr
    return ns_arr
def matching(s0,s1,s2):
    s3=''
    for i in range(len(s0)):
        if (s0[i] == s1[i]):
            s01 = "0"
        else:
            s01= "1"
        if (s01 == s2[i]):
            s12="0"
        else:
            s12="1"
        s3=s3+s12
    return s3
binarr=np.zeros(64)
binarr=binarr.astype(np.str)
text="hello world"
bini=''.join(format(ord(i), '08b') for i in text)
bini=(bini+'1')
zrs='0'*360
bini=(bini+zrs)
bini=(bini+'0'*7*8+"1011000")
h0 = "0x6a09e667"
h1 = "0xbb67ae85"
h2= "0x3c6ef372"
h3 ="0xa54ff53a"
h4 = "0x510e527f"
h5 =  "0x9b05688c"
h6 =  "0x1f83d9ab"
h7 = "0x5be0cd19"
const=[0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
bini=bini + "0"*32*48
for i in range(64):
    binarr[i]= bini[i*32:i*32+32:1]
for i in range(16,64,1):
    print(i)
    s0=matching(rightrt(binarr[i-15],7),rightrt(binarr[i-15],18),rightsft(binarr[i-15],3))
    s1=matching(rightrt(binarr[i-2],17),rightrt(binarr[i-2],19),rightsft(binarr[i-2],10))
    binarr[i]=bin(int(binarr[i-16],2)+int(s0,2)+int(binarr[i-7],2)+int(s1,2))
    



