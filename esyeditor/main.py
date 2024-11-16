#Підключаємо бібліотеки 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap 
import os 
from PIL import Image, ImageFilter 
 
 
app = QApplication([]) 
 
win = QWidget() 
win.resize(700,500) 
win.setWindowTitle('Easy Editor') 
win.show() 
 
btn_file = QPushButton('Folder') 
btn_left = QPushButton('Left') 
btn_right = QPushButton('Right') 
btn_mirror = QPushButton('Mirror') 
btn_sharp = QPushButton('Sharp') 
btn_blur = QPushButton('Blur') 
btn_black_white = QPushButton('B/W') 
 
lbl_picture = QLabel('Picture') 
 
list_file = QListWidget() 
 
v1 = QVBoxLayout() 
v2 = QVBoxLayout() 
h1 = QHBoxLayout() 
h2 = QHBoxLayout() 
main_layout = QHBoxLayout() 
 
v1.addWidget(btn_file) 
v1.addWidget(list_file) 
 
h1.addWidget(btn_left) 
h1.addWidget(btn_right) 
h1.addWidget(btn_mirror) 
h1.addWidget(btn_sharp) 
h1.addWidget(btn_black_white) 
 
h2.addWidget(btn_blur) 
 
v2.addWidget(lbl_picture) 
v2.addLayout(h1) 
v2.addLayout(h2) 
 
main_layout.addLayout(v1) 
main_layout.addLayout(v2) 
win.setLayout(main_layout) 
 
def chooseWorkgir():
    global workidr
    workdir  = QFileDialog.getExistingDirectory()

def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
 
 
 
app.exec_()