import os

# Variabel Global
pengguna = {
    "admin": {"password": "admin123", "role": "admin"}
}
TiketKereta = {
    1: {"nama": "Stasiun Gear", "rute": "Samarinda-Balikpapan", "harga": 150000, "sisa": 7},
    2: {"nama": "Stasiun ISO", "rute": "Samarinda-Banjarmasin", "harga": 280000, "sisa": 5},
    3: {"nama": "Stasiun Unmul", "rute": "Balikpapan-Palangkaraya", "harga": 500000, "sisa": 3}
}
RiwayatPembelian = {}

KonfirmasiLogin = False
User = ""
Role = ""

# Prosedur
def daftar_pengguna():
    global pengguna, RiwayatPembelian
    os.system('cls || clear')
    print("\tMenu Pendaftaran\n", "=" * 35)
    UsernameBaru = input("Username baru: ")

    if UsernameBaru in pengguna:
        print("Username sudah digunakan!")
    else:
        Password_baru = input("Kata Sandi baru: ")
        pengguna[UsernameBaru] = {"password": Password_baru, "role": "penumpang"}
        RiwayatPembelian[UsernameBaru] = []
        print("Pendaftaran berhasil! Anda terdaftar sebagai penumpang.")
    input("Tekan enter untuk Melanjutkan >_<1")

# Fungsi tanpa parameter
def tampilkan_tiket_tersedia():
    os.system('cls || clear')
    print("\nDaftar Tiket Tersedia:")
    print(f"{'Nama Kereta':<20} {'Rute':<25} {'Harga (IDR)':<15} {'Sisa Tiket':<10}")
    print("=" * 70)
    for tiket in TiketKereta.values():
        print(f"{tiket['nama']:<20} {tiket['rute']:<25} {tiket['harga']:<15,} {tiket['sisa']:<10}")
    input("\nTekan enter untuk Melanjutkan >_<1")

# Fungsi dengan parameter
def beli_tiket(username, id_tiket, jumlah_tiket):
    global TiketKereta, RiwayatPembelian
    if id_tiket in TiketKereta and TiketKereta[id_tiket]["sisa"] >= jumlah_tiket:
        total_harga = TiketKereta[id_tiket]["harga"] * jumlah_tiket
        TiketKereta[id_tiket]["sisa"] -= jumlah_tiket
        RiwayatPembelian[username].append({
            "nama": TiketKereta[id_tiket]["nama"], 
            "rute": TiketKereta[id_tiket]["rute"], 
            "jumlah": jumlah_tiket, 
            "total_harga": total_harga
        })
        print(f"Anda telah membeli {jumlah_tiket} tiket {TiketKereta[id_tiket]['nama']} rute {TiketKereta[id_tiket]['rute']}.")
        print(f"Total harga: Rp{total_harga:,}")
    else:
        print(f"Maaf, jumlah tiket tidak mencukupi atau tiket tidak ditemukan!")

# Fungsi rekursif
def tampilkan_tiket_rekursif(index=0):
    if index < len(TiketKereta):
        tiket = TiketKereta[index + 1]
        print(f"{index + 1}. {tiket['nama']} - {tiket['rute']} - Harga: Rp{tiket['harga']:,} - Sisa: {tiket['sisa']}")
        return tampilkan_tiket_rekursif(index + 1)

# Prosedur dengan input error handling
def login():
    global KonfirmasiLogin, User, Role
    try:
        os.system('cls || clear')
        print("=" * 45, "\n\t\tSilahkan Login tuan\n", "=" * 45)
        Username = input("Username: ")
        Password = input("Kata Sandi: ")
        
        if Username in pengguna and pengguna[Username]["password"] == Password:
            KonfirmasiLogin = True
            User = Username
            Role = pengguna[Username]["role"]
            print(f"Kamu Berhasil Masuk Dengan Role {Role}")
        else:
            print("Username atau kata sandi anda salah!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        input("Tekan enter untuk Melanjutkan >_<1")

# Fungsi lain
def perbarui_tiket():
    global TiketKereta
    try:
        os.system('cls || clear')
        print("\tPerbarui Informasi Tiket")
        print("=" * 45, "\nDaftar Tiket:")
        for i, tiket in TiketKereta.items():
            print(f"{i}. {tiket['nama']} - {tiket['rute']}")
        
        index = int(input("\nPilih nomor tiket yang akan diperbarui: "))
        if index in TiketKereta:
            nama = input("Nama kereta baru (kosongkan jika tidak ingin diubah): ")
            rute = input("Rute baru (kosongkan jika tidak ingin diubah): ")
            harga = input("Harga baru (kosongkan jika tidak ingin diubah): ")
            sisa = input("Jumlah tiket tersedia baru (kosongkan jika tidak ingin diubah): ")
            
            if nama:
                TiketKereta[index]["nama"] = nama
            if rute:
                TiketKereta[index]["rute"] = rute
            if harga:
                TiketKereta[index]["harga"] = int(harga)
            if sisa:
                TiketKereta[index]["sisa"] = int(sisa)
            print("Informasi tiket berhasil diperbarui!")
        else:
            print("Nomor tiket tidak valid!")
    except ValueError:
        print("Input tidak valid, harap masukkan angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        input("Tekan enter untuk Melanjutkan >_<1")

# Menu Utama
while True:
    if not KonfirmasiLogin:
        os.system('cls || clear')
        print("======================================================================")
        print("\tSelamat datang di pembelian tiket stasiun Mulawarman >_<")
        print("\tApa yang bisa saya bantu >_<")
        print("======================================================================")
        print("1. Masuk\n2. Daftar\n3. Keluar") 
        
        pilihan = input("Pilih menu anda tuan: ")
        
        if pilihan == "1":
            login()
        elif pilihan == "2":
            daftar_pengguna()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami. Semoga harimu menyenangkan >_<.")
            break
        else:
            print("Mohon dipilih dulu -_-<")
            input("Tekan enter untuk Melanjutkan >_<")
            
    else:  
        os.system('cls || clear')
        print("=" * 45)
        print(f"\n\tWelcome {Role} >_<")
        print("=" * 45)
        print("1. Lihat Tiket Tersedia")
        if Role == "admin":
            print("2. Tambah Tiket")
            print("3. Perbarui Informasi Tiket")
            print("4. Hapus Tiket")
        elif Role == "penumpang":
            print("2. Beli Tiket\n3. Lihat Riwayat Pembelian")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkan_tiket_tersedia()
        elif pilihan == "2" and Role == "penumpang":
            try:
                os.system('cls || clear')
                print("\n=== Beli Tiket ===")
                tampilkan_tiket_rekursif()
                id_tiket = int(input("\nPilih nomor tiket yang ingin dibeli: "))
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                beli_tiket(User, id_tiket, jumlah_tiket)
            except ValueError:
                print("Input tidak valid, masukkan angka yang benar!")
            input("Tekan enter untuk Melanjutkan >_<1")
        elif pilihan == "3" and Role == "admin":
            perbarui_tiket()
        elif pilihan == "0":
            KonfirmasiLogin = False
            User = ""
            Role = ""
            print("Anda Telah Keluar.")
        else:
            print("Pilihan tidak valid!")
            input("Tekan enter untuk Melanjutkan >_<1")