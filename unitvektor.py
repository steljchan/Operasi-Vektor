import math
def Panjangvektor(A):
    return math.sqrt(A[0]*2 + A[1]*2)
def Panjangvektor(B):
    return math.sqrt(B[0]*2 + B[1]*2)
                     
def Unit(A):
    Panjang = Panjangvektor(A)
    if Panjang == 0
        return (0,0)
    return (A[0]/Panjang, A[1]/Panjang)
def Unit(B):
    Panjang = Panjangvektor(B)
    if Panjang == 0
        return (0,0)
    return (B[0]/Panjang, B[1]/Panjang)