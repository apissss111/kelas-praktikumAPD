# Inventaris properti perusahaan

# 2409106(099) - Muhammad Taufiqul Hafizh Muttaqin
# C1 C'24


# Daftar inventaris perusahaan yang akan menyimpan data barang
inventory = []

# Daftar pengguna (user) dengan username dan password
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},                                    
    {"username": "user", "password": "user123", "role": "user"}
]         
             # Terdapat multiuser login yaitu admin dan user 

# Note : LOGIN ADMIN HANYA BISA DIAKSES MENGGUNAKAN USERNAME DAN PASSWORD DIBAWAH INI :
# LOGIN admin (Masukkan username : admin
#              Masukkan password : admin123)

# LOGIN user 
# bisa dari (MENDAFTAR AKUN)
# atau bisa menggunakan (Masukkan username : user
#                        Masukkan password : user123)


while True:
    print("\n=== Inventaris Properti Perusahaan ===")
    print("1. Mendaftar")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":  # Mendaftar
        print("=== Mendaftar Pengguna Baru ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")

        if username and password:
            users.append({"username": username, "password": password, "role": "user"})
            print("Pengguna baru berhasil didaftarkan!")
        else:
            print("Username dan password tidak boleh kosong.")
    
    elif pilihan == "2":  # Login
        print("=== Login ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        role = None
        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Login berhasil sebagai {user['role']}.")
                role = user["role"]
                break

        if role == "admin":
            while True:
                print("\n=== Menu Admin ===")
                print("1. Tambah Barang")
                print("2. Lihat Barang")
                print("3. Ubah Barang")
                print("4. Hapus Barang")
                print("5. Logout")
                pilihan_admin = input("Masukkan pilihan: ")

                if pilihan_admin == "1":  # Tambah barang
                    print("=== Menambah Barang Baru ===")
                    try:
                        id_barang = int(input("Masukkan ID barang: "))
                        kategori = input("Masukkan kategori barang: ")
                        jumlah = int(input("Masukkan jumlah barang: "))
                        merk = input("Masukkan merk barang: ")
                        harga = float(input("Masukkan harga barang: "))
                        tanggal_pembelian = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")

                        # Menyimpan barang ke dalam daftar inventory
                        inventory.append([id_barang, kategori, jumlah, merk, harga, tanggal_pembelian])
                        print("Barang berhasil ditambahkan!")
                    except ValueError:
                        print("Kesalahan: Pastikan ID, jumlah, dan harga diisi dengan benar.")
                
                elif pilihan_admin == "2":  # Lihat barang
                    print("=== Daftar Barang ===")
                    if inventory:
                        for item in inventory:
                            print(f"ID: {item[0]}, Kategori: {item[1]}, Jumlah: {item[2]}, Merk: {item[3]}, Harga: {item[4]}, Tanggal Pembelian: {item[5]}")
                    else:
                        print("Tidak ada barang dalam inventaris.")

                elif pilihan_admin == "3":  # Ubah barang
                    print("=== Memperbarui Barang ===")
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin diubah: "))
                        for item in inventory:
                            if item[0] == id_barang:
                                item[2] = int(input(f"Masukkan jumlah baru (sekarang: {item[2]}): "))
                                item[4] = float(input(f"Masukkan harga baru (sekarang: {item[4]}): "))
                                print("Barang berhasil diperbarui!")
                                break
                        else:
                            print("Barang dengan ID tersebut tidak ditemukan.")
                    except ValueError:
                        print("Kesalahan: Masukkan data yang benar.")

                elif pilihan_admin == "4":  # Hapus barang
                    print("=== Menghapus Barang ===")
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
                        for item in inventory:
                            if item[0] == id_barang:
                                inventory.remove(item)
                                print("Barang berhasil dihapus!")
                                break
                        else:
                            print("Barang dengan ID tersebut tidak ditemukan.")
                    except ValueError:
                        print("Kesalahan: ID barang harus berupa angka.")

                elif pilihan_admin == "5":  # Logout
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")
        
        elif role == "user":
            while True:
                print("\n=== Menu Pengguna ===")
                print("1. Lihat Barang")
                print("2. Logout")
                pilihan_user = input("Masukkan pilihan: ")

                if pilihan_user == "1":  # Lihat barang (pengguna biasa)
                    print("=== Daftar Barang ===")
                    if inventory:
                        for item in inventory:
                            print(f"ID: {item[0]}, Kategori: {item[1]}, Jumlah: {item[2]}, Merk: {item[3]}, Harga: {item[4]}, Tanggal Pembelian: {item[5]}")
                    else:
                        print("Tidak ada barang dalam inventaris.")
                
                elif pilihan_user == "2":  # Logout
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")
        
        else:
            print("Login gagal. Username atau password salah.")

    elif pilihan == "3":  # Keluar program
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
