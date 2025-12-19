from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

player = FirstPersonController(position=(16, 2, 10), speed=6)
camera.fov = 90

score = 0
score_text = Text(text=f"Score: {score}", position=(-0.85, 0.45), scale=2)

clear = Text(
    text = 'gameover',
    scale = 2,
    origin = (0,0),
    color = color.white,
    visible = False
)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x,0,z))

sphere1 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(13,7,0))
sphere2 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(10,5,0))
sphere3 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(14,4,0))
sphere4 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(17,6,0))
sphere5 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(15,9,0))
sphere6 = Entity(model='sphere', color=color.green, scale=1, collider='box', position=(16,8,0))

spheres = [sphere1, sphere2, sphere3, sphere4, sphere5, sphere6]


def input(key):
    if key == 'escape':
        application.quit()

    if key == 'left mouse down':
        global score
        for s in spheres:
            if mouse.hovered_entity == s:
                s.color = color.random_color()
                score += 1
                score_text.text = f"Score: {score}"
                if s == sphere1:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
                if s == sphere2:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
                if s == sphere3:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
                if s == sphere4:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
                if s == sphere5:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
                if s == sphere6:
                    s.y = random.uniform(3.0, 11.0) 
                    s.x = random.uniform(9.0, 16.0)
        if mouse.hovered_entity == None:
                clear.visible = True
        


               
app.run()
