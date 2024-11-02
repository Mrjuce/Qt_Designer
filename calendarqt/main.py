import sys
from PyQt5.QtCore import Qurl 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.media)
        self.get_date()

    def configure(self):
        self.ui.start.clicked.connect(self.media_play)
        self.ui.stop.clicked.connect(self.media_stop)
    
    self.ui.calendar.selectionChanged.connect(self.get_date)

    def get_date(self):
        self.media_stop()
        print(self.ui.calendar.selected().day())

    self.media.setMedia(selfMediaContend(QUrl.fromLocalFile(f"Video\\{day}.avi")))
