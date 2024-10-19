# - Підключаємо бібліотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
from PyQt5.QtGui import QKeySequence  # запрограмувати клавішу на вихід

# -------------------------- [Створюємо структуру заміток ідентичну json файлу] ------------------------------------------

# - функція для запису в файл
def writeToFile():
    with open("notes.json", "w") as file:   # Записуємо нашу структуру - сортовано
        json.dump(notes, file, sort_keys=True)
# --------------------------------------------------------------------


'''Інтерфейс програми'''
# ---------------------------
#   Вікно програми
# ---------------------------
app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна
window.setWindowTitle("Smart Notes")
window.resize(main_width,main_height)
window.move(0,0)
window.setStyleSheet("background: rgb(240, 128, 128); font-size:15px")

# ---------------------------
#     Eлементи інтерфейсу
# ---------------------------
text_editor = QTextEdit()                                           # Введення тексту замітки
text_editor.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()                                       # Список заміток
list_widget_1.setStyleSheet("background: rgb(235, 235, 235); font-size:17px")

list_widget_2 = QListWidget()                                       # Список (тегів)
list_widget_2.setStyleSheet("background: rgb(235, 235, 235); font-size:17px")

text_searcher = QLineEdit()                                         # Пошук  по тексту
text_searcher.setPlaceholderText('Введіть текст...')
text_searcher.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")

tag_searcher = QLineEdit()
tag_searcher.setPlaceholderText('Введіть тег...')                   # Пошук  по тегу
tag_searcher.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;") 
# ---------------------------
#      Створення кнопок
# ---------------------------
make_note = QPushButton()
make_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
make_note.setText("Створити замітку")                   

delete_note = QPushButton()
delete_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
delete_note.setText("Видалити замітку")                  

save_note = QPushButton()
save_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
save_note.setText("Зберегти замітку")                  

search_for_text = QPushButton()
search_for_text.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
search_for_text.setText("Шукати замітку за текстом")         

search_for_tag = QPushButton()
search_for_tag.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
search_for_tag.setText("Шукати замітку за тегом")           

add_to_note = QPushButton()
add_to_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
add_to_note.setText("Додати тег до замітки")                   

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
unpin_to_note.setText("Відкріпити тег від замітки")


convert_to_txt = QPushButton()
convert_to_txt.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
convert_to_txt.setText("Конвертувати до txt-формату")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")
action_theme_btn.setText("Змінити тему на чорну")

# ---------------------------
#   Розміщення на макет
# ---------------------------

row1 = QHBoxLayout()              # - гориз додати і видалити замітку
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()              # - гориз дод. до замітки та відкріпити від замітки
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()              # - вер. ввести текст
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
   
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Пошук данних:"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

# Нижні 3 кнопки
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(convert_to_txt)
col2.addWidget(action_theme_btn)

# Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

# Макет на екран
window.setLayout(layout_note) 

# ---------------------------------------------------------[ Функціонал програми ]---------------------------------------------------------------------

# ------------------- [ Замітки ] -------------------

#  отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
def show_notes():
    global key                                        # зберігати назву замітки
    key = list_widget_1.selectedItems()[0].text()     # дізнаємось на яку замітку клікнули
    list_widget_2.clear()                             # очищаємо поле із тегами
    text_editor.setText(notes[key]["text"])           # відобразили текст замітки
    list_widget_2.addItems(notes[key]["tag"])         # відобразили теги замітки


#  додаємо нову замітку 
def add_notes():
    note_name,ok = QInputDialog.getText(window,'Додати замітку',"Назва замітки")    # - Створити вікно QInputDialog з назвою note_name і зчитати текст
    if note_name and ok:
        list_widget_1.addItem(note_name)                                            # - Додає замітку до віджету (списку заміток)
        notes[note_name] = {"text":"","tag":[]}                                     # - Додає до списку notes новий обєкт - але з  пустими поки полями
    writeToFile()                                                                   # - Викликаємо фукнцію для запису в Json фалу нові замітки


