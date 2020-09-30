bil = []

banyak = int(input("Masukkan Berapa Jumlah Yang Ingin Diinputkan"))
for i in range(banyak):
    nomor = int(input("Masukkan Angka: "))
    bil.append(nomor)

print("Bilangan Yang Diinputkan", bil)
for i in range(len(bil)):
    for j in range(i+1, len(bil)):
        if bil[i] > bil[j]:
            bil[i],bil[j] = bil[j],bil[i]

print("Nilai Minimum", bil[0])
print("Nilai Maksimal: ", bil[-1])

