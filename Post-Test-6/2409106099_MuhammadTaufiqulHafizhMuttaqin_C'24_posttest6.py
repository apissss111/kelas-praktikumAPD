# Inventaris properti perusahaan

# Daftar inventaris yang sebelumnya berbentuk list kini menjadi dictionary dengan id_barang sebagai kuncinya
# Akses ke inventaris menggunakan kunci dictionary untuk menyimpan, mengubah, dan menghapus barang
# Daftar pengguna juga menggunakan dictionary untuk menyimpan username sebagai kunci dan menyimpan informasi terkait password dan role di dalam dictionary

# 2409106(099) - Muhammad Taufiqul Hafizh Muttaqin
# C1 C'24

# Daftar inventaris perusahaan yang akan menyimpan data barang
inventory = {}

# Daftar pengguna (user) dengan username dan password
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

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
            users[username] = {"password": password, "role": "user"}
            print("Pengguna baru berhasil didaftarkan!")
        else:
            print("Username dan password tidak boleh kosong.")
    
    elif pilihan == "2":  # Login
        print("=== Login ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role}.")
        else:
            print("Login gagal. Username atau password salah.")
            role = None

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

                        # Menyimpan barang ke dalam dictionary inventory
                        inventory[id_barang] = {
                            "kategori": kategori,
                            "jumlah": jumlah,
                            "merk": merk,
                            "harga": harga,
                            "tanggal_pembelian": tanggal_pembelian
                        }
                        print("Barang berhasil ditambahkan!")
                    except ValueError:
                        print("Kesalahan: Pastikan ID, jumlah, dan harga diisi dengan benar.")
                
                elif pilihan_admin == "2":  # Lihat barang
                    print("=== Daftar Barang ===")
                    if inventory:
                        for id_barang, item in inventory.items():
                            print(f"ID: {id_barang}, Kategori: {item['kategori']}, Jumlah: {item['jumlah']}, "
                                  f"Merk: {item['merk']}, Harga: {item['harga']}, Tanggal Pembelian: {item['tanggal_pembelian']}")
                    else:
                        print("Tidak ada barang dalam inventaris.")

                elif pilihan_admin == "3":  # Ubah barang
                    print("=== Memperbarui Barang ===")
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin diubah: "))
                        if id_barang in inventory:
                            inventory[id_barang]["jumlah"] = int(input(f"Masukkan jumlah baru (sekarang: {inventory[id_barang]['jumlah']}): "))
                            inventory[id_barang]["harga"] = float(input(f"Masukkan harga baru (sekarang: {inventory[id_barang]['harga']}): "))
                            print("Barang berhasil diperbarui!")
                        else:
                            print("Barang dengan ID tersebut tidak ditemukan.")
                    except ValueError:
                        print("Kesalahan: Masukkan data yang benar.")

                elif pilihan_admin == "4":  # Hapus barang
                    print("=== Menghapus Barang ===")
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
                        if id_barang in inventory:
                            del inventory[id_barang]
                            print("Barang berhasil dihapus!")
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
                        for id_barang, item in inventory.items():
                            print(f"ID: {id_barang}, Kategori: {item['kategori']}, Jumlah: {item['jumlah']}, "
                                  f"Merk: {item['merk']}, Harga: {item['harga']}, Tanggal Pembelian: {item['tanggal_pembelian']}")
                    else:
                        print("Tidak ada barang dalam inventaris.")
                
                elif pilihan_user == "2":  # Logout
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")

    elif pilihan == "3":  # Keluar program
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
