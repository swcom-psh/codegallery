from ursina import *
import random as ran
import time

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

# 캐릭터, 코인 배치
background = Entity(model='quad', scale=8, position=(0, 0, 0))
character  = Entity(model='sphere', scale=0.75, position=(0, 0, -0.001),color="#000000", collider='box')

coins = []
for _ in range(10):
    coin = Entity(model='sphere',scale=0.5,position=(ran.uniform(-3.5, 3.5), ran.uniform(-3.5, 3.5), -0.1),color="#D4C00D",collider='box')
    coins.append(coin)



#업데이트 함수 
def update():
    global ti

    # 캐릭터 이동
    if held_keys['w']:
        character.y += 3 * time.dt
    if held_keys['s']:
        character.y -= 3 * time.dt
    if held_keys['a']:
        character.x -= 3 * time.dt
    if held_keys['d']:
        character.x += 3 * time.dt

    # 코인 획득
    for c in coins:
        if c.enabled and character.intersects(c).hit:
            c.enabled = False

    # 시간 업데이트
    ti = int(time.time() - start)
    timer_text.text = f'time: {ti} sec'

# 시간 표시
ti = 0
start = time.time()
timer_text = Text(text='time: 0 sec', position=(-0.85, 0.45))









app.run()