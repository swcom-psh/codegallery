#2105 김솔희 수행평가
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
EditorCamera()


class xx(Entity):
    def __init__(self, rotation, position, color):
        super().__init__(
            model = 'quad',
            scale = (1,5,5),
            rotation = rotation,
            position = position,
            color = color
            )


class cc(Entity):  
    def __init__(self, rotation, position):
        super().__init__(
            model = 'circle',
            color = color.white,
            scale = (10,10,10),
            rotation = rotation,
            position = position
            )


# 왼       
cc(rotation = (0,0,0), position = (0,0,1))
cc(rotation = (0,0,0), position = (-9,-9,1))
cc(rotation = (0,0,0), position = (9,-9,1)) # 1
cc(rotation = (0,0,0), position = (-6,-22,1))
cc(rotation = (0,0,0), position = (6,-22,1))
cc(rotation = (0,0,0), position = (19,-22,1)) # 2
cc(rotation = (0,0,0), position = (-19,-22,1)) # 3


# 오
cc(rotation = (0,0,0), position = (55,0,1))
cc(rotation = (0,0,0), position = (46,-9,1))
cc(rotation = (0,0,0), position = (64,-9,1)) # 1
cc(rotation = (0,0,0), position = (49,-22,1))
cc(rotation = (0,0,0), position = (61,-22,1))
cc(rotation = (0,0,0), position = (73,-22,1)) # 2
cc(rotation = (0,0,0), position = (36,-22,1)) # 3


pi = Entity(position = (0,0,0))
a = []
a1 = xx(rotation = (0,0,20) , position = (-1.5,0,0), color = color.pink)
a.append(a1)
a2 = xx(rotation = (0,0,-20) , position = (-1.5,0,0), color = color.pink)
a.append(a2)
a3 = xx(rotation = (0,0,20) , position = (1.5,0,0), color = color.blue)
a.append(a3)
a4 = xx(rotation = (0,0,-20) , position = (1.5,0,0), color = color.blue)
a.append(a4)


a1.parent = pi
a2.parent = pi
a3.parent = pi
a4.parent = pi


qi1 = Entity(position = (0,0,0))
qi2 = Entity(position = (0,0,0))
b = []
b1 = xx(rotation = (0,0,20) , position = (53.5,0,0), color = color.pink)
b.append(b1)
b2 = xx(rotation = (0,0,-20) , position = (53.5,0,0), color = color.pink)
b.append(b2)
b3 = xx(rotation = (0,0,20) , position = (56.5,0,0), color = color.blue)
b.append(b3)
b4 = xx(rotation = (0,0,-20) , position = (56.5,0,0), color = color.blue)
b.append(b4)


b1.parent = qi1
b2.parent = qi1
b3.parent = qi2
b4.parent = qi2


def update():
    if pi.y > -9:
        pi.x += 0.06
        pi.y -= 0.06 

        qi1.x -= 0.05
        qi1.y -= 0.06 
        qi2.x += 0.05
        qi2.y -= 0.06 
        
    elif a1.x > -4.7:
        a1.x -= 0.01 
        a1.y -= 0.04
        a2.x += 0.03 
        a2.y -= 0.04 
        a3.x -= 0.01 
        a3.y -= 0.04 
        a4.x += 0.03 
        a4.y -= 0.04 

        b1.x += 0.004
        b1.y -= 0.04
        b2.x += 0.013
        b2.y -= 0.04
        b3.x -= 0.01 
        b3.y -= 0.04 
        b4.x += 0.03 
        b4.y -= 0.04


app.run()