print("Menghitung BMI")
berat = float(input("Masukkan Berat Badan Anda: "))
tinggi = float(input("Masukkan Tinggi Badan Anda (dalam meter): "))
bmi = berat / tinggi**2
print("Hasil Perhitungan: ", bmi)
if bmi < 18.5:
    print("Berat Badan Anda Kurang")
elif bmi <= 22.9:
    print("Berat Badan Normal")
elif bmi >= 29.9:
    print("Berat Badan Berlebih (Cenderung Obesitas)")
elif bmi >= 30:
    print("Obesitas")
