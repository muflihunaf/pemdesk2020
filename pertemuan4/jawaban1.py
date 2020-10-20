import sys
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QComboBox,QHBoxLayout,QGroupBox, QRadioButton,QVBoxLayout, QGridLayout, QTabWidget,QSizePolicy,QTableWidget,QTextEdit,QSpinBox,QSlider,QDial,QLineEdit,QDateTimeEdit,QScrollBar,QProgressBar
#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()



   GLayout = QGridLayout()
   GLayout.addLayout(topLayout(window),0,0,1,2)
   GLayout.addWidget(group1(window),1,0)
   GLayout.addWidget(group2(window),1,1)
   GLayout.addWidget(group3(window),2,0)
   GLayout.addWidget(group4(window), 2, 1)
   GLayout.addWidget(group5(window), 3, 0,1,2)
   GLayout.setRowStretch(1, 1)
   GLayout.setRowStretch(2, 1)
   GLayout.setColumnStretch(0, 1)
   GLayout.setColumnStretch(1, 1)

   window.setLayout(GLayout)
   
   window.setGeometry(100,100,500,500)
   window.setWindowTitle("PyQT Pertama")
   window.show()
   sys.exit(app.exec_())
def topLayout(window):
    comboBox = QComboBox(window)
    comboBox.addItem("Halo")
    
    label = QLabel("Style",window)
    label.setBuddy(comboBox)

    checkbox = QCheckBox("Use Style Standart Palette",window)
    checkbox.setChecked(True)

    checkbox2 = QCheckBox("Disable widgets",window)

    layout1 = QHBoxLayout()
    layout1.addWidget(label)
    layout1.addWidget(comboBox)
    layout1.addStretch(1)
    layout1.addWidget(checkbox)
    layout1.addWidget(checkbox2)
    return layout1
def group1(window):
    groupbox = QGroupBox("Group 1", window)
    radioButton1 = QRadioButton("Radio button 1")
    radioButton2 = QRadioButton("Radio button 2")
    radioButton3 = QRadioButton("Radio button 3")
    radioButton1.setChecked(True)

    checkBox = QCheckBox("Tri-state check box")
    checkBox.setTristate(True)
    checkBox.setCheckState(Qt.PartiallyChecked)
    layout = QVBoxLayout()
    layout.addWidget(radioButton1)
    layout.addWidget(radioButton2)
    layout.addWidget(radioButton3)
    layout.addWidget(checkBox)
    layout.addStretch(1)
    groupbox.setLayout(layout)
    return groupbox
def group2(window):
    groupbox = QGroupBox("Group 2", window)

    button1 = QPushButton("Default Push Button",window)
    button1.setDefault(True)

    button2 = QPushButton("Toggle Push Button")
    button2.setCheckable(True)
    button2.setChecked(True)

    button3 = QPushButton("Flat Push Button")
    button3.setFlat(True)
    layout = QVBoxLayout()
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addStretch(1)
    groupbox.setLayout(layout)
    return groupbox
def group3(window):
    tab = QTabWidget(window)
    tab.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Ignored)

    table = QTableWidget(5,5,window)

    tab1 = QWidget()
    hbox = QHBoxLayout()
    hbox.setContentsMargins(5, 5, 5, 5)
    hbox.addWidget(table)
    tab1.setLayout(hbox)

    tab2 = QWidget()
    textEdit = QTextEdit(window)
    hbox2 = QHBoxLayout()
    hbox2.setContentsMargins(5, 5, 5, 5)
    hbox2.addWidget(textEdit)
    tab2.setLayout(hbox2)

    tab.addTab(tab1,"Table")
    tab.addTab(tab2,"Text Edit")
    return tab
def group4(window):
    groupbox = QGroupBox("Group 3")
    groupbox.setCheckable(True)
    groupbox.setChecked(True)

    input = QLineEdit("firmanslur",window)
    input.setEchoMode(QLineEdit.Password)

    spin = QSpinBox(window)
    spin.setValue(50)

    tanggal = QDateTimeEdit(window)
    tanggal.setDateTime(QDateTime.currentDateTime())

    slider = QSlider(Qt.Horizontal,window)
    slider.setValue(50)
    
    scrollBar = QScrollBar(Qt.Horizontal, window)
    scrollBar.setValue(60)

    dial = QDial(window)
    dial.setValue(30)
    dial.setNotchesVisible(True)

    layout = QGridLayout()
    layout.addWidget(input, 0, 0, 1, 2)
    layout.addWidget(spin, 1, 0, 1, 2)
    layout.addWidget(tanggal, 2, 0, 1, 2)
    layout.addWidget(slider, 3, 0)
    layout.addWidget(scrollBar, 4, 0)
    layout.addWidget(dial, 3, 1, 2, 1)
    layout.setRowStretch(5, 1)
    groupbox.setLayout(layout)
    return groupbox
def group5(window):
    progressbar = QProgressBar(window)
    progressbar.setRange(0,100)
    progressbar.setValue(22)
    return progressbar



if __name__ == '__main__':
   window_go()
