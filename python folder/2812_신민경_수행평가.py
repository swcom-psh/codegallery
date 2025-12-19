from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

#얼굴
cube = Entity(model = 'sphere',position = (0, 0, 5), scale = 6, color = "#eff5ee")
cube = Entity(model = 'sphere',position = (-1.5, 2.5, 5), scale = 1.5, color = "#eff5ee")
cube = Entity(model = 'sphere',position = (1.5, 2.5, 5), scale = 1.5, color = "#eff5ee")

#눈
cube = Entity(model = 'sphere',position = (0.6, 0.8, 2), scale = 0.2, color = "#111110")
cube = Entity(model = 'sphere',position = (-0.6, 0.8, 2), scale = 0.2, color = "#111110")

#코
cube = Entity(model = 'cube',position = (-0.2, 0.1, 2), scale = (1,0.3), color = "#E66109")


#몸
cube = Entity(model = 'sphere',position = (0, -4.5, 5), scale = 6, color = "#eff5ee")

#바닥
cube = Entity(model = 'plane',position = (0, -7.5, 6), scale = 30, color = "#eff5ee", collider= 'box')

#눈
ball1 = Entity(model = 'sphere',position = (6, 5, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball2 = Entity(model = 'sphere',position = (-3, 4, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball3 = Entity(model = 'sphere',position = (4, 7, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball4 = Entity(model = 'sphere',position = (-5, 6, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball5 = Entity(model = 'sphere',position = (-7, 8, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball6 = Entity(model = 'sphere',position = (8, 4, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball7 = Entity(model = 'sphere',position = (7, 10, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball8 = Entity(model = 'sphere',position = (-2, 10, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball9 = Entity(model = 'sphere',position = (-6, 9, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball10 = Entity(model = 'sphere',position = (5, 10, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball11 = Entity(model = 'sphere',position = (9, 10, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball12 = Entity(model = 'sphere',position = (11, 7, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball13 = Entity(model = 'sphere',position = (-9, 10, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball14 = Entity(model = 'sphere',position = (-11, 3, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball15 = Entity(model = 'sphere',position = (8, 5, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball16 = Entity(model = 'sphere',position = (2, 8, 5), scale = 0.5, color = "#eff5ee", collider= 'box')
ball17 = Entity(model = 'sphere',position = (3, 6, 5), scale = 0.5, color = "#eff5ee", collider= 'box')



def update():
    ball1.y -= time.dt * 5 
    ball2.y -= time.dt * 4
    ball3.y -= time.dt * 7
    ball4.y -= time.dt * 5
    ball5.y -= time.dt * 5
    ball6.y -= time.dt * 3
    ball7.y -= time.dt * 5
    ball8.y -= time.dt * 4
    ball9.y -= time.dt * 5
    ball10.y -= time.dt * 8
    ball11.y -= time.dt * 6
    ball12.y -= time.dt * 5
    ball13.y -= time.dt * 7
    ball14.y -= time.dt * 3
    ball15.y -= time.dt * 5
    ball16.y -= time.dt * 7
    ball17.y -= time.dt * 6
    if ball1.intersects(cube).hit: ball1.y = 10
    if ball2.intersects(cube).hit:ball2.y = 9
    if ball3.intersects(cube).hit:ball3.y = 8
    if ball4.intersects(cube).hit:ball4.y = 10
    if ball5.intersects(cube).hit:ball5.y = 5
    if ball6.intersects(cube).hit:ball6.y = 10
    if ball7.intersects(cube).hit:ball7.y = 7
    if ball8.intersects(cube).hit:ball8.y = 10
    if ball9.intersects(cube).hit:ball9.y = 6
    if ball10.intersects(cube).hit:ball10.y = 4
    if ball11.intersects(cube).hit:ball11.y = 8
    if ball12.intersects(cube).hit:ball12.y = 7
    if ball13.intersects(cube).hit:ball13.y = 10
    if ball14.intersects(cube).hit:ball14.y = 9
    if ball15.intersects(cube).hit:ball15.y = 10
    if ball16.intersects(cube).hit:ball16.y = 5
    if ball17.intersects(cube).hit:ball17.y = 7




    
app.run()

