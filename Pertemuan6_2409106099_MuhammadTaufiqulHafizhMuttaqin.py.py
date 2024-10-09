# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Twillight",
# # "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# # print(daftar_buku)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "Izanami#6848",
#     "Email" : "iniemail@gmail.com"
#  }
# }

# print(Biodata["KRS"]["0"])
# print(Biodata["Social Media"]["Email"])
    # Games = {
    #     "Game1" : "PUBG Mobile"
    #     "Game2" : "Mobile Legends"
    #     "Game3" : "COC"
    # # }
    # # games = dict(Sekiro = "Action", Pokemon = "Adventure",
    # Valorant = {"nama" : "123" : "informatika"}} )
    # print(games['Valorant']['nama'][123])
    
    # Games = {
    #     "Game1" : "PUBG Mobile"
    #     "Game2" : "Mobile Legends"
    #     "Game3" : {
    #         "nama" : "COC" 
    #         "genre" : "Strategy"
    #     }
    # }
    # print((Games.get)('Game 3').get('genre'))
    
#     Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in nilai 
#     print(i)
# print("")
#menggunakan items
# for mapel, nilai in Nilai.items():
#     print(f"{mapel} : {Nilai[mapel]}")


# #Sebelum diubah
# print(Film)


# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hour" : "Comedy","Oblivion" : "Horror"})

# #Setelah diubah
# print(Film)

# penggunaaan del
# del Film['Avenger Endgame']
# print(Film) 

# simpan = Film.pop('Hours')

# print(Film)
# simpan = Film.pop('Hours')
# Film.clear()
# print(Film)
# Film["hours"] = simpan
# print(Film)
# print("Jumlah Film : ", len(Film))

# movies = Film.copy
# print(movies)
# print("Jumlah Film : ", len(movies))

# key = "apel", "jeruk", "mangga", "semangka"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai Kimia : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# # print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
# print(f"Musik milik {i} adalah : ")
# for song in j:
# print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
# for x, y in value.items():
# print (x, " : ", y)
# print("")
