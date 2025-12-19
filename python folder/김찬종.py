from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.

app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()




#기본적인 바탕이되는 Entity이다.
background = Entity(model = 'quad',scale = 200, position = (0,0,0),color = color.green,texture= 'grass')

#player가 만날수있는 장애물 역할을 하는 Entity이다.
problem = Entity(model = 'cube',scale = 2, position = (-8,1,0),color = color.red,collider='sphere')






#player라는 물체를 wasd를 사용하여 4가지 방향으로 움직입니다.
from ursina import *
app = Ursina()
player = Entity(model='sphere', color=color.blue, scale=1,collider='box')

def update():
    if held_keys['a']:  
        player.x -= 0.1  
    if held_keys['d']:  
        player.x += 0.1  
    if held_keys['w']:  
        player.y += 0.1 
    if held_keys['s']:  
        player.y -= 0.1  




 # 만약 player가 움직이다가 problem이라는 물체와 충돌하면
    if player.intersects(problem).hit:
        problem_2 = Text(text ='3+5=', scale = 5, position = (-0.15,0.5,0),)
        problem_2.color = color.black # 문제식의 색을 변경합니다.






    




app.run()





