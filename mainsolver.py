from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from pyqtgraph import PlotWidget


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
        self.label_3.setGeometry(QtCore.QRect(160, 60, 150, 21))
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
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 351, 291))
        self.widget.setObjectName("widget")
        self.graphicsView = PlotWidget(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 1, 361, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 351, 281))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
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
        self.historyshow()  # Вывод истории при входе
        self.pushButton.clicked.connect(self.run)  # Ответ на кнопки
        self.pushButton_2.clicked.connect(self.delhistory)

    def delhistory(self):  # Удаляет историю
        f = open('History.txt', mode='w')
        self.label_5.setText('История пуста')
        f.write('')
        f.close()
        return

    def historyshow(self):  # Показывает при входе
        f = open('History.txt', mode='r')
        h_data = f.read()
        f.close()
        h_data = h_data.split('\n')
        text = []
        schet = len(h_data)
        if h_data[0] == '':
            schet = 0
            self.label_5.setText('История пуста')
            return
        if schet > 3:
            schet = 3
        for i in range(schet):
            q = i + 1
            find = h_data[-q]
            find = find.split('@#$')
            firstr = ''.join([str(q), ') Пример: ', str(find[0])])
            secstr = ''.join(['Ответ: ', str(find[1])])
            text.append('\n'.join([firstr, secstr]))
        text = '\n \n'.join(text)
        self.label_5.setText(text)

    def run(self):  # Основа программы(высчитывание ответа)
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
        for i in chl:  # Отбор всех чисел и знаков
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
                if chislo == '':
                    chislo = '1'
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
                if chislo == '':
                    chislo = '1'
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
        self.graph(a, b, c)
        discr = b * b - 4 * a * c
        oneotvet = True
        x1 = 0
        x2 = 0
        if a == 0:  # Вычисление ответов, если нет какого-то параметра
            if b == 0:
                solve.append(''.join([str(solvenum), ') ', 'Переносим всё в левую часть и сокращаем подобное.']))
                solvenum += 1
                solve.append(''.join([str(c), ' = 0']))
                if c == 0:
                    self.label_3.setText("Любой X.")
                    solve = '\n'.join(solve)
                    self.label_4.setText(solve)
                    self.history(equation, "Любой X.")
                else:
                    self.label_3.setText("Нет такого X.")
                    solve = '\n'.join(solve)
                    self.label_4.setText(solve)
                    self.history(equation, "Нет такого X.")
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
                text = " ".join(['x =', x1])
                self.label_3.setText(" ".join(['x =', x1]))
                solve = '\n'.join(solve)
                self.label_4.setText(solve)
                self.history(equation, text)
                return
        solve.append(''.join([str(solvenum), ') ', 'Переносим всё в левую часть и сокращаем подобное.']))
        solvenum += 1
        solve.append('...')
        solve.append(''.join([str(solvenum), ') ', 'Вычисляем дискриминант.']))
        solve.append('Формула дискриминанта: D = b*b - 4*a*c')
        solve.append(''.join(['D = ', str(discr)]))
        solvenum += 1
        solve.append('...')  # Далее вычисление ответов квадратного уравнения
        if discr < 0:
            self.label_3.setText("Нет ответа.")
            solve.append(''.join([str(solvenum), ') ', 'Для такого D нет решения.']))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
            self.history(equation, "Нет ответа.")
            return
        if discr == 0:
            solve.append(''.join([str(solvenum), ') ', 'Вычисляем единственный х.']))
            solve.append(''.join(['x = ', str(-b), '/(2*', str(a), ')']))
            x1 = -b / 2 * a
            x1 = round(x1, 3)
            x1 = str(x1)
            solve.append(''.join(['x = ', x1]))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
        elif discr > 0:
            oneotvet = False
            solve.append(''.join([str(solvenum), ') ', 'Вычисляем х1 и x2.']))
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x1 = round(x1, 3)
            x1 = str(x1)
            solve.append(''.join(['x1 = (', str(-b), '+ sqrt(', str(discr), '))/(2*', str(a), ') = ', x1]))
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            x2 = round(x2, 3)
            x2 = str(x2)
            solve.append(''.join(['x2 = (', str(-b), '- sqrt(', str(discr), '))/(2*', str(a), ') = ', x2]))
            solve = '\n'.join(solve)
            self.label_4.setText(solve)
        if oneotvet:
            text = ' '.join(['x =', x1])
            self.label_3.setText(' '.join(['x =', x1]))
            self.history(equation, text)
        else:
            text = ' '.join(['x1 =', x1, 'x2 =', x2])
            self.label_3.setText(' '.join(['x1 =', x1, 'x2 =', x2]))
            self.history(equation, text)

    def history(self, eq='', ans=''):  # Собирает историю из файла History.txt и выводит
        f = open('History.txt', mode='r')
        h_data = f.read()
        f.close()
        f = open('History.txt', mode='w')
        text = []
        if eq == '' and ans == '':
            self.label_5.setText('История пуста')
            f.write('')
            return
        h_data = h_data.split('\n')
        h_data.append('@#$'.join([eq, ans]))
        schet = len(h_data)
        if schet >= 4:
            schet = 3
        else:
            schet = schet - 1
        for i in range(schet):
            q = i + 1
            find = h_data[-q]
            find = find.split('@#$')
            firstr = ''.join([str(q), ') Пример: ', str(find[0])])
            secstr = ''.join(['Ответ: ', str(find[1])])
            text.append('\n'.join([firstr, secstr]))
        text = '\n \n'.join(text)
        self.label_5.setText(text)
        h_data = '\n'.join(h_data)
        f.write(h_data)
        f.close()
        return

    def graph(self, a=0, b=0, c=0):  # Построение графика
        mass = [i for i in range(-25, 25)]
        self.graphicsView.clear()
        if a == 0 and b == 0:
            self.graphicsView.plot([i for i in mass],
                                   [c for i in mass],
                                   pen='r')
        elif a == 0:
            self.graphicsView.plot([(-c + i) / b for i in mass],
                                   [i for i in mass],
                                   pen='r')
        elif a != 0:
            self.graphicsView.plot([i for i in mass],
                                   [(a * i * i + b * i + c) for i in mass],
                                   pen='r')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