#  видалити вибрану замітку 
def delete_notes():
    if list_widget_1.currentItem():          # - якщо вибрана замітка
        if key in notes:                     # - і є така замітка в словнику notes (за ключем)
            notes.pop(key)                   # - pop видаляє з словника
            
            text_editor.clear()              # - очищаємо віджети
            list_widget_2.clear()
            list_widget_1.clear()
            list_widget_1.addItems(notes)    # - оновлюємо віджет списку заміток
            writeToFile()                    # - перезаписуємо файл


#  зберегти замітку 
def save_notes():
    if list_widget_1.currentItem():                       # - якщо вибрана замітка
        key = list_widget_1.currentItem().text()          # - отримати назву вибраної замітки
        notes[key]['text'] = text_editor.toPlainText()   # - записати у словник notes з текстом з віджену
        writeToFile() 


# ---------------------------------------------------------[ Теги ]---------------------------------------------------------------------

# доати тег до замітки 

def add_tag():
    key = list_widget_1.selectedItems()[0].text() # якщо в списку заміток обрана замітка

    if key in  notes:
        tag_name,ok = QInputDialog.getText(window,'Додати тег',"Назва тегу")
        if tag_name and ok:              # чи не пусті поля для вводу
            notes[key]["tag"].append(tag_name)
            writeToFile()

            tag_searcher.clear()
            list_widget_2.addItems(notes[key] ["tag"])

def delete_tag():
    if key in notes:                                                      # Якщо в list_notes обрана замітка
        current_item = list_widget_2.currentItem()                        
        if current_item:
            tag_name = current_item.text()                                # беремо назву тегу
            notes[key]["tag"].remove(tag_name)                            # видаляємо з notes
            list_widget_2.takeItem(list_widget_2.row(current_item))       # видалити цей тег зі списку тегів поточної замітки notes
            writeToFile()                                                 # перезаписуємо в файл


def change_theme():
    if action_theme_btn.text() == "Змінити тему на чорну":
        action_theme_btn.setText("Змінити тему на білу")
        window.setStyleSheet('background-color: rgb(119,49,49);font-size:15px')
        text_editor.setStyleSheet("background: rgb(122,122, 122); font-size:17px;border: 1.9px solid #834F7C;")
        list_widget_1.setStyleSheet("background: rgb(122,122, 122); font-size:17px;border: 1.9px solid #834F7C;")
        list_widget_2.setStyleSheet("background: rgb(122,122, 122); font-size:17px;border: 1.9px solid #834F7C;")
        text_searcher.setStyleSheet("background: rgb(122,122, 122); font-size:17px;border: 1.9px solid #834F7C;")
        tag_searcher.setStyleSheet("background: rgb(122,122, 122); font-size:17px;border: 1.9px solid #834F7C;")
        make_note.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        save_note.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        delete_note.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        search_for_text.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        search_for_tag.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        convert_to_txt.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        add_to_note.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")
        unpin_to_note.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")    
        action_theme_btn.setStyleSheet("background: rgb(41, 116, 192); font-size:17px;border: 1.9px solid #834F7C;")

    elif action_theme_btn.text() == "Змінити тему на білу":
        action_theme_btn.setText("Змінти тему на чорну")
        window.setStyleSheet("background: rgb(240, 128, 128); font-size:15px")
        list_widget_1.setStyleSheet("background: rgb(235, 235, 235); font-size:17px")# поле списку заміток
        list_widget_2.setStyleSheet("background: rgb(235, 235, 235); font-size:17px")# поле списку тегів

        delete_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")#видалити замітку
        make_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# створити замітку
        save_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# зберегти замітку


        search_for_tag.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")# поле пошуку за тегом
        search_for_text.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")#поле пошуку за текстом

        add_to_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# додати тег до замітки
        unpin_to_note.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# вікріпити тег від заміток

        search_for_tag.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# шукати за тегом 
        search_for_text.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# шукати за текстом

        convert_to_txt.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")# конвертувати до txt
        action_theme_btn.setStyleSheet("background: rgb(48, 152, 255); font-size:17px;border: 1.9px solid #834F7C;")#змінити тему на чорну

        tag_searcher.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")  #введіть тег
        text_searcher.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;") #введіть текст

        text_editor.setStyleSheet("background: rgb(235, 235, 235); font-size:17px;border: 1.9px solid #834F7C;")

