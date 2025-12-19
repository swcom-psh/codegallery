from ursina import *
import random


app = Ursina()

window.color= color.hex("#080741")# 배경화면








score = 0 # 점수판 만들기
score_text = Text(text=f"Score: {score}", position=(-0.85, 0.45), scale=1.5)


ck =0
def round(): # 목표물 랜덤 위치에 생성 + 목표물 설정
    x = random.uniform(-5, 5)
    y = random.uniform(-3, 3)

    t1 = Entity(
            model='sphere',
            color=color.red,
            scale=0.5,
            position=(x, y, 0),
            collider='sphere'
        )
    return t1# t1을 


def input(key):
    global score
    global ck
    if key == 'left mouse down':  # 마우스 왼쪽 버튼 눌렀을 때
            if mouse.hovered_entity == tls and ck == 0: # 만약 마우스가 목표물 위에 있고 ck가 0이면 목표물을 파괴시키고 점수를 1을 점수판에 보이게 올리고 ck는 1이 된다.
                destroy(tls)
                score +=1
                score_text.text=f"Score:{score}"
                ck =1
                

tls= round()# 첫 목표물 생성

def update(): #목표물 재 생성
     global ck
     global start_time
     global tls
     if ck == 1:
         tls = round()
         ck= 0

     


app.run()