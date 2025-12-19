from ursina import *
#우르시나 라이브러리의 모든기능(=*)을 가져온다.
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()





window.color = color.rgb(0, 50, 100)     # 어두운 파란색
# 또는
window.color = color.azure               # 기본 색 이름으로도 가능
# 혹은
window.color = color.hex("#00c3ff")      # HEX 코드 사용 가능

window.size = (1280, 720)






ball = Entity(model='sphere', scale=2, position=(0,1,0), color=color.black, collider='sphere')
#EditorCamera()
player = FirstPersonController(
    position=(0,0,-5), #플레이어의 시작 좌표도 설정할 수 있고
    speed=20, #이동 속도 설정 가능
    jump_height=2, #점프 높이도 설정할 수 있음.
    collider = 'box'
) #1인칭 시점 화면 가져오기

ground = Entity(
    model='plane',
    scale=(100, 0, 100),
    texture='assets/잔디밭.jpg',
    color ="#0A7945",  
    collider='box') #반드시 충돌체가 있어야 함.

cube = Entity(model = 'cube',position = (0,3,25), scale = (20,6,5),  color="#7C590E")
cube = Entity(model = 'cube',position = (0,3,35), scale = (20,6,5),  color="#7C590E")
cube = Entity(model = 'cube',position = (-20,3,10), scale = (6,6,18),color="#7C590E")

cube = Entity(model = 'cube',position = (0,7,25), scale = (1,5,1),  color="#000000")
cube = Entity(model = 'cube',position = (-2,8,25), scale = (5,3,1),  color="#FFFFFF")

cube = Entity(model = 'sphere',position = (-2,8,24), scale = (1,1,1),  color="#1900FF")
cube = Entity(model = 'sphere',position = (-2,8.5,24), scale = (1,1,1),  color="#FF0000")

cube = Entity(model = 'cube',position = (-3.5,8.7,24), scale = (1,0.3,1),  color="#000000")
cube = Entity(model = 'cube',position = (-0.5,8.7,24), scale = (1,0.3,1),  color="#000000")
cube = Entity(model = 'cube',position = (-3.5,7,24), scale = (1,0.3,1),  color="#000000")
cube = Entity(model = 'cube',position = (-0.5,7,24), scale = (1,0.3,1),  color="#000000")


cube = Entity(model = 'cube',position = (-6,3.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")
cube = Entity(model = 'cube',position = (-2.5,3.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")
cube = Entity(model = 'cube',position = (1.5,3.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")
cube = Entity(model = 'cube',position = (5.5,3.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")

cube = Entity(model = 'cube',position = (-6,1.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")
cube = Entity(model = 'cube',position = (5.5,1.7,22.8), scale = (2.5,1.5,1),  color="#058FC5")


cube = Entity(model = 'cube',position = (-16.5,3.5,15), scale = (1,1.5,2.5), color="#058FC5")
cube = Entity(model = 'cube',position = (-16.5,3.5,10), scale = (1,1.5,2.5), color="#058FC5")
cube = Entity(model = 'cube',position = (-16.5,3.5,5), scale = (1,1.5,2.5), color="#058FC5")

cube = Entity(model = 'cube',position = (30,3,7), scale = (3,8,25),  color="#FFFFFF",texture = 'assets/골대.jpg', collider='box')

cube2 = Entity(model = 'quad',position = (5,3,7), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png' )
cube2 = Entity(model = 'quad',position = (-5,3,-2), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png')
cube2 = Entity(model = 'quad',position = (-8,3,10), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png')
cube2 = Entity(model = 'quad',position = (-7,3,15), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png')
cube2 = Entity(model = 'quad',position = (6,3,10), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png')
cube2 = Entity(model = 'quad',position = (9,3,20), scale = (3,8,3),  color="#FFFFFF",texture = 'textures/chemdgkrtod.png')


def input(key):
    if key == 'escape':
        application.quit()

    

def update():
    if ball.intersects(player).hit:
        ball.x += 5  # 공의 위치를 다시 위로 올립니다.
        ball.color = color.random_color()  # 공의 색상을 랜덤으로 변경
    
    if ball.intersects(cube).hit:
        ball.x -= 40  # 공의 위치를 다시 위로 올립니다.
        cube.color = color.random_color()
        window.color = color.random_color() 

        
app.run()
