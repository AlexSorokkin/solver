from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 362)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 361, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 90, 271, 71))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 331, 291))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 351, 291))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(234, 0, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Решить"))
        self.label.setText(_translate("MainWindow", "Инструкция к вводу. \n"
" 1) Ввод цифр и знаков производить через пробел. \n"
" 2) Неизвестную принять за x (англ). \n"
" 3) Квадрат неизвестной: x^(2) \n"
" Пример ввода: 4x^(2) + 4x - 3 = 1"))
        self.label_2.setText(_translate("MainWindow", "Ответ:"))
        self.label_3.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Калькулятор"))
        self.label_4.setText(_translate("MainWindow", "Нет уравнения - нет решения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Решение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "График"))
        self.label_5.setText(_translate("MainWindow", "История пуста"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить историю"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "История"))



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        equation = self.lineEdit.text()
        kvadrx = []
        onex = []
        solvenum = 1
        solve = []
        svob_chl = []
        chislo = 0
        a = 0
        b = 0
        c = 0
        chl = equation.split(' ')
        polozhit = True
        after_equal = False
        for i in chl:
            if i == '+':
                if after_equal:
                    polozhit = False
                else:
                    polozhit = True
            elif i == '-':
                if after_equal:
                    polozhit = True
                else:
                    polozhit = False
            elif i == '=':
                after_equal = True
                polozhit = False
            elif 'x^(2)' in i:
                chislo = i[:-5]
                try:
                    chislo = int(chislo)
                except ValueError:
                    self.label_3.setText("Неправильный ввод.")
                    return
                if polozhit:
                    kvadrx.append(chislo)
                else:
                    chislo = -chislo
                    kvadrx.append(chislo)
            elif 'x' in i:
                chislo = i[:-1]
                try:
                    chislo = int(chislo)
                except ValueError:
                    self.label_3.setText("Неправильный ввод.")
                    return
                if polozhit:
                    onex.append(chislo)
                else:
                    chislo = -chislo
                    onex.append(chislo)
            else:
                try:
                    chislo = int(i)
                except ValueError:
                    self.label_3.setText('Неправильный ввод.')
                    return
                if not polozhit:
                    chislo = -chislo
                svob_chl.append(chislo)
        for i in kvadrx:
            a += i
        for i in onex:
            b += i
        for i in svob_chl:
            c += i
        discr = b*b - 4*a*c
        oneotvet = True
        x1 = 0
        x2 = 0
        if a == 0:
            if b == 0:
                solve.append(''.join([str(solvenum), ') ', 'Переносим всё в левую часть и сокращаем подобное.']))
                solvenum += 1
                solve.append(''.join([str(c), ' = 0']))
                self.label_3.setText("Любой X.")
                solve = '\n'.join(solve)
                self.label_4.setText(solve)
                return
            else:
                solve.append(''.join([str(solvenum), ') ', 'Переносим всё в левую часть и сокращаем подобное.']))
                solvenum += 1
                solve.append(''.join([str(b), str(c), ' = 0']))
                x1 = -c / b
                solve.append('...')
                solve.append(''.join([str(solvenum), ') ', 'Вычисляем x.']))
                solve.append(''.join(['x = ', str(-c), '/', str(b)]))
                x1 = str(x1)
                self.label_3.setText(" ".join(['x =', x1]))
                solve = '\n'.join(solve)
                self.label_4.setText(solve)
                return
        solve.append(''.join([str(solvenum), ') ', 'Переносим всё в левую часть и сокращаем подобное.']))
        solvenum += 1
        solve.append('...')
        solve.append(''.join([str(solvenum),') ', 'Вычисляем дискриминант.']))
        solve.append('Формула дискриминанта: D = b*b - 4*a*c')
        solve.append(''.join(['D = ', str(discr)]))
        solvenum += 1
        solve.append('...')
        if discr < 0:
            self.label_3.setText("Нет ответа.")
            solve.append(''.join([str(solvenum), ') ', 'Для такого D нет решения.']))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
            return
        if discr == 0:
            solve.append(''.join([str(solvenum), ') ', 'Вычисляем единственный х.']))
            solve.append(''.join(['x = ', str(-b), '/(2*', str(a), ')']))
            x1 = -b / 2*a
            x1 = round(x1, 3)
            x1 = str(x1)
            solve.append(''.join(['x = ', x1]))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
        elif discr > 0:
            oneotvet = False
            solve.append(''.join([str(solvenum), ') ', 'Вычисляем х1 и x2.']))
            x1 = (-b + math.sqrt(discr)) / (2*a)
            x1 = round(x1, 3)
            x1 = str(x1)
            solve.append(''.join(['x1 = (', str(-b), '+ sqrt(', str(discr), '))/(2*', str(a), ') = ', x1]))
            x2 = (-b - math.sqrt(discr)) / (2*a)
            x2 = round(x2, 3)
            x2 = str(x2)
            solve.append(''.join(['x2 = (', str(-b), '- sqrt(', str(discr), '))/(2*', str(a), ') = ', x2]))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
        if oneotvet:
            self.label_3.setText(' '.join(['x =', x1]))
        else:
            self.label_3.setText(' '.join(['x1 =', x1, 'x2 =', x2]))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
