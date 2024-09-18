cuaca = "mendung"

if cuaca == "mendung":
    print("diam di rumah")
else:
     ("hari ini mendung")

Umur = int(input("Masukkan Umur Anda : ")) 
if Umur > 0 :
    if Umur <= 10 :
        print("Umur anda termasuk kategori Anak-Anak")
    elif Umur <= 18 :
        print("Umur anda termasuk kategori Remaja")
    elif Umur <= 35 :
        print("Umur anda termasuk dewasa")
    elif Umur <= 65 :
        print("Umur anda termasuk paruh baya")
    else:
        print("Umur anda termasuk kategori tua")
else:
    print("Input Usia Harus Bilangan Positif")

NIM = int(input("Masukkan NIM :"))

if NIM >= 1 and NIM <= 50 :
    if NIM >= 1 and NIM <= 25 :
        print("Kelas A`1")
    else :
        print("Kelas A`2")
elif NIM >= 51 and NIM <= 100 :
    if NIM >= 51 and NIM <= 75 :
        print("Kelas B`1")
    else :
        print("Kelas B`2")
elif NIM >= 101 and NIM <= 121 :
    if NIM >= 101 and NIM <= 110 :
        print("Kelas C`1")
    else :
        print("Kelas C`2")
else :
    print("Anda bukan Mahasiswa Informatika 2024")

NIM = int(input("Masukkan NIM :"))
hasil = "Kelas A" if NIM >=1 and NIM <=50 else "Kelas B"if NIM >=51 and NIM <=100 else "Kelas C" if NIM >=101 and NIM <=121 else "Mahasiswa Ghaib"
print(hasil)