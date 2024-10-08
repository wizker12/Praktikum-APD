import os


pengguna = [["admin", "admin123", "admin"]]

TiketKereta = [
    ["Stasiun Gear", "Samarinda-Balikpapan", 150000, 7],
    ["Stasiun ISO", "Samarinda-Banjarmasin", 280000, 5],
    ["Stasiun Unmul", "Balikpapan-Palangkaraya", 500000, 3]
]


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
        
        # Memilih menu tampilan awal


        if pilihan == "1":
            os.system('cls || clear')
            print("=" * 45, "\n\t\tSilahkan Login tuan\n", "=" * 45)
            Username = input("Username: ")   # Memasukan Username yang sudah di daftar
            Password = input("Kata Sandi: ") # Memasukan kata sandi yang sudah di daftar

            
            for user in pengguna:
                if user[0] == Username and user[1] == Password:
                    KonfirmasiLogin = True
                    User = user[0]
                    Role = user[2]
                    print(f"Kamu Berhasil Masuk Dengan Role {Role}")
                    input("Tekan enter untuk Manjutkan >_<1")
                    break
            
            if not KonfirmasiLogin:
                print("Username atau kata sandi anda salah!")
                input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2":
            os.system('cls || clear')
            print("\tMenu Pendaftaran\n", "=" * 35)
            UsernameBaru = input("Username baru: ") # Memasukan Username yang ingin di daftar
            
            UsernameTersedia = False
            for user in pengguna:
                if user[0] == UsernameBaru:
                    UsernameTersedia = True
                    print("Username sudah digunakan!")
                    input("Tekan enter untuk Manjutkan >_<1")
                    break
            
            if not UsernameTersedia:
                Password_baru = input("Kata Sandi baru: ") # Memasukan Kata sandi yang ingin di daftar
                pengguna.append([UsernameBaru, Password_baru, "penumpang"])
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
        print(f"\n\tWelcome {Role} >_<")  # Tampilan awal untuk menu daftar tiket kereta api
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
            for tiket in TiketKereta:
                nama, rute, harga, sisa = tiket
                print(f"{nama:<20} {rute:<25} {harga:<15,} {sisa:<10}")
            input("\nTekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2" and Role == "admin":  
            os.system('cls || clear')
            print("\n=== Tambah Tiket ===") # Menambahkan tiket untuk pengguna admin
            nama = input("Nama kereta: ")
            rute = input("Rute perjalanan: ")
            harga = int(input("Harga tiket (dalam IDR): "))
            sisa = int(input("Jumlah tiket tersedia: "))
            TiketKereta.append([nama, rute, harga, sisa])
            print("Tiket berhasil ditambahkan!")
            input("Tekan enter untuk Manjutkan >_<1")
            
        elif pilihan == "3" and Role == "admin": 
            os.system('cls || clear')
            print("\tPerbarui Informasi Tiket") # Mengupdate informasi tiket untuk para pengguna
            print("=" * 45, "\nDaftar Tiket:")
            for i, tiket in enumerate(TiketKereta, 1):
                print(f"{i}. {tiket[0]} - {tiket[1]}")
            
            index = int(input("\nPilih nomor tiket yang akan diperbarui: ")) - 1 # Mempebarui tiket
            if 0 <= index < len(TiketKereta):
                nama = input("Nama kereta baru (kosongkan jika tidak ingin diubah): ")
                rute = input("Rute baru (kosongkan jika tidak ingin diubah): ")
                harga = input("Harga baru (kosongkan jika tidak ingin diubah): ")
                sisa = input("Jumlah tiket tersedia baru (kosongkan jika tidak ingin diubah): ")
                
                if nama:
                    TiketKereta[index][0] = nama
                if rute:
                    TiketKereta[index][1] = rute
                if harga:
                    TiketKereta[index][2] = int(harga)
                if sisa:
                    TiketKereta[index][3] = int(sisa)
                print("Informasi tiket berhasil diperbarui!")
            else:
                print("Nomor tiket tidak valid!")
            input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "4" and Role == "admin": 
            os.system('cls || clear')
            print("\n=== Hapus Tiket ===") # Menghapus daftar tiket yang ingin dihapus
            print("Daftar Tiket:")
            for i, tiket in enumerate(TiketKereta, 1):
                print(f"{i}. {tiket[0]} - {tiket[1]}")
            
            index = int(input("\nPilih nomor tiket yang akan dihapus: ")) - 1
            if 0 <= index < len(TiketKereta):
                hapus = TiketKereta.pop(index)
                print(f"Tiket '{hapus[0]}' rute {hapus[1]} berhasil dihapus!")
            else:
                print("Nomor tiket tidak valid!")
            input("Tekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "2" and Role == "penumpang":
            os.system('cls || clear')
            print("\n=== Beli Tiket ===") # Membeli tiket kereta api
            print("Tiket Tersedia:")
            for i, tiket in enumerate(TiketKereta, 1):
                if tiket[3] > 0:
                    print(f"{i}. {tiket[0]} - {tiket[1]} - Harga: Rp{tiket[2]:,} - Sisa: {tiket[3]}")
            
            index = int(input("\nPilih nomor tiket yang ingin dibeli: ")) - 1
            if 0 <= index < len(TiketKereta) and TiketKereta[index][3] > 0:
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                if jumlah_tiket <= TiketKereta[index][3]:
                    total_harga = TiketKereta[index][2] * jumlah_tiket
                    TiketKereta[index][3] -= jumlah_tiket
                    print(f"Anda telah membeli {jumlah_tiket} tiket {TiketKereta[index][0]} rute {TiketKereta[index][1]}.")
                    print(f"Total harga: Rp{total_harga:,}")
                    
                    if User not in RiwayatPembelian:
                        RiwayatPembelian[User] = []
                    RiwayatPembelian[User].append([TiketKereta[index][0], TiketKereta[index][1], jumlah_tiket, total_harga])
                    
                else:
                    print(f"Maaf, hanya tersedia {TiketKereta[index][3]} tiket.")
            else:
                print("Nomor tiket tidak valid atau tiket habis!")
            input("Tekan enter untuk Manjutkan >_<1")
        
        elif pilihan == "3" and Role == "penumpang":
            os.system('cls || clear')
            print("\n=== Riwayat Pembelian ===")  # Mengecek riwayat pembelian yang sudah di beli
            if User in RiwayatPembelian and RiwayatPembelian[User]:
                for i, pembelian in enumerate(RiwayatPembelian[User], 1):
                    print(f"{i}. {pembelian[0]} - {pembelian[1]} - Jumlah: {pembelian[2]} - Total: Rp{pembelian[3]:,}")
            else:
                print("Anda belum memiliki riwayat pembelian.")
            input("\nTekan enter untuk Manjutkan >_<1")
                
        elif pilihan == "0": 
            KonfirmasiLogin = False
            User = ""
            Role = ""
            print("Anda Telah Keluar.")
            input("Tekan enter untuk Manjutkan >_<1")
            
        else:
            print("Pilihan tidak valid!")
            input("Tekan enter untuk Lanjutkan >_<1")