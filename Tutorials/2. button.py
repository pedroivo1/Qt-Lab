import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("\033[32mButton clicked, Hello!\033[0m")

app = QApplication(sys.argv)
button = QPushButton('Click Me!')
button.clicked.connect(say_hello)
button.show()

app.exec()
