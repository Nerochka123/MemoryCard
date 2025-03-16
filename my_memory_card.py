#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QButtonGroup, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
#приложение
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 300)

main_win.score=0
main_win.total=0

#создание виджетов
lbl_question = QLabel('Вопрос')
RadioGroup = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ1')
rbtn_2 = QRadioButton('Ответ2')
rbtn_3 = QRadioButton('Ответ3')
rbtn_4 = QRadioButton('Ответ4')
btn_ok = QPushButton('Ответить')

AnswerGroup = QGroupBox('Результат')
lbl_result = QLabel('Верно/Неверно')
lbl_correct = QLabel('Правильный ответ')

lbl_stat = QLabel('Статистика')
lbl_question = QLabel('Вопрос')
rbtn_1 = QRadioButton('ответ1')
rbtn_2 = QRadioButton('ответ2')
rbtn_3 = QRadioButton('ответ3')
rbtn_4 = QRadioButton('ответ3')

#привязка элементов к лейаутам
BattonGroup = QButtonGroup()
BattonGroup.addButton(rbtn_1)
BattonGroup.addButton(rbtn_2)
BattonGroup.addButton(rbtn_3)
BattonGroup.addButton(rbtn_4)

row1 = QHBoxLayout()
row1.addWidget(rbtn_1)
row1.addWidget(rbtn_2)
row2 = QHBoxLayout()
row1.addWidget(rbtn_3)
row1.addWidget(rbtn_4)

answ = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)

RadioGroup.setLayout(col)

col1 = QVBoxLayout()
col1.addWidget(lbl_result, alignment=Qt.AlignLeft)
col1.addWidget(lbl_correct, alignment=Qt.AlignCenter)


AnswerGroup.setLayout(col1)
AnswerGroup.hide()

main_layout = QVBoxLayout()
main_layout.setSpacing(15)
main_layout.addWidget(lbl_question, alignment=Qt.AlignCenter, stretch = 1)
main_layout.addWidget(RadioGroup, stretch = 2)
main_layout.addWidget(AnswerGroup, stretch = 2)
main_layout.addWidget(btn_ok)
main_layout.addWidget(lbl_stat, stretch=2)

main_win.setLayout(main_layout)

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.r_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
Q = Question('Когда началсь вторая ВОВ?', '1941', '1888', '1000', '4703')
question_list.append(Q)
Q = Question('Кто полетел в космос?', 'Юрий Гагарин', 'Николай Носов', 'Александр Пушкин', 'Король Артур')
question_list.append(Q)
Q = Question('Из чего состоит физическое тело?', 'из атомов и молекул', 'из воды', 'не из чего', 'из воздуха')
question_list.append(Q)


def show_result():
    RadioGroup.hide()
    AnswerGroup.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    BattonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    BattonGroup.setExclusive(True)
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    RadioGroup.show()
    AnswerGroup.hide()
    btn_ok.setText('Ответить')



def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_answer)
    answ[0].setText(q.wrong1)
    answ[1].setText(q.wrong2)
    answ[2].setText(q.wrong3)
    answ[3].setText(q.wrong3)
    main_win.total+=1

def checkAnswer():
    if btn_ok.text() == 'Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Совершено верно')
            main_win.score+=1
        else:
            lbl_result.setText('Неврно!')
        show_result()
        lbl_stat.setText('статистика:\nВсего вопросов:'+str(main_win.total)+'\nПравильных:'+str(main_win.score)+'\nРейтинг:'+str(main_win.score/main_win.total*100))
    else:
        show_question()
    
num = randint(0, len(question_list)-1)
ask(question_list[num])
btn_ok.clicked.connect(checkAnswer)


#запуск приложения
main_win.show()
app.exec_()