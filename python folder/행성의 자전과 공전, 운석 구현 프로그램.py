from ursina import *
from random import uniform   # 랜덤 위치
#김예준
app = Ursina()
window.color = color.black   # 배경을 검정색으로
EditorCamera()


# 행성 클래스
class Planet(Entity):
    def __init__(self, texture, position, a, speed, orbit=0):
        super().__init__(
            model='sphere',
            texture=texture,
            position=position,
            scale=a,
            parent=scene
        )
        self.speed = speed
        self.orbit = orbit

        # 공전 중심점(보이지 않는 축)
        self.pi = Entity(position=(0, 0, 0))
        self.parent = self.pi

# 별 만들기 
stars = []

def create_stars(amount=200):
    for i in range(amount):
        x = uniform(-300, 300)
        y = uniform(-300, 300)
        z = uniform(-300, 300)

        # 행성들이 보이도록 태양계 근처는 비워뒀습니다.
        if -100 < x < 100 and -100 < y < 100 and -100 < z < 100:
            continue

        star = Entity(
            model='sphere',
            scale=0.4,
            color=color.white,
            position=(x, y, z),
            parent=scene
        )
        stars.append(star)

create_stars()



# 운석 클래스
class Meteor(Entity):
    def __init__(self, position, direction, speed=0.8):
        super().__init__(
            model='sphere',
            color=color.orange,
            scale=1,
            position=position,
            parent=scene
        )
        self.direction = direction.normalized()
        self.speed = speed

#태양계 행성들
planets = []


planets.append(Planet('textures/sun.jpg',     (0,0,0),   25, 0.05, 1))
planets.append(Planet('textures/Mercury.jpg', (15,0,0),  0.5, 0.7, 1.5))
planets.append(Planet('textures/Venus.jpg',   (20,0,0),  1,   0.8, 1))
planets.append(Planet('textures/Earth.jpg',   (30,0,0),  1,   1.2, 0.7))
planets.append(Planet('textures/Mars.jpg',    (40,0,0),  0.5, 2.0, 0.3))
planets.append(Planet('textures/Jupiter.jpg', (50,0,0), 10,   3.5, 0.1))
planets.append(Planet('textures/Saturn.jpg',  (-60,0,0), 8,   8.5, 0.08))
planets.append(Planet('textures/Uranus.jpg',  (70,0,0),  3.8, 9.5, 0.05))
planets.append(Planet('textures/Neptune.jpg', (-80,0,0), 3.7, 10,  0.03))


meteors = []   # 운석들을 담을 리스트


# 운석 생겨나는 곳 (랜덤 위치 + 대각선 방향)
def spawn_meteor():
    # 화면 위쪽 어딘가에서 랜덤으로 시작
    x = uniform(-80, 80)
    y = uniform(40, 60)
    z = uniform(-80, 80)

    start_pos = Vec3(x, y, z)

    # 대각선 방향 (왼쪽 아래, 뒤쪽 방향으로)
    direction = Vec3(-1, -1, -0.3)

    meteor = Meteor(start_pos, direction, speed=0.9)
    meteors.append(meteor)


# 키 입력
def input(key):
    if key == 'escape':
        application.quit()

    # 스페이스바 누르면 운석 생성
    if key == 'space':
        spawn_meteor()


# 매 프레임마다 실행합니다.
def update():
    # 행성 자전 + 공전
    for p in planets:
        p.rotation_y += p.speed
        p.pi.rotation_y += p.orbit

    # 운석 이동
    for m in meteors[:]:
        m.position += m.direction * m.speed

        # 너무 멀리 나가면 없어집니다.
        if m.y < -50 or abs(m.x) > 150 or abs(m.z) > 150:
            meteors.remove(m)
            destroy(m)


app.run()
