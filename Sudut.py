import math

def DotProduct(A,B):
    return A[0]*B[0] + A[1]*B[1]

def Panjangvektor(A):
    return math.sqrt(A[0]**2 + A[1]**2)

def Panjangvektor(B):
    return math.sqrt(B[0]**2 + B[1]**2)

def Sudut(A,B):
    PanjangA = Panjangvektor(A)
    PanjangB = Panjangvektor(B)
    DotAB = DotProduct(A,B)
    sudut = DotAB/(PanjangA*PanjangB)
    derajat = math.acos(sudut)
    return math.degrees(derajat)