# Program Pemesanan Tiket Bioskop

# 1. Meminta input nama dari user
nama = input("Masukkan nama Anda: ")

# 2. Meminta input nama hari dari user
hari = input("Hari apa yang ingin Anda pilih untuk menonton film? (Senin-Minggu): ")

# 3. Meminta input jumlah uang yang dimiliki user
uang = int(input("Berapa jumlah uang yang Anda miliki? Rp "))

# Menentukan harga tiket berdasarkan hari
if hari.lower() == "senin" or hari.lower() == "selasa" or hari.lower() == "rabu" or hari.lower() == "kamis":
    harga_tiket = 40000
elif hari.lower() == "jumat":
    harga_tiket = 45000
elif hari.lower() == "sabtu":
    harga_tiket = 55000
elif hari.lower() == "minggu":
    harga_tiket = 60000
else:
    harga_tiket = None

# Mengecek apakah hari valid
if harga_tiket is None:
    print(f"Hari {hari} tidak valid. Silakan masukkan hari yang benar (Senin-Minggu).")
else:
    # 4. Mengecek apakah uang cukup untuk membeli tiket
    if uang >= harga_tiket:
        print(f"Selamat {nama}, Anda bisa membeli tiket pada hari {hari.capitalize()}!")
    else:
        kekurangan = harga_tiket - uang
        print(f"Maaf {nama}, uang Anda kurang Rp {kekurangan} untuk membeli tiket pada hari {hari.capitalize()}.")
