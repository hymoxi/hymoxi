from PyQt5.QtCore import Qt, QTimer, QTime
from final_win import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class FinalWin(QWidget):
    def __init__(self, age, t1, t2, t3):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3

class TestWin(QWidget):
    def time_test(self):
        global time
        time = time.addSecs(-1)
        time = QTime(0, 1, 0)
        self.timer = QTime()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
        def timer1Event (self): 
            self.text_timer.setText(time.toString("hh:mm:ss"))
            self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0")
            if time.toString("hh:mm:ss") == "00:00:00":
                self.timer.stop()
    def timer_sits(self):
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer3Event)
    def timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        if int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_test)
        self.btn_test3.clicked.connect(self.timer_test)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))- 200 / 10)