# Inventaris properti perusahaan

# 2409106(099) - Muhammad Taufiqul Hafizh Muttaqin
# C1 C'24

# INSTRUKSI:
# Lanjutkan program yang telah dibuat pada Posttest 6, dengan ketentuan sebagai berikut:
# - Buat 3 fungsi dengan dan tanpa parameter
# - Buat 2 prosedur
# - Gunakan minimal 3 variable global dan 5 variable lokal


# Variabel global
inventory = {}
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}
logged_in_user = None

# Fungsi tanpa parameter untuk melihat jumlah total barang
def total_barang():
    total = sum(item["jumlah"] for item in inventory.values())  # variabel lokal
    print(f"Total barang dalam inventaris: {total}")

# Fungsi dengan parameter untuk menambah barang
def tambah_barang(id_barang, kategori, jumlah, merk, harga, tanggal_pembelian):
    # Menggunakan variabel lokal untuk menyimpan data barang
    inventory[id_barang] = {
        "kategori": kategori,
        "jumlah": jumlah,
        "merk": merk,
        "harga": harga,
        "tanggal_pembelian": tanggal_pembelian
    }
    print("Barang berhasil ditambahkan!")

# Fungsi tanpa parameter untuk menampilkan semua barang
def lihat_barang():
    if inventory:
        for id_barang, item in inventory.items():
            print(f"ID: {id_barang}, Kategori: {item['kategori']}, Jumlah: {item['jumlah']}, "
                  f"Merk: {item['merk']}, Harga: {item['harga']}, Tanggal Pembelian: {item['tanggal_pembelian']}")
    else:
        print("Tidak ada barang dalam inventaris.")

# Fungsi dengan parameter untuk menghitung total nilai barang dalam inventaris
def hitung_nilai_barang():
    total_nilai = sum(item["harga"] * item["jumlah"] for item in inventory.values())  # variabel lokal
    print(f"Total nilai semua barang dalam inventaris: {total_nilai}")

# Prosedur untuk proses login
def login():
    global logged_in_user
    print("=== Login ===")
    username = input("Masukkan username: ")  # variabel lokal
    password = input("Masukkan password: ")  # variabel lokal

    if username in users and users[username]["password"] == password:
        logged_in_user = users[username]["role"]
        print(f"Login berhasil sebagai {logged_in_user}.")
    else:
        print("Login gagal. Username atau password salah.")
        logged_in_user = None

# Prosedur untuk mendaftar pengguna baru
def daftar():
    print("=== Mendaftar Pengguna Baru ===")
    username = input("Masukkan username baru: ")  # variabel lokal
    password = input("Masukkan password baru: ")  # variabel lokal

    if username and password:
        users[username] = {"password": password, "role": "user"}
        print("Pengguna baru berhasil didaftarkan!")
    else:
        print("Username dan password tidak boleh kosong.")

# Main Program
while True:
    print("\n=== Inventaris Properti Perusahaan ===")
    print("1. Mendaftar")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")  # variabel lokal

    if pilihan == "1":  # Mendaftar
        daftar()

    elif pilihan == "2":  # Login
        login()

        if logged_in_user == "admin":
            while True:
                print("\n=== Menu Admin ===")
                print("1. Tambah Barang")
                print("2. Lihat Barang")
                print("3. Total Barang")
                print("4. Hitung Nilai Barang")
                print("5. Logout")
                pilihan_admin = input("Masukkan pilihan: ")

                if pilihan_admin == "1":  # Tambah barang
                    print("=== Menambah Barang Baru ===")
                    try:
                        id_barang = int(input("Masukkan ID barang: "))  # variabel lokal
                        kategori = input("Masukkan kategori barang: ")  # variabel lokal
                        jumlah = int(input("Masukkan jumlah barang: "))  # variabel lokal
                        merk = input("Masukkan merk barang: ")  # variabel lokal
                        harga = float(input("Masukkan harga barang: "))  # variabel lokal
                        tanggal_pembelian = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")  # variabel lokal

                        # Memanggil fungsi tambah_barang
                        tambah_barang(id_barang, kategori, jumlah, merk, harga, tanggal_pembelian)
                    except ValueError:
                        print("Kesalahan: Pastikan ID, jumlah, dan harga diisi dengan benar.")

                elif pilihan_admin == "2":  # Lihat barang
                    lihat_barang()

                elif pilihan_admin == "3":  # Total Barang
                    total_barang()

                elif pilihan_admin == "4":  # Hitung nilai barang
                    hitung_nilai_barang()

                elif pilihan_admin == "5":  # Logout
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")
        
        elif logged_in_user == "user":
            while True:
                print("\n=== Menu Pengguna ===")
                print("1. Lihat Barang")
                print("2. Logout")
                pilihan_user = input("Masukkan pilihan: ")

                if pilihan_user == "1":  # Lihat barang (pengguna biasa)
                    lihat_barang()
                
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
