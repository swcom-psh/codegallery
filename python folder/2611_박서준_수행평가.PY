from ursina import*
import random as ran


from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()  
#EditorCamera()
objects =2000
somethings = []

player = FirstPersonController(model = 'cube', color=color.gray, collider = 'box', speed = 25 ,jump_height = 0)

def input(key):
    if key == 'escape':
        application.quit()
    if held_keys['r']:
        player.enabled = True
        clear.visible = False
        king.visible = False
        player.position = (0,0,0)


sea = Entity(model = 'plane', scale = (1000,-5,100), collider = 'box', position = (0,0,0), color = "#0097FC")
goal = Entity(model = 'plane', scale = (1100,-5,100), collider = 'box', position = (0,-1,0), color = "#FFFFFF")

for obj in range(objects):

    # 플레이어 주변 금지 반경
    forbidden_radius = 10

    while True:
        pos = (ran.uniform(-500, 500), 0, ran.uniform(-50, 50))

        # 플레이어 위치와의 거리 계산
        dist = distance(player.position, pos)

        # 금지 영역 밖이면 스폰 위치로 확정
        if dist > forbidden_radius:
            break

    cube = Entity(
        model='cube',
        position=pos,
        scale=(2, 2, 2),
        color= "00FFD5",
        collider='box'
    )
    somethings.append(cube)


clear = Text( #텍스트 객체를 생성하고, self.clear 변수에 저장합니다.
            text = 'RESTART = R', #출력할 메시지를 작성합니다.
            scale = 2, #텍스트의 크기
            origin = (0,0), #텍스트의 좌표(2차원)
            color=color.white,
            visible = False #텍스트는 우선 눈에 보이지 않게 하였습니다.
)

king = Text( #텍스트 객체를 생성하고, self.clear 변수에 저장합니다.
            text = 'goal!!!', #출력할 메시지를 작성합니다.
            scale = 2, #텍스트의 크기
            origin = (0,0), #텍스트의 좌표(2차원)
            color=color.black,
            visible = False #텍스트는 우선 눈에 보이지 않게 하였습니다.
)

def update():
    for i in somethings:
        if i.intersects(player).hit:
            player.enabled = False
            clear.visible = True
    if goal.intersects(player).hit:
        player.enabled = False
        king.visible = True

app.run()