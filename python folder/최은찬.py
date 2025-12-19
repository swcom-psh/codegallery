from ursina import *
import time

app = Ursina()

questions = ['실수 a에 대해 (a-3)² - (a+3)² 의 값은?', '등비수열 {a_n}에서 a₂ = 6, a₄ = 54 일 때, 첫째항 a₁은?', 'sin(45°)의 값은?','sin 150° + cos 60° 의 값은?','log₂(8) + log₃(9) 의 값은?']

def on_button_click6():    
    text = Text('정답', font = '강원교육튼튼.ttf', origin = (-10,-3))
    text = Text('다른 문제를 풀려면 다시 실행', font = '강원교육튼튼.ttf', origin = (0,-4))

def on_button_click7():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,0))

def on_button_click8():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,3))

def on_button_click1():
    text = Text(questions[0], font = '강원교육튼튼.ttf', origin = (0,.5))

    btn6 = Button(text='-12a', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, -.3))
    btn6.on_click = on_button_click6

    btn7 = Button(text='-18a', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, -.3))
    btn7.on_click = on_button_click7

    btn8 = Button(text='-24a', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.0, -.3))
    btn8.on_click = on_button_click8

btn1 = Button(text='Quiz1', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, .3))
btn1.on_click = on_button_click1







def on_button_click11():
    text = Text('정답', font = '강원교육튼튼.ttf', origin = (-10,-3))
    text = Text('다른 문제를 풀려면 다시 실행', font = '강원교육튼튼.ttf', origin = (0,-4))

def on_button_click10():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,0))

def on_button_click12():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,3))


def on_button_click2():
    text = Text(questions[1], font = '강원교육튼튼.ttf', origin = (0,.5))
    
    btn10 = Button(text='2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, -.3))
    btn10.on_click = on_button_click10
    
    btn11 = Button(text='3', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, -.3))
    btn11.on_click = on_button_click11

    btn12 = Button(text='6', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.0, -.3))
    btn12.on_click = on_button_click12

btn2 = Button(text='Quiz2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, .3))
btn2.on_click = on_button_click2










def on_button_click13():
    text = Text('정답', font = '강원교육튼튼.ttf', origin = (-10,-3))
    text = Text('다른 문제를 풀려면 다시 실행', font = '강원교육튼튼.ttf', origin = (0,-4))

def on_button_click14():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,0))

def on_button_click15():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,3))


def on_button_click3():
    text = Text(questions[2], font = '강원교육튼튼.ttf', origin = (0,.5))
    
    btn13 = Button(text='√2 / 2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, -.3))
    btn13.on_click = on_button_click13
    
    btn15 = Button(text='1 / 2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, -.3))
    btn15.on_click = on_button_click14

    btn15 = Button(text='√3 / 2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.0, -.3))
    btn15.on_click = on_button_click15

btn3 = Button(text='Quiz3', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.0, .3))
btn3.on_click = on_button_click3










def on_button_click16():
    text = Text('정답', font = '강원교육튼튼.ttf', origin = (-10,-3))
    text = Text('다른 문제를 풀려면 다시 실행', font = '강원교육튼튼.ttf', origin = (0,-4))

def on_button_click17():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,0))

def on_button_click18():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,3))


def on_button_click4():
    text = Text(questions[3], font = '강원교육튼튼.ttf', origin = (0,.5))
    
    btn16 = Button(text='1', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, -.3))
    btn16.on_click = on_button_click16
    
    btn17 = Button(text='√3/2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, -.3))
    btn17.on_click = on_button_click17

    btn18 = Button(text='3/2', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.0, -.3))
    btn18.on_click = on_button_click18



btn4 = Button(text='Quiz4', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.3, .3))
btn4.on_click = on_button_click4







def on_button_click21():
    text = Text('정답', font = '강원교육튼튼.ttf', origin = (-10,-3))
    text = Text('다른 문제를 풀려면 다시 실행', font = '강원교육튼튼.ttf', origin = (0,-4))

def on_button_click19():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,0))

def on_button_click20():
    text = Text('오답', font = '강원교육튼튼.ttf', origin = (-10,3))


def on_button_click5():
    text = Text(questions[4], font = '강원교육튼튼.ttf', origin = (0,.5))
    
    btn19 = Button(text='4', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.6, -.3))
    btn19.on_click = on_button_click19
    
    btn20 = Button(text='6', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(-.3, -.3))
    btn20.on_click = on_button_click20

    btn21 = Button(text='5', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.0, -.3))
    btn21.on_click = on_button_click21



btn5 = Button(text='Quiz5', font = '강원교육튼튼.ttf', color=color.azure, scale=.1, parent=camera.ui, position=(.6, .3))
btn5.on_click = on_button_click5





app.run()
