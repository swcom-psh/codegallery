#컴퓨터의 메인보드 구현
#키보드 구현-누르면 메모리에 저장되는 기능 추가(메모리도 화면으로 보여주기)-제어장치를
#추가하고 제어신호를 통해 메모리에 저장된 값을 읽는 모습 구현-명령어가 cpu-->레지스터로
#저장되는 모습 구현-제어장치가 명령어를 해석해서 메모리 읽기 제어 신호를 보내는것을 구현
#이지민
from ursina import *
app = Ursina()
EditorCamera()
def input(key):
    if key == 'escape':
        application.quit()

cube = Entity (
    model='plane',
    scale=1000,
    position=(0,-10,0),
    color=color.black)

cube00 = Entity (
    model='plane',
    texture='assets/cpu.png',
    scale=150,
    position=(-100,0,100),
    color=color.white,
    rotation = (0,270,0))

cube000 = Entity (
    model='plane',
    texture='assets/m.png',
    scale=150,
    position=(-100,0,-100),
    color=color.white,
    rotation = (0,270,0))

a = 0
cube1 = Entity(model='cube', color=color.red, collider='box', scale=5,position=(0,0,10))
cube2 = Entity(model='cube', color=color.orange, collider='box', scale=5,position=(0,0,20))
cube3 = Entity(model='cube', color=color.yellow, collider='box', scale=5,position=(0,0,30))

cube4 = Entity(model='cube', color=color.red, collider='box', scale=5,position=(0,0,40))
cube5 = Entity(model='cube', color=color.orange, collider='box', scale=5,position=(0,0,50))
cube6 = Entity(model='cube', color=color.yellow, collider='box', scale=5,position=(0,0,60))

cube7 = Entity(model='cube', color=color.red, collider='box', scale=5,position=(0,0,70))
cube8 = Entity(model='cube', color=color.orange, collider='box', scale=5,position=(0,0,80))
cube9 = Entity(model='cube', color=color.yellow, collider='box', scale=5,position=(0,0,90))

cube0 = Entity(model='cube', color=color.red, collider='box', scale=5,position=(0,0,100))




t = 0 
def input(key):
    global a, t
    if key == 'left mouse down':  # 마우스 왼쪽 버튼 눌렀을 때
        if mouse.hovered_entity == cube1:
            a = 1
            cube1.color = color.random_color()
            print('큐브 클릭! 색이 바뀜!')
    if key=='1':
        cube1.color=color.random_color()
        t+=1
        print(f't값 {t}')

    if key=='2':
        cube2.color=color.random_color()

    if key=='3':
        cube3.color=color.random_color()

    if key=='4':
        cube4.color=color.random_color()

    if key=='5':
        cube5.color=color.random_color()

    if key=='6':
        cube6.color=color.random_color()

    if key=='7':
        cube7.color=color.random_color()

    if key=='8':
        cube8.color=color.random_color()

    if key=='9':
        cube9.color=color.random_color()

    if key=='0':
        cube0.color=color.random_color()

ube_text=Text(text = t, x = -0.2, y = 0.2, parent = cube000, scale = 2, color = color.black, rotation = (90,0,0))


wall=[[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0]
]

for i in range(len(wall)): #i는 행의 개수를 의미 >> 5
    for j in range(len(wall[i])): #j는 열의 개수를 의미 >> 10
        if wall[i][j]: #i, j 인자를 주소로 리스트 값에 접근해 T/F 판단
            test = Entity(
                model = 'plane',
                texture = 'brick',
                color = "#949494",
                scale = 5,
                position = (i * 5,0,j * 5)
            )
        else:
            test = Entity(
                model = 'plane',
                texture = 'brick',
                color = "#292929",
                scale = 5,
                position = (i*5, 0, j*5)
            )




abcd = Entity(model = 'cube', position = (-150, 0, -20))
abcd2 = Entity(model = 'cube', position = (-150, 0, -10))
abcd3 = Entity(model = 'cube', position = (-150, 0, 0))
abcd4= Entity(model = 'cube', position = (-150, 0, 10))
abcd5= Entity(model = 'cube', position = (-150, 0, 20))
abcd6= Entity(model = 'cube', position = (-50, 0, -20))
abcd7= Entity(model = 'cube', position = (-50, 0, -10))
abcd8= Entity(model = 'cube', position = (-50, 0, 0))
abcd9= Entity(model = 'cube', position = (-50, 0, 10))
abcd10= Entity(model = 'cube', position = (-50, 0, 20))
def update():
    abcd.color = "#15e9bb"
    abcd2.color = "#15e9bb"
    abcd3.color = "#15e9bb"
    abcd4.color = "#15e9bb"
    abcd5.color = "#15e9bb"
    abcd6.color = "#15e9bb"
    abcd7.color = "#15e9bb"
    abcd8.color = "#15e9bb"
    abcd9.color = "#15e9bb"
    abcd10.color = "#15e9bb"



    if t == 1:
        abcd.color = "#f30808"
    if t == 2:
        abcd2.color = "#f30808"
    if t == 3:
        abcd3.color = "#f30808"
    if t == 4:
        abcd4.color = "#f30808"
    if t == 5:
        abcd5.color = "#f30808"
    if t == 6:
        abcd6.color = "#f30808"
    if t == 7:
        abcd7.color = "#f30808"
    if t == 8:
        abcd8.color = "#f30808"
    if t == 9:
        abcd9.color = "#f30808"
    if t == 10:
        abcd10.color = "#f30808"






app.run()