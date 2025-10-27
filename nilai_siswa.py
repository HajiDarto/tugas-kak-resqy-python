nilai_1 = input ("masukkan nilai pertama = ")
nilai_2 = input ("masukkan nilai kedua = ")

nilai_1 = float(nilai_1)
nilai_2 = float(nilai_2)

rata_rata = (nilai_1 + nilai_2) / 2
print (rata_rata)

if rata_rata >= 74:
    print("anda lulus")
else :
    print("anda TIDAK lulus")