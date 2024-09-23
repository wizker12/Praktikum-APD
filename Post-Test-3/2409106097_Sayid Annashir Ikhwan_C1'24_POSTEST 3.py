print("Masukan Nama mu")
# memasukan Nama 
nama = input()

print("Selamat datang di bioskop mulawarman online ")
print("Ingin nonton apa tuan?")
print("Disini tersedia film :")
print("1.One piece Stampade 2.One piece Z 3.One piece Gold")
# memasukan film yang ingin ditonton
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
    else:
        print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
        print(hari)
else:
    if hari == "jumat":
        if nominaluang >= 45000:
            print("baikk tuann anda dapat membeli tiket di hari:")
            print(hari)
        else:
            print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
            print(hari)
    else:
        if hari == "sabtu":
            if nominaluang >= 55000:
                print("baikk tuann anda dapat membeli tiket di hari:")
                print(hari)
            else:
                print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                print(hari)
        else:
            if hari == "minggu":
                if nominaluang >= 60000:
                    print("baikk tuann anda dapat membeli tiket di hari")
                    print(hari)
                else:
                    print("Maaf tuan, uang anda tidak cukup untuk membeli tiket di hari")
                    print(hari)
