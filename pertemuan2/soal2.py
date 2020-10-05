import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   x = 0
   for i in range(5):
       button = QPushButton(str(i+1),window)
       button.setStyleSheet("color: red; font-size: 13pt; font-weight: bold; background-color: grey")
       button.resize(50,50)
       button.move(x,10)
       x += 50
   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(100,100,500,500)
   window.setWindowTitle("PyQT Pertama")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()
