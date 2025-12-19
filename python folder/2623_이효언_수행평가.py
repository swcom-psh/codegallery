from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.
'''1.효소의 기질 특이성 이거로 해야지





'''
app = Ursina()
EditorCamera()
window.color = color.rgb(172, 157, 131)
def input(key):
    if key == 'escape':
        application.quit()


#효소모양
E = Entity(model = 'cube',position = (0, 0, 0), scale = 5, texture ='assets\효소2.png')
N = Entity(model = 'cube',position = (-5, 0, 0), scale = 5,texture ='assets\효소2.png')
Z = Entity(model = 'cube',position = (-10, 0, 0), scale = 5,texture ='assets\효소2.png')
Y = Entity(model = 'cube',position = (-10, 5, 0), scale = 5,collider='box',texture ='assets\효소2.png')
M = Entity(model = 'cube',position = (-10, 10, 0), scale = 5,collider='box',texture ='assets\효소2.png')
E1 = Entity(model = 'cube',position = (-5, 10, 0), scale = 5,collider='box',texture ='assets\효소2.png')
 
#기질A 모양
cube1 = Entity(model = 'cube',position = (15, 5, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')
cube2 = Entity(model = 'cube',position = (10, 5, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')
cube3 = Entity(model = 'cube',position = (15, 10, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')

#효소2모양
E2 = Entity(model = 'cube',position = (0, -20, 0), scale = 5, texture ='assets\효소2.png')
N2 = Entity(model = 'cube',position = (-5, -20, 0), scale = 5,texture ='assets\효소2.png')
Z2 = Entity(model = 'cube',position = (-10, -20, 0), scale = 5,texture ='assets\효소2.png')
Y2 = Entity(model = 'cube',position = (-10, -15, 0), scale = 5,collider='sphere',texture ='assets\효소2.png')
M2 = Entity(model = 'cube',position = (-10, -10, 0), scale = 5,collider='sphere',texture ='assets\효소2.png')
E3 = Entity(model = 'cube',position = (-5, -10, 0), scale = 5,collider='sphere',texture ='assets\효소2.png')

#기질B 모양
cube4 = Entity(model = 'sphere',position = (15, -15, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')
cube5 = Entity(model = 'sphere',position = (10, -15, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')
cube6 = Entity(model = 'sphere',position = (15, -10, 0), scale = 5, color = "#df99d0",texture ='assets\효소3.png',collider='box')

#기질B가 효소2와 반응하지 않고 돌아오는 것을 구현하기 위한 물체, .alpha를 사용해서 투명도를 0으로 만들었다.
cube_sphere = Entity(model = 'sphere',scale = 5, position = (10,-15,0),collider = 'box',alpha = 0)

#배경: 세포 속을 표현하기 위해 사용, 사진을 삽입했다.
album = Entity(model = 'plane', scale = (200,0,200),position = (0, 10, 10), rotation = (270,0,0), texture = 'assets\세포속.png')

#효소가 결함에 성공하거나 실패했을 때를 알려주는 것을 구현하기 위한 텍스트 객체 설정. 처음에는 글자가 보이면 안되기 때문에 안보이게 함
#선생님이 만든 미로게임에 있던 .visible을 참고함 

enzyme = Text(text='Success', position=(.2, .3), scale=1.7 , color=color.yellow,font = 'assets/강원교육튼튼.ttf' )
enzyme1 = Text(text='Failure', position=(.2, -.1), scale=1.7, color=color.yellow,font = 'assets/강원교육튼튼.ttf')
enzyme.visible = False
enzyme1.visible = False

#기질A와 기질B가 효소와 결합할 때의 반응을 각각 구현
#기질A는 효소와 충돌한다면 결합되었다는 것을 보여주기 위해 색깔을 바꾸었고, 충돌하지 않았을 때는 계속 이동했다.
#기질B는 효소와 충돌한다면 결합되지 않음을 보여주기 위해 다시 자리로 돌아가는 것으로 구현했다. 또 충돌하지 않았을 때는 계속 이동했다.
#위에 있는 성공하거나 실패했다는 것을 알려주는 코드를 실행하기 위해, 위에서 설정했던 cube_sphere이 물체와 충돌했을 때 돌아오게 함과 동시에 글자를 나타나게 함
def update(): 
                
    if cube2.intersects(Y).hit:
        cube2.color = color.hex("#84e6b0")
    else:
        cube2.x -= time.dt * 5  

    if cube1.intersects(E1).hit:
        cube1.color = color.hex("#84e6b0")
    else:
        cube1.x -= time.dt * 5  

    if cube3.intersects(E1).hit:
        cube3.color = color.hex('#84e6b0') 
    else:
        cube3.x -= time.dt * 5  

    if cube_sphere.intersects(Y2).hit:
        cube4.x = 20
        cube5.x = 15
        cube6.x = 20
        enzyme.visible = True
        enzyme1.visible = True
    else:
        cube_sphere.x -= time.dt * 5
       
    
    if cube5.intersects(Y2).hit:
        pass
    else:
        cube5.x -= time.dt * 5  

    if cube4.intersects(E3).hit:
        pass
    else:
        cube4.x -= time.dt * 5  

    if cube6.intersects(E3).hit:
        pass
    else:
        cube6.x -= time.dt * 5  




app.run()
