import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   y = 10
   for i in range(10):
       var = QLabel(window)
       var.setText("Ini Kalimat Ke " + str(i+1))
       var.setStyleSheet("color: white")
       var.move(160,y)
       y += 30

   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(100,100,500,500)
   window.setWindowTitle("PyQT Pertama")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()
