from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.
import random as ran
app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

arm1 = Entity(model = 'cube', scale = (3.5,1,1.2), position = (0,0,0), color = "#e79e7a")
arm2 = Entity(model = 'cube', scale = (4,1,1), position = (-3,0,0), color = "#e79e7a")
biceps1 = Entity(model = 'sphere', scale = (3,1,1), position = (0,0.5,0), color = color.red)
biceps2 = Entity(model = 'sphere', scale = (2,1,1), position = (0,0,0), color = color.red)
elbow = Entity(model = 'sphere', scale = (1,0.4,1), position = (-1.6,-0.4,0), color = "#e79e7a")
state = 0

def update():    
    global state
    if state == 0:
        arm2.rotation_z += 3 *time.dt
        arm2.y +=  0.08 * time.dt
        biceps1.y -=  0.03 * time.dt
        biceps2.y +=  0.03 * time.dt



        print(f'로테이션값 {arm2.rotation}')
        if arm2.rotation_z >= 38:
            state = 1


    elif state == 1:
        arm2.rotation_z -= 3 *time.dt
        arm2.y -=  0.08 * time.dt
        biceps1.y +=  0.03 * time.dt
        biceps2.y -=  0.03 * time.dt





app.run()