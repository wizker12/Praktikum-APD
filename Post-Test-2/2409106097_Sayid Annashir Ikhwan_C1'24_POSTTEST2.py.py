print("Masukan nama")
# memasukkan nama
nama = input()

# memasukkan NIM
print("Masukan NIM")
nIM = input()

# memasukkan harga gula sesuai diskon
print("Masukan Harga Gula")
hargagula = int(input())
hargadiskongulaku = hargagula * 0.07
hargadiskonmaniskita = hargagula * 0.11
hargadiskongunungmadu = hargagula * 0.13
hargasesudahdiskongulaku = hargagula - hargadiskongulaku
hargasesudahdiskonmaniskita = hargagula - hargadiskonmaniskita
hargasesudahdiskongunungmadu = hargagula - hargadiskongunungmadu
print("Harga diskon gulaku:")
print(hargasesudahdiskongulaku)
print("harga diskon maniskita:")
print(hargasesudahdiskonmaniskita)
print("Harga diskon gunung madu:")
print(hargasesudahdiskongunungmadu)
