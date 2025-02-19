import sys
from models import DigitalClock
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = DigitalClock.DigitalClock()
    clock.show()
    sys.exit(app.exec())
