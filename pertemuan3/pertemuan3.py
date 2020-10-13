import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QApplication,QCheckBox,QRadioButton

# Membuat Class Tampilan
class Tampilan(QWidget):

    # Membuat Sebuah Konstruktor
    def __init__(self):
        super().__init__()

        # Memanggil Method tampilan()
        self.tampilan()

    #membuat method/fungsi tampilan
    def tampilan(self):
        #Membuat Label
        judul = QLabel('Input Biodata')
        nama = QLabel('Nama')
        alamat = QLabel('Address')
        hobby = QLabel('Hobby')
        status = QLabel('Status')

        # memanipulasi tampilan Label
        judul.setStyleSheet("font-size: 30px;color:red;background: cyan; font-weight: bold")

        # membuat checkbox
        cbutton = QCheckBox('Makan')
        cbutton1 = QCheckBox('Tidur')
        cbutton2 = QCheckBox('Main')

        # Membuat Sebuah Textbox/Line Edit
        editnama = QLineEdit()
        editAddress = QLineEdit()
        editAddress1 = QLineEdit()

        # Membuat Radio Button
        radio1 = QRadioButton("Pelajar")
        radio2 = QRadioButton("Mahasiswa")
        radio3 = QRadioButton("Wiraswasta")

        # Membuat Grid Layout
        grid = QGridLayout()
        # memanipulasi baris agar keatas
        grid.setRowStretch(10,1)
        # membuat spasi diantara item
        grid.setSpacing(5)

        # menambahkan widget ke layout grid
        grid.addWidget(judul, 0, 0,1,0)
        grid.addWidget(nama, 1, 0)
        grid.addWidget(editnama, 1, 1)

        grid.addWidget(alamat, 2, 0)
        grid.addWidget(editAddress, 2, 1)
        grid.addWidget(editAddress1, 3, 1)
        
        grid.addWidget(hobby, 4, 0)
        grid.addWidget(cbutton, 4, 1)
        grid.addWidget(cbutton1, 5, 1)
        grid.addWidget(cbutton2, 6, 1)

        grid.addWidget(status, 7, 0)
        grid.addWidget(radio1, 7, 1)
        grid.addWidget(radio2, 8, 1)
        grid.addWidget(radio3, 9, 1)

        # mengeset layout dalam bentuk grid layout
        self.setLayout(grid)

        self.setGeometry(100, 100, 400, 500)

        self.setWindowTitle('Pyqt')
        self.show()


def main():
    app = QApplication(sys.argv)
    # Memanggil Class yang sudah dibuat
    tamp = Tampilan()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
