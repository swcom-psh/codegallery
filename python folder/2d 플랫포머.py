from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina() 
camera.orthographic = True
camera.fov = 20
#플레이어
player = PlatformerController2d(
    position=(-15,-5),
    texture='cube',
    color=color.blue,
    scale=1,
    max_jumps=2
)
#최지환


#땅
ground = Entity(
    model='cube',
    color=color.green,
    z=0.1,
    y=-8,
    scale=(100,5,10),
    collider='box'
)
#떠있는 땅
flatform = Entity(
    model='cube',
    color=color.green,
    position=(-3, 0),
    collider='box',
    scale=(5,1)
)

#장애물
objects = []
clear = []
for i in range(10):
    object = Entity(
        model='cube',
        color=color.red,
        collider='box',
        position=(random.randint(-10, 10), -5),
        scale=1
    )

    objects.append(object)
    goal = Entity(
        model='cube',
        color=color.yellow,
        collider='box',
        position=(15,-5),
        scale=1
    )
    clear.append(goal)

#장애물에 닿으면 처음으로
def update():
    hit_info = player.intersects()

    if hit_info.hit:
        if hit_info.entity in objects:
            player.position = (-15, -5)
    if hit_info.hit:
        if hit_info.entity in clear:
            print('clear!')



app.run()