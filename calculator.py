import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
)
from PyQt5.QtCore import Qt

# Вказуємо шлях до плагінів Qt (якщо виникають проблеми з платформою)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = (
    r"C:\Users\Влад\AppData\Local\Programs\Python\Python39\Lib\site-packages\PyQt5\Qt\plugins\platforms"
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")  # Заголовок вікна
        self.setGeometry(100, 100, 300, 400)  # Позиція та розміри вікна

        self.result_display = QLineEdit(self)  # Поле для виведення результату
        self.result_display.setReadOnly(False)  # Тепер можна редагувати текст
        self.result_display.setAlignment(Qt.AlignRight)  # Вирівнювання по правому краю

        self.create_buttons()  # Створення кнопок калькулятора

        # Лейаут для розміщення елементів
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_display)
        main_layout.addLayout(self.grid_layout)
        self.setLayout(main_layout)

    def create_buttons(self):
        """Метод для створення кнопок калькулятора"""
        self.grid_layout = QGridLayout()

        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            (".", 3, 1),
            ("=", 3, 2),
            ("+", 3, 3),
            ("C", 4, 0),  # Кнопка для очищення
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(
                self.on_button_click
            )  # Підключення до методу натискання
            self.grid_layout.addWidget(button, row, col)

    def on_button_click(self):
        """Метод обробки натискання кнопок"""
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            try:
                expression = self.result_display.text()
                result = eval(expression)  # Обчислення виразу
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText(
                    "Error"
                )  # Якщо виникає помилка в обчисленні
        elif button_text == "C":
            current_text = self.result_display.text()
            self.result_display.setText(current_text[:-1])  # Стираємо останній символ
        else:
            current_text = self.result_display.text()
            self.result_display.setText(current_text + button_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
