#이지환의 수행평가
from ursina import *
import math

app = Ursina()
EditorCamera()

a = Entity(position=(0, 3, 0))#
b = Entity()
m = Entity()
c = Entity(model='cube', scale=(0.05, 3, 0.05), color=color.gray, parent=b)

v = Entity()
class d(Entity):  
    def __init__(self,position, scale, color):
        
        super().__init__(model = 'sphere', position = position, scale = scale, color = color) 

h = d(position=Vec3(0,-1.5,0), scale= 1, color= color.blue)
k= d(position=Vec3(-1,-1.5,0), scale = 1, color= color.red)
    
h.parent= b
k.parent = m 


A = 25
g = 9.8
L = 1.5
t = 0
w = math.sqrt(g / L)

trail_dots = []
max_trail = 50
dis = 0.1
speed = 10

def update():
    global dis
    
    b.rotation_z += dis * speed
    
    
    if b.rotation_z > 50:
        dis = dis * -1
    elif b.rotation_z < -50:
        dis = dis * -1   
    
    


    m.rotation_z += dis * speed
    
    
    if b.rotation_z > 90:
        dis = dis * -1
    elif m.rotation_z < -90:
        dis = dis * -1   
    
    print(m.rotation_z)
    print(b.rotation_z)  

    
    
app.run()
    

   