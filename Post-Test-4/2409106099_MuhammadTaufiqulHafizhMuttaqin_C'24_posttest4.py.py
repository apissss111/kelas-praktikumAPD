# Membuat program login dengan looping jika salah 3x maka program akan berhenti dan jika benar akan lanjut ke pemesanan tiket bioskop 
#  (note : username harus sesuai dengan username di program, contoh "Hafizh" dan bukan "hafizh" harus sesuai dengan huruf perkapitalannya, jika benar maka langsung bisa memesan tiket, dan jika salah username/passwordnya. maka program akan looping 3x dan program akan berhenti)
username_valid = "Hafizh"
password_valid = "99"
attempts = 0
login_berhasil = False

# Proses login dengan maksimal 3 percobaan
while attempts < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan 3 digit terakhir NIM (contoh: 099 -> 99): ")

    if username == username_valid and password == password_valid:
        print("Login berhasil! Selamat datang, lanjutkan dengan pemesanan tiket.")
        login_berhasil = True
        break
    else:
        attempts += 1
        print(f"Login gagal. Kesempatan tersisa: {3 - attempts}")

# Jika login gagal 3 kali, program akan berhenti
if not login_berhasil:
    print("Login gagal 3 kali. Program akan berhenti.")
else:
    # Memasuki proses pemesanan tiket setelah login berhasil
    while True:
        # 1. Meminta input nama dari user
        nama = input("Masukkan nama Anda: ")

        # 2. Meminta input nama hari dari user
        hari = input("Hari apa yang ingin Anda pilih untuk menonton film? (Senin-Minggu): ").lower()

        # 3. Meminta input jumlah uang yang dimiliki user
        uang = input("Berapa jumlah uang yang Anda miliki? Rp ")
        
        # Memeriksa apakah input uang hanya berupa angka
        if uang.isdigit():
            uang = int(uang)  # Mengubah uang menjadi tipe integer jika input valid
        else:
            print("Jumlah uang harus berupa angka! Coba lagi.")
            continue

        # Menentukan harga tiket berdasarkan hari
        if hari in ["senin", "selasa", "rabu", "kamis"]:
            harga_tiket = 40000
        elif hari == "jumat":
            harga_tiket = 45000
        elif hari == "sabtu":
            harga_tiket = 55000
        elif hari == "minggu":
            harga_tiket = 60000
        else:
            print(f"Hari {hari.capitalize()} tidak valid. Silakan masukkan hari yang benar (Senin-Minggu).")
            continue

        # 4. Mengecek apakah uang cukup untuk membeli tiket
        if uang >= harga_tiket:
            print(f"Selamat {nama}, Anda bisa membeli tiket pada hari {hari.capitalize()}!")
        else:
            kekurangan = harga_tiket - uang
            print(f"Maaf {nama}, uang Anda kurang Rp {kekurangan} untuk membeli tiket pada hari {hari.capitalize()}.")

        # Menanyakan apakah user ingin melanjutkan atau berhenti
        lanjutkan = input("Apakah Anda ingin memesan tiket lagi? (ya/tidak): ").lower()
        if lanjutkan != "ya":
            print("Terima kasih telah menggunakan layanan pemesanan tiket bioskop kami !")
            break
