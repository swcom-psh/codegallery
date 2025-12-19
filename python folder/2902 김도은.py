from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
EditorCamera()

window.color = color.light_gray
camera.orthographic = True
camera.fov = 20
ground = Entity(model='cube', color=color.olive.tint(-.4), z=-.1, y=-1, origin_y=.5, scale=(1000,100,10), collider='box', ignore=True)
'''
random.seed(20)
for i in range(10):
    Entity(model='cube', color=color.dark_gray, collider='box', ignore=True  , position=(random.randint(-40,40), random.randint(0,10)), scale=(random.randint(1,20), random.randint(2,5), 10))'''
'''Entity(model='cube',
    color=color.dark_gray,
    collider='box', ignore=True,
    position=(random.randint(-40,40), random.randint(0,10)),
    scale=(random.randint(1,20),random.randint(2,5), 10)) '''

def input(key):
    if key == 'escape':
        application.quit()

wall = [
    [1,1,1,0,0,1], #이 한줄이 세로로 형성되는것것
    [1,0,4], #즉, 여러 줄이 가로를 만든는것임임]
    [0,0,0], 
    [0,0,0],
    [0,0,3],
    [1,0,3],
    [0,8,0],
    [0,0,0], 
    [1,0,3],
    [0,0,0],
    [0,0,3],
    [0,0,3], #이 한줄이 세로로 형성되는것것
    [1,0,0], #즉, 여러 줄이 가로를 만든는것임임]
    [0,2,0],
    [0,9,0],
    [0,2,0],
    [0,0,3],
    [0,0,3],
    [0,2,0],
    [0,0,0],
    [0,0,3],
    [0,0,3],
    [0,2,3], #이 한줄이 세로로 형성되는것것
    [0,0,0], #즉, 여러 줄이 가로를 만든는것임임]
    [0,2,0],
    [0,0,0],
    [0,2,3],
    [1,0,3],
    [0,0,0],
    [0,2,0],
    [0,0,3],
    [0,0,3],
    [0,0,3], #이 한줄이 세로로 형성되는것것
    [0,0,0], #즉, 여러 줄이 가로를 만든는것임임]
    [0,2,0],
    [0,0,0],
    [0,2,3],
    [0,0,3],
    [0,0,3],
    [0,2,0],
    [0,0,0],
    [0,0,3],
    [0,0,3],
    [9,2,0],
    [0,2,3],
    [0,0,3],
    [0,2,0],
   
]

for i in range(len(wall)): #i는 행의 개수를 의미 >> 5
    for j in range(len(wall[i])): #j는 열의 개수를 의미 >> 10
        if wall[i][j]: #i, j 인자를 주소로 리스트 값에 접근해 T/F 판단
            test = Entity(
                model = 'cube',
                texture = 'brick',
                color = "#ffb700",
                scale = (6,3.25),
                position = (i * 5, j * 5,0),
                collider= 'box'
            )



player = PlatformerController2d()
player.x = 10
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

coins = []

coin_positions = [
    (0,0,0),
    (15,3.48,0),
    (25,3.48,0),
    (25,13.48,0),
    (29.3,8.198,0),
    (5,13.48,0),
    (5,13.48,0),
    (40,3,0),
    (60,3,0),
    (63.3,8.198,0),
    (67.3,8.198,0),
    (71.3,8.198,0),
    (75.3,8.198,0),
    (80.9,0,0),
    (97,0.999,0),
    (103,0,0),
    (117,0,0),
    
    
]
for pos in coin_positions:
    coin = Entity(
        model='circle',
        position=pos,
        color=color.yellow,
        collider='box',
        scale=2
    )
    coins.append(coin)


def update():
    for coin in coins:
        if coin.enabled and player.intersects(coin):
            coin.enabled = False



app.run()