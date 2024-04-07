from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,QPushButton,
    QGroupBox, QRadioButton, QHBoxLayout,QVBoxLayout,QButtonGroup
)
from random import shuffle, randint

class Question():
    def __init__(self, queston, right_answer, wrong1, wrong2, wrong3):
        self.queston = queston
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

queston_list = []
queston_list.append(Question("Вопрос 1", '1', '2', '3','4'))
queston_list.append(Question("Вопрос 2", '1', '2', '3','4'))
queston_list.append(Question("Вопрос 3", '1', '2', '3','4'))
queston_list.append(Question("Вопрос 4", '1', '2', '3','4'))
queston_list.append(Question("Вопрос 5", '1', '2', '3','4'))

app = QApplication([])
window = QWidget()

window.setWindowTitle('Memory card')
window.resize(400, 400)

queston = QLabel('Вопрос')
btn_ok = QPushButton("Ответить")

RadioGroupBox = QGroupBox('Варианты ответов :')
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Ответ будет тут !')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(queston, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)

''' Функции'''
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий Вопрос')
btn_ok.clicked.connect(show_result)

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


def start_test():
    if 'Ответить' == btn_ok.text():
        show_result()
    else:
        show_question()

answer = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    queston.setText(q.queston)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()


def cheack_answer():
    if answer[0].isChecked():
        show_correct('правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked()or answer[2].isChecked()or answer[3].isChecked():
            show_correct('неправильно!')
            print('Рейтинг:', (window.score/window.total*100), '%')


def next_question():
    cur_question = randint(0, len(queston_list) - 1)
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:', window.score)
    q = queston_list[cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        cheack_answer
    else:
        next_question()


btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()





btn_ok.clicked.connect(cheack_answer)


window.show()
app.exec_()
