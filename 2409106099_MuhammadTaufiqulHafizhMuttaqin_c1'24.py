# ulang = 10
# for i in range (ulang) :
#   print ("halo")

# simpan = [12, "udin petot", 14.5, True, 'A',"102"]
# for i in simpan : 
#    print (simpan)

# simpan = [12, "udin petot", 14.5, True, 'A',"102"]
# for i in simpan [0:3] : 
#    print (i)

# for i in range (1, 4)
#     for j in range (1, 4) :
#       print (f"{1} * {j} = {i * j}")
#     print ()

# print ("Menu Rumah Makan Informatika 24: ")
# print ("--------------------------------")
# simpan = ["Nasi Goreng", "mie goreng", "mie ayam", "bakso", "soto"]
# for i range (simpan)
#     print

# print ("Menu Rumah Makan Informatika 24: ")
# print ("--------------------------------")
# simpan = ["Nasi Goreng", "mie goreng", "mie ayam", "bakso", "soto"]
# for i, menu in enumerate(simpan,start=100):
#     print(f"{i}.{menu}")

# print ("Menu Rumah Makan Informatika 24: ")
# print ("--------------------------------")
# simpan = ["Nasi Goreng", "mie goreng", "mie ayam", "bakso", "soto"]
# for i in range (len(simpan))
#    print(f"{i+1}. {simpan[i]}")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya') :
#     hitung += 1
#     jawab = input("ulang lagi tidak? ")
# print(f"total perulangan: {hitung}")

# jawab = 'ya'
# hitung = 0
# while (True):
#     hitung += 1
#     ulang = input("masih ingin mengulangi? ")
#     if ulang == "tidak" or ulang =="Tidak":
#         break
# print (f"total perulangan: {hitung}")

print("Daftar bilangan ganjil dari 1-10")
for i in range (10):
    if i % 2 == 0:
        continue
    print(i)