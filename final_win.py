from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import*

class FinalWin(QWidget):
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results)
        self.index_text = QLabel(txt_index + str(self.index))
        def ifs(self):
            print(txt_index, self.index)
            print(txt_workheart)
            if self.age >= 15:
                if self.index >= 15:
                    print(txt_res1)
                elif self.index >= 11 and self.index <= 14.9:
                    print(txt_res2)
                elif self.index >= 6 and self.index <= 10.9:
                    print(txt_res3)
                elif self.index >= 0.5 and self.index <= 5.9:
                    print(txt_res4)
                elif self.index <= 0.4:
                    print(txt_res5)
            elif self.age >= 13 and self.age <= 14:
                if self.index >= 16.5:
                    print(txt_res1)
                elif self.index >= 12.5 and self.index <= 16.4:
                    print(txt_res2)
                elif self.index >= 7.5 and self.index <= 12.4:
                    print(txt_res3)
                elif self.index >= 2 and self.index <= 7.4:
                    print(txt_res4)
                elif self.index <= 1.9:
                    print(txt_res5)
            elif self.age >= 11 and self.age <= 12:
                if self.index >= 18:
                    print(txt_res1)
                elif self.index >= 14 and self.index <= 17.9:
                    print(txt_res2)
                elif self.index >= 9 and self.index <= 13.9:
                    print(txt_res3)
                elif self.index >= 3.5 and self.index <= 8.9:
                    print(txt_res4)
                elif self.index <= 3.4:
                    print(txt_res5)
            elif self.age >= 9 and self.age <= 10:
                if self.index >= 19.5:
                    print(txt_res1)
                elif self.index >= 15.5 and self.index <= 19.4:
                    print(txt_res2)
                elif self.index >= 10.5 and self.index <= 15.4:
                    print(txt_res3)
                elif self.index >= 5 and self.index <= 10.4:
                    print(txt_res4)
                elif self.index <= 4.9:
                    print(txt_res5)
            elif self.age >=7 and self.age <= 8:
                if self.index >= 21:
                    print(txt_res1)
                elif self.index >= 17 and self.index <= 20.9:
                    print(txt_res2)
                elif self.index >= 12 and self.index <= 16.9:
                    print(txt_res3)
                elif self.index >= 6.5 and self.index <= 11.9:
                    print(txt_res4)
                elif self.index <= 6.4:
                    print(txt_res5)