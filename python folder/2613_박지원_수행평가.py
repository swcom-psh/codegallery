from ursina import *

app = Ursina()
EditorCamera()


rocket = Entity(model='assets/Barrel_02_4k.fbx', color=color.blue, scale=0.01, position=(0, 0.01, 0), collider='box')
ground = Entity(model='plane', color=color.gray, scale=(50, 50, 50), collider='box', position=(0, 0, 0))


g= 9.8
y=18
z=48

ck = False  
Sky(texture = "sky_sunset")
def update():
    global ck,y,z,g,x



    if held_keys['space'] and not ck:
        x=5
        ck = True 
    #if held_keys['a'] and not ck:
        #rocket.rotation_z += 5
        #print(rocket.rotation)  

 
    if ck:
        rocket.rotation_z += z * time.dt
        x = x - 1 * time.dt
        print(rocket.position)
    if ck:
   
        rocket.x += x * time.dt
        rocket.y += y * time.dt

       
        y -= g * time.dt



    if rocket.y <= 0.01: 
        rocket.y = 0.01 
        x = 0  
        ck = False  

app.run()
