import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QHBoxLayout,QGroupBox,QVBoxLayout, QGridLayout,QTextEdit,QLineEdit
app = QApplication(sys.argv)
window = QWidget()
#membuat fungsi utk menentukan layout window
def window_go(app):
   #inisialisasi pyqt   
   # Menginisiasi GridLayout
   GLayout = QGridLayout()
   # Menambahkan Widget GroupBox Ke gridLayout
   GLayout.addLayout(topLayout(window),0,0,1 ,2) 
   GLayout.addWidget(inputSuhu(window),1,0,1,0)
   GLayout.addWidget(group4(window), 2, 0,1,2)
   # Menset agar jarak tidak terlalu renggang 
   GLayout.setRowStretch(2,1)
   GLayout.setRowStretch(3,1)

   # Menset Layout Utama Ke GridLayout
   window.setLayout(GLayout)
   # Mensetting Ukuran Aplikasinya
   window.setGeometry(100,100,500,500)
   # Menset Judul Aplikasi
   window.setWindowTitle("Refleksi")
   window.show()

# Memcah Fungsi Untuk Beberapa Bagian, TopLayout Merupakan FUngsi Untuk Tampilan bagian Atas
def topLayout(window):
    # Membuat Judul Dibagian Atas
    label = QLabel("Aplikasi Konversi Suhu")
    # Mengubah Font Judul
    label.setStyleSheet("font-family: roboto; ")
    # Mensetting Align nya agar berada Ditengah
    label.setAlignment(Qt.AlignCenter)
    # Membuat Vertical Layout Dan Menambahkan Widget Nya
    layout1 = QVBoxLayout()
    layout1.addWidget(label)
    # Mereturn/mengembalikan nilai layout nya karena kita butuh layoutnya untuk ditambahkan ke gridLayout nya
    return layout1
def inputSuhu(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Suhu Yang Dikonversi", window)
    # Membuat Widget Label
    label = QLabel("Besarnya Suhu Dalam Celcius")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/ membuat variabel suhu tidak menjadi lokal lagi
    global suhu
    # Membuat Widget Inputan 
    suhu = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Konversi")

    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(lambda x: dipencet(suhu))
    
    # Membuat Horizontal Layout Dan Menambahkan widget
    layout1 = QHBoxLayout()
    layout1.addWidget(label)
    layout1.addWidget(suhu)
    layout1.addWidget(btn)

    groupbox.setLayout(layout1)
    return groupbox

# Rumus Perhitungan 
def dipencet(suhu):
    # mengambil hasil inputan user dan dimasuukan ke variabel value
    value = suhu.text()
    # Menampilkan inputan ke Widget suhu celcius
    celcius.setText(value)
    # Menghitung Suhu Dan Menampilkannya ke widget
    hasilR = str(4/5 * float(value))
    reamur.setText(hasilR)

    hasilF = str(9/5 * float(value) + 32)
    fahrenheit.setText(hasilF)

    hasilK = str(float(value) + 273)
    kelvin.setText(hasilK)
    # Membuat Inputan Menjadi Kosong
    suhu.setText("")
def group4(window):
    # Membuat Groupbox
    groupbox = QGroupBox("Hasil Konversi")
    # Membuat Widget Label
    label = QLabel("Reamur")
    # membuat variabel Reamur Menjadi Global/agar bisa diakses fungsi Lain
    global reamur
    # Membuat Widget QLineEdit
    reamur = QLineEdit("",window)
    # Mensetting agar QLineEdit tidak bisa diinput/hanya bisa dibaca
    reamur.setReadOnly(True)

    Lcel = QLabel("Celcius")
    global celcius
    celcius = QLineEdit("",window)
    celcius.setReadOnly(True)

    LFahrenheit = QLabel("Fahrenheit")
    global fahrenheit
    fahrenheit = QLineEdit()
    fahrenheit.setReadOnly(True)

    Lkelvi = QLabel("Kelvin: ")
    global kelvin
    kelvin = QLineEdit("")
    kelvin.setReadOnly(True)

    # Membuat GridLayout Dan Menambahkan Widget nya
    grid = QGridLayout()
    grid.addWidget(Lcel,0,0)
    grid.addWidget(celcius,0,1)
    
    grid.addWidget(label,1,0)
    grid.addWidget(reamur,1,1)

    grid.addWidget(Lkelvi,2,0)
    grid.addWidget(kelvin,2,1)

    grid.addWidget(LFahrenheit,3,0)
    grid.addWidget(fahrenheit,3,1)
    grid.setRowStretch(4,5)
    groupbox.setLayout(grid)
    return groupbox
def close():
    print("halo")
if __name__ == '__main__':
   window_go(app)
 