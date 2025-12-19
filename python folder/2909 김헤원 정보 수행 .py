from ursina import *
import math
import random as ran

app = Ursina()

window.color = color.white

EditorCamera()

objects = 1
somethings = []

cube = Entity(model = 'cube', scale = (0.01,1000, 0.1), position = (-3,0,0), color = color.black)
cube = Entity(model = 'cube', scale = (1000,0.01, 1), position = (0,0,0), color = color.black)

# 지수함수 y = e^x 그리기
def draw_exp_function():
    points = []

    # x 범위: -5 ~ 5
    for i in range(200):
        x = lerp(-5, 5, i/200)
        y = math.exp(x)
        points.append(Vec3(x, y, 0))
    a = ran.uniform(0,5)
    print(f'a값: {a}')
    x= lerp(0, 5, a/200)
    y= math.exp(x)
    print(x)
    print(y)
    Entity(model = 'sphere', scale = (0.05,0.05,0.05), position = (x,y,0), color = color.black)
    b = ran.uniform(1,5)
    x = lerp(1, 5, b/200)
    y = math.exp(x)
    Entity(model = 'sphere', scale = (0.05,0.05,0.05), position = (x,y,0), color = color.black) 
    
    curve = Entity(
        model=Mesh(vertices=points, mode='line'),
        color=color.black,
        thickness=2
    )

draw_exp_function()






app.run()

