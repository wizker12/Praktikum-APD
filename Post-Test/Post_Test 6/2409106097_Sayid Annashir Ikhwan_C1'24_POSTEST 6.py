import os

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
            os.system('cls || clear')
            print("=" * 45, "\n\t\tSilahkan Login tuan\n", "=" * 45)
            Username = input("Username: ")
            Password = input("Kata Sandi: ")

            if Username in pengguna and pengguna[Username]["password"] == Password:
                KonfirmasiLogin = True
                User = Username
                Role = pengguna[Username]["role"]
                print(f"Kamu Berhasil Masuk Dengan Role {Role}")
                input("Tekan enter untuk Manjutkan >_<1")
            else:
                print("Username atau kata sandi anda salah!")
                input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2":
            os.system('cls || clear')
            print("\tMenu Pendaftaran\n", "=" * 35)
            UsernameBaru = input("Username baru: ")

            if UsernameBaru in pengguna:
                print("Username sudah digunakan!")
                input("Tekan enter untuk Manjutkan >_<1")
            else:
                Password_baru = input("Kata Sandi baru: ")
                pengguna[UsernameBaru] = {"password": Password_baru, "role": "penumpang"}
                RiwayatPembelian[UsernameBaru] = []
                print("Pendaftaran berhasil! Anda terdaftar sebagai penumpang.")
                input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami. Semoga harimu menyenangkan >_<.")
            break
        else:
            print("Mohon dipilih dulu -_-<")
            input("Tekan enter untuk Manjutkan >_<")
            
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
            os.system('cls || clear')
            print("\nDaftar Tiket Tersedia:")
            print(f"{'Nama Kereta':<20} {'Rute':<25} {'Harga (IDR)':<15} {'Sisa Tiket':<10}")
            print("=" * 70)
            for tiket in TiketKereta.values():
                print(f"{tiket['nama']:<20} {tiket['rute']:<25} {tiket['harga']:<15,} {tiket['sisa']:<10}")
            input("\nTekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2" and Role == "admin":  
            os.system('cls || clear')
            print("\n=== Tambah Tiket ===")
            nama = input("Nama kereta: ")
            rute = input("Rute perjalanan: ")
            harga = int(input("Harga tiket (dalam IDR): "))
            sisa = int(input("Jumlah tiket tersedia: "))
            id_tiket_baru = max(TiketKereta.keys()) + 1
            TiketKereta[id_tiket_baru] = {"nama": nama, "rute": rute, "harga": harga, "sisa": sisa}
            print("Tiket berhasil ditambahkan!")
            input("Tekan enter untuk Manjutkan >_<1")
            
        elif pilihan == "3" and Role == "admin": 
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
            input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "4" and Role == "admin": 
            os.system('cls || clear')
            print("\n=== Hapus Tiket ===")
            print("Daftar Tiket:")
            for i, tiket in TiketKereta.items():
                print(f"{i}. {tiket['nama']} - {tiket['rute']}")
            
            index = int(input("\nPilih nomor tiket yang akan dihapus: "))
            if index in TiketKereta:
                hapus = TiketKereta.pop(index)
                print(f"Tiket '{hapus['nama']}' rute {hapus['rute']} berhasil dihapus!")
            else:
                print("Nomor tiket tidak valid!")
            input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2" and Role == "penumpang":
            os.system('cls || clear')
            print("\n=== Beli Tiket ===")
            print("Tiket Tersedia:")
            for i, tiket in TiketKereta.items():
                if tiket["sisa"] > 0:
                    print(f"{i}. {tiket['nama']} - {tiket['rute']} - Harga: Rp{tiket['harga']:,} - Sisa: {tiket['sisa']}")
            
            index = int(input("\nPilih nomor tiket yang ingin dibeli: "))
            if index in TiketKereta and TiketKereta[index]["sisa"] > 0:
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                if jumlah_tiket <= TiketKereta[index]["sisa"]:
                    total_harga = TiketKereta[index]["harga"] * jumlah_tiket
                    TiketKereta[index]["sisa"] -= jumlah_tiket
                    print(f"Anda telah membeli {jumlah_tiket} tiket {TiketKereta[index]['nama']} rute {TiketKereta[index]['rute']}.")
                    print(f"Total harga: Rp{total_harga:,}")
                    
                    if User not in RiwayatPembelian:
                        RiwayatPembelian[User] = []
                    RiwayatPembelian[User].append({"nama": TiketKereta[index]["nama"], "rute": TiketKereta[index]["rute"], "jumlah": jumlah_tiket, "total_harga": total_harga})
                    
                else:
                    print(f"Maaf, hanya tersedia {TiketKereta[index]['sisa']} tiket.")
            else:
                print("Nomor tiket tidak valid atau tiket habis!")
            input("Tekan enter untuk Manjutkan >_<1")
        
        elif pilihan == "3" and Role == "penumpang":
            os.system('cls || clear')
            print("\n=== Riwayat Pembelian ===")
            if User in RiwayatPembelian and RiwayatPembelian[User]:
                for i, pembelian in enumerate(RiwayatPembelian[User], 1):
                    print(f"{i}. {pembelian['nama']} - {pembelian['rute']} - Jumlah: {pembelian['jumlah']} - Total: Rp{pembelian['total_harga']:,}")
            else:
                print("Anda belum memiliki riwayat pembelian.")
            input("\nTekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "0": 
            KonfirmasiLogin = False
            User = ""
            Role = ""
            print("Anda Telah Keluar.")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan enter untuk Lanjutkan >_<1")
