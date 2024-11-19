def Sudut(A,B):
    sudut = Dotproduct/(Panjangvektor(A) * Panjangvektor(B))
    derajat = math.degrees(math.acos(sudut))
    return derajat