def export_to_txt():
    if list_widget_1.currentItem():                                                                       # Перевіряємо, чи вибрана замітка у списку
        key = list_widget_1.currentItem().text()                                                          # Витягуємо дані замітки з словника notes за отриманою назвою
        note_data = notes[key]                                                                            # Витягуємо текст з неї
        note_text = note_data['text']                                                                     # Отримуємо текст замітки
        file_dialog = QFileDialog()                                                                       # Викликаємо діалогове вікно для вибору шляху збереження файлу
        file_path, _ = file_dialog.getSaveFileName(window, "Зберегти як .txt", "", "Text Files (*.txt)")

        if file_path:                                                                                      # Якщо шлях збереження був обраний (не пустий)
            with open(file_path, 'w', encoding='utf-8') as txt_file:                                       # Відкриваємо файл для запису в текстовому режимі з кодуванням UTF-8
                txt_file.write("Назва замітки: " )
                txt_file.write(key)
                txt_file.write("\n")
                txt_file.write("Текст замітки: " )
                txt_file.write("\n")
                txt_file.write(note_text)                                                                  # Записуємо текст замітки у файл


def exit_program():
    app.quit()

exit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), window)
exit_shortcut.activated.connect(exit_program)


# пошук по тегу
def search_note_for_tag():

    tag = tag_searcher.text()                                               # Отримуємо текст, введений у поле пошуку тегів
    if search_for_tag.text() == 'Шукати замітку за тегом':                  # Перевіряємо, чи кнопка пошуку по тегу має текст 'Шукати замітку за тегом'
        filtered_notes = {}                                                     # Створюємо словник для збереження відфільтрованих заміток
        for key in notes:                                                       # Перебираємо всі замітки в словнику notes
            if tag in notes[key]['tag']:                                        # Якщо введений тег є в списку тегів замітки
                filtered_notes[key] = notes[key]                                    # Додаємо замітку до відфільтрованих
        search_for_tag.setText('Скинути пошук')                                 # Змінюємо текст кнопки на 'Скинути пошук'

        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes)                              # Додаємо відфільтровані замітки у віджет
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_tag.text() == 'Скинути пошук':                          # Якщо кнопка має текст 'Скинути пошук'
            search_for_tag.setText('Шукати замітку за тегом')               # Змінюємо текст кнопки на 'Шукати замітку за тегом'
            list_widget_1.clear()
            list_widget_1.addItems(notes.keys())                            # Додаємо всі замітки у відже
            list_widget_2.clear()
            text_editor.clear()

def search_for_note():

    text_to_search = text_searcher.text()
    if search_for_text.text() == 'Шукати замітку за текстом':
        filtered_notes = {}
        for key, note_data in notes.items():
            if text_to_search in note_data['text']:
                filtered_notes[key] = note_data

        search_for_text.setText('Скинути пошук')
        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes.keys())
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_text.text() == 'Скинути пошук':
        search_for_text.setText('Шукати замітку за текстом')
        list_widget_1.clear()
        list_widget_1.addItems(notes.keys())
        list_widget_2.clear()
        text_editor.clear()


'''Запуск програми'''
# підключення обробки подій
list_widget_1.itemClicked.connect(show_notes)

#  підключення обробки подій

make_note.clicked.connect(add_notes)
delete_note.clicked.connect(delete_notes)
save_note.clicked.connect(save_notes)
add_to_note.clicked.connect(add_tag)
unpin_to_note.clicked.connect(delete_tag)
search_for_tag.clicked.connect(search_note_for_tag)
search_for_text.clicked.connect(search_for_note)
action_theme_btn.clicked.connect(change_theme)
convert_to_txt.clicked.connect(export_to_txt)

# Зчитати файл - щоб з самого початку вже видно було всі замітки
with open("notes.json", "r") as file:
    notes = json.load(file)
list_widget_1.addItems(notes)

# --------------------------- Закриття програми та показ
window.show()
app.exec_()



# шукати по замітці
