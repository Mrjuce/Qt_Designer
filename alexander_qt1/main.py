
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generate.clicked.connect(self.generate)

    def generate(self):
        #виберається тільки букви або тільки цифри
    
        signs = ""
        if self.ui.only_liters.isChecked():
            signs += "qwertyuiopasdfghjklzxcvbnm"
        if self.ui.only_num.isChecked():
            signs += "0123456789"


        result = ""
        numbers = random.randint(5,10)
        for _ in range(numbers):
            result += random.choice(signs)

        self.ui.results.setText(result)



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()