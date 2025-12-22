from ursina import *
import math
import random
#전해찬

app = Ursina()


window.color = color.black
EditorCamera()
camera.position = (0, 10, -30)
camera.look_at((0, 10, 0))




Text(text='DNA Visualization', position=(-0.85, 0.45), scale=1.5)



dna_structure = Entity(position=(0, -10, 0))




pairs = [
    (color.red, color.blue),      # A - T
    (color.green, color.yellow)   # G - C
]




height = 40      
steps = 60        
radius = 4        
twist_speed = 0.5


for i in range(steps):
   
    y = i * 0.8
    angle = i * twist_speed
   
   
   
    x1 = math.sin(angle) * radius
    z1 = math.cos(angle) * radius
   
   
    x2 = math.sin(angle + math.pi) * radius
    z2 = math.cos(angle + math.pi) * radius
   
   
    Entity(model='sphere', color=color.white, scale=0.8, position=(x1, y, z1), parent=dna_structure)
    Entity(model='sphere', color=color.white, scale=0.8, position=(x2, y, z2), parent=dna_structure)
   
   
    pair_color = random.choice(pairs)
   
   
    Entity(model='cube', color=pair_color[0], scale=(radius, 0.2, 0.2),
           position=((x1)/2, y, (z1)/2), look_at=Vec3(0,y,0), parent=dna_structure)
           
   
    Entity(model='cube', color=pair_color[1], scale=(radius, 0.2, 0.2),
           position=((x2)/2, y, (z2)/2), look_at=Vec3(0,y,0), parent=dna_structure)




for i in range(50):
    Entity(
        model='sphere',
        color=color.rgba(100, 255, 100, 50),
        scale=random.uniform(0.1, 0.5),
        position=(random.uniform(-20, 20), random.uniform(-10, 30), random.uniform(-20, 20))
    )


def update():
   
    dna_structure.rotation_y += 30 * time.dt
   
   
    dna_structure.y += math.sin(time.time()) * 0.02


app.run()

