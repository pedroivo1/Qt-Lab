from PySide6 import QtWidgets, QtCore


class DigitalClock(QtWidgets.QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.setDigitCount(8)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.show_time()

        self.setWindowTitle('Digital Clock')
        self.resize(250, 60)


    @QtCore.Slot()
    def show_time(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')

        if (time.second() % 2) == 0:
            text = text.replace(':', ' ')

        self.display(text)
