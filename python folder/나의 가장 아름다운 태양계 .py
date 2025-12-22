#한성윤
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

Sky(texture = 'stars.jpg')

sun_texture = load_texture('textures/sun.jpg')
earth_texture = load_texture('textures/earth.jpg') #지구
jupiter_texture = load_texture('textures/jupiter.jpg') #목성
mars_texture = load_texture('textures/mars.jpg') #화성
mercury_texture = load_texture('textures/mercury.jpg') #수성
moon_texture = load_texture('textures/moon.jpg') #달
neptune_texture = load_texture('textures/neptune.jpg') #해왕성
saturn_ring_texture = load_texture('textures/saturn_ring.jpg') #토성 고리
saturn_texture = load_texture('textures/saturn.jpg') #토성
stars_texture = load_texture('textures/stars.jpg') #별
uranus_texture = load_texture('textures/uranus.jpg')  #천왕성
venus_texture = load_texture('textures/venus.jpg') #금성

radius = 0.1
dis = Vec3(10, 0, 0)

class Planet(Entity):
    def __init__(self, name, texture, position, scale, rotation_speed, orbit = 0):
        super().__init__( # 부모(Entity)의 기능을 받아온다. 
            model = 'sphere',
            texture = texture,
            position = position,
            scale = scale,
            rotation_speed = rotation_speed,
            parent = scene
        )
        self.name = name
        self.orbit = orbit
        if self.orbit != 0 and self.name != 'Sun':
            self.pivot()

    def pivot(self):
        pivot_name = f'{self.name}_pivot'
        self.pi = Entity(
            name = pivot_name,
            position = (0,0,0),            
        )

        self.parent = self.pi

    def dir(self):
        self.dir = Entity(
            model = 'sphere',
            position = self.position
        )


    def update(self):
        self.rotation_y += self.rotation_speed * time.dt
        if hasattr(self, 'pi'):
            self.pi.rotation_y += self.orbit * time.dt


def draw_orbit(radius, segments=160):
    from math import sin, cos, pi

    points = []
    for i in range(segments + 1):
        angle = (2 * pi / segments) * i
        x = radius * cos(angle)
        z = radius * sin(angle)
        points.append(Vec3(x, 0, z))

    return Entity(
        model=Mesh(vertices=points, mode='line', thickness=2),
        color= "#fdfdfd",  
        position=(0,0,0)
    )



draw_orbit(10 * 0.4)   # 수성
draw_orbit(10 * 0.7)   # 금성
draw_orbit(10 * 1.0)   # 지구
draw_orbit(10 * 1.5)   # 화성
draw_orbit(10 * 5.2)   # 목성
draw_orbit(10 * 9.5)   # 토성
draw_orbit(10 * 19.2)  # 천왕성
draw_orbit(10 * 30.1)  # 해왕성

Planet('Sun', sun_texture, (0,0,0), (radius * 2) * 30, 1.9969)
Planet('mercury', mercury_texture, dis * 0.4, (radius * 2) * 1, 0.003, 47.87 )
Planet('venus', venus_texture, dis * 0.7, (radius * 2) * 2, 0.0018, 35)
Planet('earth', earth_texture, dis * 1, radius * 2, 3,29)
Planet('mars', mars_texture, dis * 1.5, (radius * 2) * 0.5, 0.2411,24)
Planet('jupiter', jupiter_texture, dis * 5.2, (radius * 2) * 11.2, 12.6,13)
Planet('saturn', saturn_texture, dis * 9.5, (radius * 2) * 9.4, 9.87,9.6)
Planet('uranus', uranus_texture, dis * 19.2, (radius * 2) * 4.0, 2.59,6.8)
Planet('neptune', neptune_texture, dis * 30.1, (radius * 2) * 3.9, 2.68,5.4)

###
#행성 거리 정리...
# 태양 -- 수성 : 

app.run()