import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import refleksi, GuiHitung
app = QApplication(sys.argv)
mWin = QMainWindow()
def window1():
    win = QWidget()   #layout di tempelkan ke QWidget
    bar = mWin.menuBar()
    file = bar.addMenu("Menu")
    suhu = QAction("Rumus Suhu")
    ruang = QAction("Rumus Kecepatan")
    file.addAction(suhu)
    file.addAction(ruang)
    
    suhu.triggered.connect(hitungSuhu)
    ruang.triggered.connect(hitungKecepatan)
    
    judul = QLabel("Belajar Membuat Menu Bar")
    vbox = QVBoxLayout(win)
    vbox.addWidget(judul)
    vbox.setAlignment(Qt.AlignCenter)
    
    #win.setLayout()
    mWin.setCentralWidget(win)
    mWin.setGeometry(200,200,300,300)
    mWin.setWindowTitle("Membuat MenuBar")
    mWin.show() 
    sys.exit(app.exec_())   
def hitungSuhu():
    refleksi.window_go(app)
def hitungKecepatan():
    GuiHitung.window_go(app)

if __name__ == '__main__':
    window1()