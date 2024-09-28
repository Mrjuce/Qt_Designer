from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

#------------------------
#вікно програми 
#------------------------

app = QApplication([])

window = QWidget() 
window.resize(800, 600)
window.setWindowTitle("Smart notes")
window.move(0,0)
window.setStyleSheet("background: rgb(240, 128, 128); font-size:15px")

#------------------------
#    Елементи інтерфейсу
#------------------------

text_editor = QTextEdit()     #поле для тексту замітки 
text_editor.setPlaceholderText("Введіть текст замітки...")

list_widget_1 = QListWidget() # список замітоу
list_widget_2 = QListWidget() # сп тегів

text_searcher = QLineEdit()                         # пошук по тексту
text_searcher.setPlaceholderText("Введіть текс...") 

tag_searcher =  QLineEdit()                         #пошук по тегу 
tag_searcher.setPlaceholderText("Введіть тег ...") 

#------------------------
#           Кнопки
#------------------------

make_note = QPushButton()
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setText("Зберегти замітку")

search_for_text = QPushButton()
search_for_text.setText("Шукати за текстом")

search_for_tag = QPushButton()
search_for_tag.setText("Шукати за тегом")

add_to_note = QPushButton()
add_to_note.setText("Додати тег до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкріпити  тег від замітки")

convert_to_text = QPushButton()
convert_to_text.setText("Конвертувати до txt")

actoin_theme_btn = QPushButton()
actoin_theme_btn.setText("Змінити тему ")


#------------------------
#           Макет
#------------------------

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QVBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)


col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Пошук данних:"))
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addLayout(row2)
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(convert_to_text)
col2.addWidget(actoin_theme_btn)

#Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

#Макет на екран
window.setLayout(layout_note)

#------------------------
#           
#------------------------
list_widget_1.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
list_widget_1.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
delete_note.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
make_note.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
save_note.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
list_widget_2.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
search_for_tag.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
search_for_text.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
add_to_note.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
unpin_to_note.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
search_for_tag.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
search_for_text.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
convert_to_text.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")
actoin_theme_btn.setStyleSheet("background: rgb(0 , 255, 255); font-size:15px")



window.show()
app.exec_()