from Penjumlahan import jumlah
from Pengurangan import kurang
from Sudut import Sudut
from dot import DotProduct
from panjang import Panjangvektor
from unitvektor import Unit
x1 = int(input("componen X untuk Vektor 1 : "))
y1 = int(input("componen y untuk Vektor 1 : "))
x2 = int(input("componen X untuk Vektor 2 : "))
y2 = int(input("componen y untuk Vektor 2 : "))
A = [x1, y1]
B = [x2, y2]

def main():
  while True:
    print("Operasi Pada vektor")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Panjang vektor")
    print("4. Sudut antar dua vektor")
    print("5. Dot product")
    print("6. Unit vektor")
    print("7. Keluar")
    pilih = int(input("Pilih: "))

    if pilih == 7:
      print ("program selesai")
      break

    if pilih == 1:
      C = jumlah(A,B)
      print(f"{A} + {B} = {C}")
    elif pilih == 2:
      D = kurang(A,B)
      print(f"{A} - {B} = {D}")
    elif pilih == 3:
      E1 = Panjangvektor(A)
      print(f"Panjang vektor A adalah {E1}")
      E2 = Panjangvektor(B)
      print(f"Panjang vektor B adalah {E2}")
    elif pilih == 4:
      F = Sudut(A,B)
      print(f"Sudut antara A dan B adalah {F}")
    elif pilih == 5:
      G = DotProduct(A,B)
      print(f"{A} * {B} = {G}")
    elif pilih == 6:
      H1 = Unit(A)
      print(f"Unit vektor A adalah {H1}")
      H2 = Unit(B)
      print(f"Unit vektor B adalah {H2}")
main()

