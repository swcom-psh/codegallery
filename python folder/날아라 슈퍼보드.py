#조은찬
from ursina import *

app = Ursina()
EditorCamera()
window.color= color.black
 
plane = Entity()

body = Entity(parent= plane, model='cube', color=color.gray, scale= (5, 1, 1.4))  #동체 (Body)

nose = Entity(parent= plane, model='cube', color=color.gray, scale= (1.8, 0.8, 1), position= (3, 0, 0))  #기수 (Nose)

canopy = Entity(parent= plane, model='sphere',color= color.azure, scale= (1.2, 0.5, 0.8), position= (1.5, 0.4, 0))  #캐노피 (canopy, 조종석)

left_wing = Entity(parent= plane, model='cube', color=color.gray, scale= (1, 0.1, 4), position = (-0.5, 0, 2), rotation = (0, -30, 0)) #주날개 (Main Wings)  
right_wing = Entity(parent= plane, model='cube', color=color.gray, scale= (1, 0.1, 4), position = (-0.5, 0, -2), rotation = (0, 30, 0)) #주날개 (Main Wings)  

left_tail = Entity(parent= plane, model='cube', color=color.gray, scale= (0.2, 1, 0.6), position = (-2.5, 0.7, 0.7), rotation = (0, 0, -25)) #수직 미익 (Tail Fins, v자)
right_tail = Entity(parent= plane, model='cube', color=color.gray, scale= (0.2, 1, 0.6), position = (-2.5, 0.7, -0.7), rotation = (0, 0, -25)) #수직 미익 (Tail Fins, v자)

engine =Entity(parent= plane, model='cube', color=color.gray, scale= (1.5, 0.8, 1), position = (-2.8, -0.1, 0) ) #엔진 (Engine Block)



app.run()






