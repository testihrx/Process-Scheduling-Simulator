from Main import *

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.Proc_List = []
        self.initUI()

    def initUI(self):
        # 첫째줄, 그리드
        grid = QGridLayout()

        cb = QComboBox(self)
        cb.addItem('FCFS')
        cb.addItem('RR')
        cb.addItem('SPN')
        cb.addItem('SRTN')
        cb.addItem('HRRN')
        cb.addItem('YOA')

        ProName = QLineEdit()
        AT = QSpinBox()
        AT.setRange(0, 65535)
        BT = QSpinBox()
        BT.setRange(0, 65535)

        addButton = QPushButton('Add', self)
        addButton.clicked.connect(lambda: self.add(ProName.text(),AT.value(),BT.value()))
        resetButton = QPushButton('Reset', self)
        resetButton.clicked.connect(lambda: self.reset())
        
        #그리드에 위젯넣기
        grid.addWidget(QLabel('Algorithm'), 0, 0)
        grid.addWidget(QLabel('Process Name'), 0, 1)
        grid.addWidget(QLabel('AT'), 0, 2)
        grid.addWidget(QLabel('BT'), 0, 3)
        grid.addWidget(cb,1,0)
        grid.addWidget(ProName, 1, 1)
        grid.addWidget(AT, 1, 2)
        grid.addWidget(BT, 1, 3)
        grid.addWidget(addButton, 1, 4)
        grid.addWidget(resetButton, 1, 5)

        
        
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)

        vbox_main.addLayout(grid)
        vbox_main.addStretch(3)

        self.setWindowTitle('Test')
        self.setGeometry(0, 0, 1024, 768)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add(self, name, at, bt):
        self.Proc_List.append([name,at,bt])

    def reset(self):
        self.Proc_List.clear()

    def passer(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
