from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
EditorCamera()
Var=color.black
window.color=color.gray
player=FirstPersonController()
player.position=(0,0,0)
player.cursor=True
player.gravity=0
player.speed=100
lst=[]
for Xx in range(15):
    for Yy in range(15):
        for Zz in range(15):
            dhahrvks=Entity(
                model="wireframe_cube",
                scale=(10,10,10),
                color=color.black,
                position=(Xx*20,Yy*20,Zz*20),
                collider="box"
            )
            lst.append(dhahrvks)
            dhahrvks.is_wire=True
def input(key):
    global Var
    if key=='escape':
        application.quit()
    if key=='space':
        player.y+=10
    if key=='f':
        player.y-=10
    if key=="left mouse down":
        for i in lst:
            if mouse.hovered_entity==i:
                clicked=mouse.hovered_entity
                spawn_pos=getattr(clicked,'world_position',clicked.position)+Vec3(0,5,0)
                dhahrehf=Entity(
                    model="sphere",
                    position=spawn_pos,
                    scale=(1,0.7,1),
                    collider="box",
                    color=Var
                    )
                if Var==color.white:
                    Var=color.black
                else:
                    Var=color.white
app.run()