"""Program to code DES, uses a key.txt and plaintext.txt for input and cipher.txt for output"""

import pprint

def convert_hex_to_Binary(inputstring):
    """Convert and pad hex digits to binary"""
    num_of_bits = len(inputstring)*4
    return bin(int(inputstring, 16))[2:].zfill(num_of_bits)     

def form_k_initial(key):
    """Form the initial Key Permutation"""
    PC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,
        35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,
        46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    return "".join([key[x-1]for x in PC1])

def getC_D(key):
    """Returns CD Blocks"""
    CD = {}
    CD[0] = (key[0:28],key[28::])
    for i in range(1,17):
        if i==1 or i==2 or i==9 or i==16:
            CD[i] = (CD[i-1][0][1::]+CD[i-1][0][:1:],CD[i-1][1][1::]+CD[i-1][1][:1:])
        else:
            CD[i] = (CD[i-1][0][2::]+CD[i-1][0][:2:],CD[i-1][1][2::]+CD[i-1][1][:2:])
    return CD

def get_second_permutation(CD):
    """Generates permutations for keys"""
    PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,
    27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,
    39,56,34,53,46,42,50,36,29,32]
    k = {}
    for i in range(0,17):
        temp = CD[i][0]+CD[i][1]
        k[i] = ""
        for j in PC2:
            k[i]+= temp[j-1]
    return k
def input_permutation(inputkey):
    ip=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,
    38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,
    9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,
    47,39,31,23,15,7]
    return "".join([inputkey[x-1]for x in ip])


def DES():
    #Read both keys
    with open("./plaintext.txt") as f:
        binaryinput = convert_hex_to_Binary(f.read())
    with open("./key.txt") as f:
        binarykey = convert_hex_to_Binary(f.read())
    permuted_k = form_k_initial(binarykey)
    # Permuted K now has our initial Key K+
    cd = getC_D(permuted_k)
    restkeys = get_second_permutation(cd)
    IP = input_permutation(binaryinput)
    L={}
    R={}
    L[0]=IP[:32]
    R[0]=IP[32:]
    E=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,
    17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,
    28,29,30,31,32,1]
    S={}
    S[0]=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,0,15,7,4,14,2,13,
        1,10,6,12,11,9,5,3,8,4,1,14,8,13,6,2,11,15,12,9,7,3,
        10,5,0,15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    S[1]=[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,
        12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    S[2]=[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,
        8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    S[3]=[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,13,8,11,5,6,15,0,3,
        4,7,2,12,1,10,14,9,10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    S[4]=[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,14,11,2,12,4,7,13,
        1,5,0,15,10,3,9,8,6,4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    S[5]=[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,10,15,4,2,7,12,9,5,
        6,1,13,14,0,11,3,8,9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    S[6]=[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,13,0,11,7,4,9,1,10,
        14,3,5,12,2,15,8,6,1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    S[7]=[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,1,15,13,8,10,3,7,4,
        12,5,6,11,0,14,9,2,7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    P=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,
    3,9,19,13,30,6,22,11,4,25]
    for i in range(1,17):
        L[i]=R[i-1]
        ER=""
        XOR=""
        for j in E:
            ER+= R[i-1][j-1]
        for j in range(0,48):
            if ER[j] == restkeys[i][j]:
                XOR+='0'
            else:
                XOR+='1'
        R[i]=""
        F=""
        for j in range (0,8):
            row = (XOR[j*6]+XOR[j*6+5])
            col = (XOR[j*6+1]+XOR[j*6+2]+XOR[j*6+3]+XOR[j*6+4])
            row = int(row,2)
            col = int(col,2)
            temp=bin(S[j][row*16+col])[2:].zfill(4)
            F+=temp
        for j in P:
            R[i]+=F[j-1]
        for j in range(0,32):
            if R[i][j] == L[i-1][j]:
                R[i]=R[i]+'0'
            else:
                R[i]=R[i]+'1'
        R[i]=R[i][32:]
    IP2=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,
     54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,
     35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,
     49,17,57,25]

    RL=R[16]+L[16]
    M2=""
    for i in IP2:
        M2+=RL[i-1]
    ciphertext = ''
    for i in range(0,16):
        temp=hex(int(M2[i*4:i*4+4],2))
        ciphertext+=temp[2:]
    
    with open("./ciphertext.txt",mode='w') as f:
        f.write(ciphertext.upper())
    
DES()