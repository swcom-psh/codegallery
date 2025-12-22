from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()
__ = False

window.color = color.hex("#1F1D1D")
check_pos = Vec3(10, 7, 10)
class Player(FirstPersonController):
     def __init__(self):
          super().__init__(
               speed = 10,
               model = 'cube',
               collider = 'box',
               scale = 1,
               position = (10, 2, 8)
          )

player = Player()

def input(key):
    if key == 'escape':
        application.quit()

ground = Entity(model = 'plane',
                scale = (1000, 0, 1000),
                collider = 'box',
                position = (0, 0, 0),
                color="#ffffff",
                texture='textures/lava.jpg')

start = Entity(
     model = 'cube',
     collider = 'box',
     scale = (20, 0.5, 13),
     position = (8, 2, 5),
     color = '2a2b2cbd'
)

finish = Entity(
     model = 'cube',
     collider = 'box',
     scale = (20, 0.5, 13),
     position = (28, 2, 5),
     color = '2a2b2cbd'
)


platform_positions = [
    (10, 2, 15),
    (10, 1, 20),
    (12, 2, 23),
    (8, 3, 29),
    (11, 4, 33),
    (10, 5, 38),
    (9, 6, 41),
    (9, 7, 45),
    (10, 8, 50),
    (11, 9, 57),
    (10, 10, 64),
    (10, 2, 73), #(좌우, 높이, 앞뒤)
    (7, 3, 78),
    (7, 3, 81),
    (25, 3, 81),
    (24, 4, 77),
    (26, 5, 74),
    (25, 6, 68),
    (23, 7, 62),
    (22, 8, 56),
    (27, 3, 24),
    (30, 3, 19),
    (27, 3, 15)
]

for pos in platform_positions:
    Entity(
        model='cube',
        color="#ffffffbe",
        scale=(3, 0.5, 3),
        position=pos,
        collider='box',
        texture = 'textures/stone.jpg'
    )

platform = Entity(
     model='cube',
     color="#bbbdffbd",
     scale=(3, 0.5, 3),
     position=(7, 3, 87),
     collider='box',
     direction=1,
     texture = 'textures/stone.jpg'
)

ddd = Entity(
     model='cube',
     color = '#ffffffbe',
     scale = (3, 0.5, 3),
     position = (25, 3.3, 81),
     collider = 'box',
     texture = 'textures/stone.jpg'
)


platform_real = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(29, 6, 39),
     collider='box',
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

platform_A = Entity(
     model='cube',
     color="#2a2b2cbd",
     scale=(15, 0.5, 3),
     position=(27, 9, 49),
     collider='box',
     direction=1
)

platform_B = Entity(
     model='cube',
     color="#2a2b2cbd",
     scale=(15, 0.5, 3),
     position=(27, 3, 30),
     collider='box',
     direction=1
)

platform_fake1 = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(25, 6, 39),
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

platform_fake2 = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(23, 6, 39),
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

platform_fake1 = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(27, 6, 39),
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

platform_fake1 = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(31, 6, 39),
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

platform_fake1 = Entity(
     model='cube',
     color="#ffffffbe",
     scale=(15, 0.5, 1),
     position=(33, 6, 39),
     direction=1,
     texture = 'textures/namu.jpg',
     rotation_y = 90,
     rotation_z = 20
)

speed = 5.5 #속도
dis = 1 #방향 용도


def update():
     global check_pos
     global dis
     global speed

     if player.intersects(ground):
          player.position = check_pos
     if player.intersects(platform):
          player.position = platform.position
     if player.intersects(ddd):
               #player.position = Vec3(25, 3.5, 81) 안써도 되는 코드였넹
               check_pos = Vec3(25, 3.5, 81)
     

     platform.x += dis * speed *time.dt
     #print(platform.x)

     if platform.x > 30:
          dis = dis * -1

     elif platform.x < 7:
          dis = dis * -1

     if player.intersects(finish):
          textt.visible = True
          player.position = (20,1000,50)
          #player.enabled = False
     
textt = Text(
               text = '!FINISH!',
               scale = 2,
               origin = (0,0),
               visible = False
          )

class Warp(Entity):
     def __init__(self):
          super().__init__( #Entity의 속성을 그대로 물려받아 초기화하기 위해 작성하는 구문
               warp = Entity(
                    model = 'cube',
                    color = "#524F4F",
                    position = (100,100,100),
                    scale = (5, 5, 5),
                    collider = 'box'
               )                          
          )
Warp()

MAP =[
    [-50,-50,-50,-50,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [-50,-50,-50,-50,1,1,1,1,1,1,1,1,1,1,1,1,1,__,__,1], #20칸
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [1,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,1],
    [-50,-50,-50,-50,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
          if MAP[i][j]:
               if MAP[i][j] == 'w': 
                    warpgate = Warp() # warpgate 객체를 생성하고, Exit 클래스 호출하며 i, j 값 전달     
                    continue

               wall = Entity(                
                    model = 'cube',
                    color = "#5E524D",
                    position = (i * 5, 0, j * 5),
                    scale = (5,30,5),
                    collider = 'box',
                    texture='textures/wall.jpg'
                    )










app.run()