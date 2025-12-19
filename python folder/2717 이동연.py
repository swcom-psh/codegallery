from ursina import *

app =Ursina()
EditorCamera()


window.color=color.hex("#B9EBF8")


beaker = Entity(model = 'wireframe_cube', position = (0, 0, 0), collider = 'box', scale = 13, color = "#FFFFFF")
neutral = Entity(model = 'cube', position = (0, 0, 0), collider = 'box', scale = 12, color = "#027E27")


HAbeaker = Entity(model = 'wireframe_cube', position = (-3, 15, 0), collider = 'box', scale = 4, color = "#FFFFFF")
acid = Entity(model = 'cube', position = (-3, 15, 0), collider = 'box', scale = 3, color = "#DDE032")


BOHbeaker = Entity(model = 'wireframe_cube', position = (3, 15, 0), collider = 'box', scale = 4, color = "#FFFFFF")
basic = Entity(model = 'cube', position = (3, 15, 0), collider = 'box', scale = 3, color = "#4657EE")


def input(key):
    if key == 'left mouse down':  
        if mouse.hovered_entity == HAbeaker:
            HAbeaker.y += -12
    if key == 'left mouse down':  
        if mouse.hovered_entity == HAbeaker:
            acid.animate('y', -3, duration = 2)
def update():
    if acid.intersects(neutral).hit:
        neutral.color = "#DDE032"

         
def input(key):
    if key == 'right mouse down':  
        if mouse.hovered_entity == BOHbeaker:
            BOHbeaker.y += -12
    if key == 'right mouse down':  
        if mouse.hovered_entity == BOHbeaker:
            basic.animate('y', -3, duration = 2)


def update():
    if basic.intersects(neutral).hit:
        neutral.color = "#4657EE"


app.run()