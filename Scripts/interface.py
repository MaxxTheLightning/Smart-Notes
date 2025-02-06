from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
    QTextEdit,
    QInputDialog,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout
)

class Interface():
    def __init__(self, name):
        self.app = QApplication([])
        self.win = QWidget()
        self.win.setWindowTitle(name)
        self.win.resize(900, 600)
        self.text_field = QTextEdit()
        self.note_list_label = QLabel('Notes list')
        self.note_list_label.setStyleSheet('''
            color: aqua;
        ''')
        self.tags_list_label = QLabel('Taglist')
        self.tags_list_label.setStyleSheet('''
            color: aqua;
        ''')
        self.create_note_button = QPushButton('Add note')
        self.create_note_button.setStyleSheet('''
            :hover{
                background-color: green;
            }    
        ''')
        self.delete_note_button = QPushButton('Delete note')
        self.delete_note_button.setStyleSheet('''
            :hover {
                background-color: #fe3434;
            }
        ''')
        self.save_note_button = QPushButton('Save note')
        self.save_note_button.setStyleSheet('''
        :hover{
            background-color: #4dbbff;
            color: black;
        }
        ''')
        self.add_tag_button = QPushButton('Add tag to note')
        self.add_tag_button.setStyleSheet('''
        :hover{
            background-color: green;
        }    
        ''')
        self.remove_tag_button = QPushButton('Unpin tag from note')
        self.remove_tag_button.setStyleSheet('''
        :hover{
            background-color: #fe3434;
        }    
        ''')
        self.find_notes_button = QPushButton('Search by tag')
        self.find_notes_button.setStyleSheet('''
        :hover{
            background-color: #4dbbff;
            color: black;
        }
        ''')
        self.note_list = QListWidget()
        self.note_list.setStyleSheet('''
            border: 1px solid aqua;
            border-radius: 8px;
        ''')
        self.tag_list = QListWidget()
        self.tag_list.setStyleSheet('''
            border: 1px solid aqua;
            border-radius: 8px;
        ''')
        self.tag_input = QLineEdit('')
        self.text_edit = QTextEdit('')
        self.text_edit.setStyleSheet('''
            border: 1px solid aqua;
            border-radius: 8px;
            font-size: 18px;
            font-family: Bahnschrift;
        ''')
        self.tag_input.setPlaceholderText('Enter tag...')
        main_layout = QHBoxLayout()
        col_1 = QVBoxLayout()
        col_1.addWidget(self.text_edit)
        col_2 = QVBoxLayout()
        col_2.addWidget(self.note_list_label)
        col_2.addWidget(self.note_list)
        row_1 = QHBoxLayout()
        row_1.addWidget(self.create_note_button)
        row_1.addWidget(self.delete_note_button)
        col_2.addLayout(row_1)
        row_2 = QHBoxLayout()
        row_2.addWidget(self.save_note_button)
        col_2.addLayout(row_2)

        col_2.addWidget(self.tags_list_label)
        col_2.addWidget(self.tag_list)
        col_2.addWidget(self.tag_input)
        row_3 = QHBoxLayout()
        row_3.addWidget(self.add_tag_button)
        row_3.addWidget(self.remove_tag_button)
        row_4 = QHBoxLayout()
        row_4.addWidget(self.find_notes_button)
        col_2.addLayout(row_3)
        col_2.addLayout(row_4)

        main_layout.addLayout(col_1, stretch = 2)
        main_layout.addLayout(col_2, stretch = 1)
        self.win.setStyleSheet("background-color: #212121;color: white;")
        self.win.setLayout(main_layout)
    def run(self):
        self.win.show()
        self.app.exec_()
    
    def update_note_fields(self, note_text, note_names, note_tags):
        self.note_list.clear()
        self.tag_list.clear()
        self.text_edit.setText(note_text)
        self.note_list.addItems(note_names)
        self.tag_list.addItems(note_tags)

    def accept_select_note(self, func):
        def update():
            name = self.note_list.selectedItems()[0].text()
            func(name)
        self.note_list.itemClicked.connect(update)

    def accept_create_note(self, func):
        def update():
            name, ok = QInputDialog.getText(self.win, "Add note", "Note name:")
            if ok and name != "":
                func(name)
        self.create_note_button.clicked.connect(update)

    def accept_save_note(self, func):
        def update():
            func(self.text_edit.toPlainText())
        self.save_note_button.clicked.connect(update)

    def accept_delete_note(self, func):
        self.delete_note_button.clicked.connect(func)

    def accept_pin_tag(self, func):
        def update():
            func(self.tag_input.text())
            self.tag_input.setText('')
        self.add_tag_button.clicked.connect(update)

    def accept_delete_tag(self, func):
        def update():
            tag = self.tag_list.selectedItems()[0].text()
            func(tag)
        self.remove_tag_button.clicked.connect(update)

    def accept_find_note(self, func):
        def update():
            tag = self.tag_input.text()
            self.tag_input.setText('')
            func(tag)
        self.find_notes_button.clicked.connect(update)