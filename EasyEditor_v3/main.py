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

workdir = ""  # Змінна для збереження шляху до вибраної директорії

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()  # Виправлено на правильний метод

def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    chooseWorkdir()  # Викликаємо функцію вибору директорії
    extensions = [".jpg", ".png", ".jpeg", ".bmp", ".gif"]  # Виправлено ".git" на ".gif"
    filenames = filter(os.listdir(workdir), extensions)
    list_file.clear()
    for file in filenames:
        list_file.addItem(file)

class ImageProcessor():
    def __init__(self):  # Виправлено на правильне ім'я конструктора
        self.image = None
        self.filename = None
        self.dir = None
        self.savedir = "Modified/"

    def loadImage(self, filename, dir):
        self.filename = filename
        self.dir = dir
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self):
        temp_image_path = os.path.join(workdir, self.savedir, self.filename)
        pixmapimage = QPixmap(temp_image_path)
        w = lbl_picture.width()
        h = lbl_picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbl_picture.setPixmap(pixmapimage)

    def saveImage(self):
        path = os.path.join(workdir, self.savedir)
        if not os.path.exists(path):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        self.showImage()

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        self.showImage()

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        self.showImage()

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        self.showImage()

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        self.showImage()

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        self.showImage()


workimage = ImageProcessor()

def showSelectImage():
    if list_file.selectedIndexes():
        filename = list_file.selectedItems()[0].text()
        workimage.loadImage(filename, workdir)  # Викликаємо метод на об'єкті workimage
        workimage.saveImage()
        workimage.showImage()

btn_file.clicked.connect(showFilenamesList)
list_file.itemClicked.connect(showSelectImage)

btn_black_white.clicked.connect(workimage.do_bw)
btn_blur.clicked.connect(workimage.do_blur)
btn_mirror.clicked.connect(workimage.do_mirror)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharp)

app.exec_()
