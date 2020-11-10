import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QHBoxLayout,QGroupBox,QVBoxLayout, QGridLayout,QLineEdit, QFormLayout
app = QApplication(sys.argv)
window = QWidget()

# Memcah Fungsi Untuk Beberapa Bagian, TopLayout Merupakan FUngsi Untuk Tampilan bagian Atas
def topLayout(window):
    # Membuat Judul Dibagian Atas
    label = QLabel("Aplikasi Menghitung Kecepatan")
    # Mengubah Font Judul
    label.setStyleSheet("font-family: roboto; ")
    # Mensetting Align nya agar berada Ditengah
    label.setAlignment(Qt.AlignCenter)
    # Membuat Vertical Layout Dan Menambahkan Widget Nya
    layout1 = QVBoxLayout()
    layout1.addWidget(label)
    # Mereturn/mengembalikan nilai layout nya karena kita butuh layoutnya untuk ditambahkan ke gridLayout nya
    return layout1
def hitungKecepatan(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Kecepatan", window)
    # Membuat Widget Label
    labelJarak = QLabel("Jarak: ")
    labelWaktu = QLabel("Waktu: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/ membuat variabel suhu tidak menjadi lokal lagi
    global jarak, waktu
    # Membuat Widget Inputan 
    jarak = QLineEdit()
    waktu = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")

    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(kecepatan)
    
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelJarak,jarak)
    layout1.addRow(labelWaktu,waktu)
    layout1.addRow(btn)

    groupbox.setLayout(layout1)
    return groupbox
def kecepatan():
    try:
        vJarak = jarak.text()
        vWaktu = waktu.text()
        hCepat = float(vJarak) / float(vWaktu)
        hasilKeceptan.setText(str(hCepat))
    except ValueError:
        jarak.setText("Bukan Angka")
    
# Rumus Perhitungan 
def hitungJarak(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Jarak", window)
    # Membuat Widget Label
    labelKeceptan = QLabel("Kecepatan: ")
    labelWaktu = QLabel("Waktu: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/ membuat variabel suhu tidak menjadi lokal lagi
    global cepetan, waktu2
    # Membuat Widget Inputan 
    cepetan = QLineEdit()
    waktu2 = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")

    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(totalJarak)
    
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelKeceptan,cepetan)
    layout1.addRow(labelWaktu,waktu2)
    layout1.addRow(btn)

    groupbox.setLayout(layout1)
    return groupbox
def totalJarak():
    try:
        vCepat = cepetan.text()
        vWaktu = waktu2.text()
        hJarak = float(vCepat) * float(vWaktu)
        hasilJarak.setText(str(hJarak))
    except ValueError:
        pass
def hitungWaktu(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Waktu", window)
    # Membuat Widget Label
    labelJarak = QLabel("Jarak: ")
    labelkecepatan = QLabel("kecepatan: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/ membuat variabel suhu tidak menjadi lokal lagi
    global jarak2, cepetan2
    # Membuat Widget Inputan 
    jarak2 = QLineEdit()
    cepetan2 = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")

    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(totalWaktu)
    
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelJarak,jarak2)
    layout1.addRow(labelkecepatan,cepetan2)
    layout1.addRow(btn)

    groupbox.setLayout(layout1)
    return groupbox
def totalWaktu():
    try:
        vJarak = jarak2.text()
        vCepat = cepetan2.text()
        hWaktu = float(vJarak) / float(vCepat)
        hasilWaktu.setText(str(hWaktu))
    except ValueError:
        pass
def Tampil(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Hasil Operasi", window)
    # Membuat Widget Label
    labelJarak = QLabel("Jarak: ")
    labelWaktu = QLabel("kecepatan: ")
    labelKecepatan = QLabel("kecepatan: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/ membuat variabel suhu tidak menjadi lokal lagi
    global hasilJarak, hasilWaktu,hasilKeceptan
    # Membuat Widget Inputan 
    hasilJarak = QLineEdit()
    hasilJarak.setReadOnly(True)
    hasilWaktu = QLineEdit()
    hasilWaktu.setReadOnly(True)
    hasilKeceptan = QLineEdit()
    hasilKeceptan.setReadOnly(True)
    
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelJarak,hasilJarak)
    layout1.addRow(labelWaktu,hasilWaktu)
    layout1.addRow(labelKecepatan,hasilKeceptan)

    groupbox.setLayout(layout1)
    return groupbox


def window_go(app):
   
   # Menginisiasi GridLayout
   GLayout = QGridLayout()
   # Menambahkan Widget GroupBox Ke gridLayout
   GLayout.addLayout(topLayout(window),0,0,1 ,2) 
   GLayout.addWidget(hitungKecepatan(window),1,0,1,0)
   GLayout.addWidget(hitungJarak(window), 2, 0,1,0)
   GLayout.addWidget(hitungWaktu(window), 3, 0,1,0)
   GLayout.addWidget(Tampil(window), 4, 0,1,0)
   # Menset agar jarak tidak terlalu renggang 
   GLayout.setRowStretch(2,1)
   GLayout.setRowStretch(3,1)
   # Menset Layout Utama Ke GridLayout
   window.setLayout(GLayout)
   
   # Mensetting Ukuran Aplikasinya
   window.setGeometry(100,100,500,500)
   # Menset Judul Aplikasi
   window.setWindowTitle("Menghitung Kecepatan")
   window.show()



if __name__ == '__main__':
   window_go(app)