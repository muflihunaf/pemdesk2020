data = ['firman','helloworld']
kondisi = True
coba = 1
while kondisi:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username == data[0] and password == data[1]:
        print("Anda Berhasil Masuk")
        kondisi = False
    else:
        print("Maaf Username Atau Password Anda Salah")
        coba += 1
        if coba > 3:
            print("Anda Salah Memasukkan lebih dari 3 Kali")
            break
