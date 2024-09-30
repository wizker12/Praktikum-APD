username = "Sayid"
password = 97
loop = 0
while loop < 3:
    print("Harap Masukkan Username anda tuan")
    # memasukan Username
    username = input()
    print("Masukkan password anda tuan")
    # memasukan paassword
    password = int(input())
    if username == "Sayid" and password == 97:
        print("Apakah Tuan ingin lanjut?")
        lanjut = input()
        if lanjut == "ga lanjut":
            print("Progam di hentikan")
        else:
            print("Baik tuan anda berhasil masuk")

        print("Selamat datang di bioskop mulawarman online ")
        print("Ingin nonton apa tuan?")
        # memasukan film yang ingin ditonton
        print("Disini tersedia film :")
        print("1.One piece Stampade 2.One piece Z 3.One piece Gold")
        print("Silahkan dipilih tuan :)")
        nonton = input()
        print("Ingin menonton hari apa tuan?")
        # memasukan hari yang ingin ditonton 
        hari = input()
        print("Uang yang dimiliki berapa tuan?")
        # memasukan nominal
        nominaluang = int(input())
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
            if nominaluang >= 40000:
                print("baikk tuann anda dapat membeli tiket di hari:")
                print(hari)
                print(nonton)
                break
            else:
                print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                print(hari)
                print(nonton)
                break
        else:
            if hari == "jumat":
                if nominaluang >= 45000:
                    print("baikk tuann anda dapat membeli tiket di hari:")
                    print(hari)
                    break
                else:
                    print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                    print(hari)
                    break
            else:
                if hari == "sabtu":
                    if nominaluang >= 55000:
                        print("baikk tuann anda dapat membeli tiket di hari:")
                        print(hari)
                        break
                    else:
                        print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                        print(hari)
                        break
                else:
                    if hari == "minggu":
                        if nominaluang >= 60000:
                            print("baikk tuann anda dapat membeli tiket di hari")
                            print(hari)
                            break
                        else:
                            print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                            print(hari)
                            break
    else:
        print("Maaf tuan,username atau password yang tuan masukan salah.apakah tuan ingin lanjut?")
        lanjut = input()
        if lanjut == "Iya":
            print("Progam tuan di hentikan")
        else:
            loop = loop + 1
            print("Maaf tuan anda sudah mencoba sebanyak")
            print(loop)
