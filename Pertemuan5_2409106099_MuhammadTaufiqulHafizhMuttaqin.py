akuns = []

while True:
    print("Halo! selamat datang di aplikasi Catatan")
    print("Silahkan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("----------------------------------")
    opsi = input("Pilih opsi : ")
    print("") 
    
    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username : ")
        akuna = False 
        for akun in akuns:
            if akun[0] == Username: # Memeriksa apakah username sudah ada
                akuna = True
                break
            if akuna:
                print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
            else:
                Password = input("Password : ")
                akuns.append([Username,Password, []]) #Simpan username, password, dan catatan 
                print(f"Akun Anda Berhasil terdaftar dengan ID: {Username}")
                

# nama = ["shandy",106,True,
#         ["yuyun",145],3.96,
#         [123,"ALVITO",False,3.66],
#         "rehan"]
# print(nama[4])

# matkul = ["APD",
#           "APL",
#           "WEB",
#           "JARKOM",
#           "BASDAT",
#           "STRUKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]
# print(matkul[6])

# makanan = ["Bakso","Sate","Soto","nasi goreng","mie ayam","ayam bakar","cumi goreng"]
# print("Sebelum :")
# print(makanan)
# # makanan.append("Nasi Goreng")
# print("Sesudah :")
# makanan.clear()
# print(makanan)
# data = makanan.pop(5)
# print(makanan)
# print(data)
# del makanan[]
# makanan.insert(2,"Nasi Goreng")
# makanan[0] = ["AYAM","BEBEK"]
# print(makanan)

# minuman = ["es teh","es jeruk","es kopi","air hitam","jus","pocari","teh pucuk"]
# print("Sebelum")
# print(minuman)
# del minuman[3]
# minuman[4] = "air putih"
# print("Sesudah")
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)

# makanan = ["ayam","ikan",["Bakso","Soto","Sate","ikan","bebek"],
#            ["teh","kopi","air"]]

# for i in makanan :
#     if isintance(i, list) :
#         for j in i :
#           print(j)        
#         else:
#             print(i)    
# for i in makanan :
#     for j in i :
#         print(j)
