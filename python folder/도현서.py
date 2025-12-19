from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.
import random as ran




app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()



cube = Entity(model = 'cube', scale = (5,20,3.9), position = (0,0,0), color = "#7f4c1f", texture = 'brick')

cube = Entity(model = 'cube', scale = (7,20,3), position = (0,0,0), color = "#8d8883")
cube = Entity(model = 'cube', scale = (7,20,3), position = (0,0,0), color = "#8d8883")
cube = Entity(model = 'cube', scale = (1,20,5), position = (4,0,0), color = "#000000")
cube = Entity(model = 'cube', scale = (1,20,5), position = (-4,0,0), color = "#000000")


sphere1 = Entity(model = 'sphere', scale = (2.5, 2.5,2.5), position = (-0,-8.5,-3.25), color = "#0946c9", collider='box')
sphere2 = Entity(model = 'sphere', scale = (1, 1, 2), position = (0,6,-3), color = "#ffffff", collider='box')
sphere3 = Entity(model = 'sphere', scale = (1, 1, 2), position = (-0.5,7,-3), color = "#ffffff", collider='box')
sphere4 = Entity(model = 'sphere', scale = (1, 1, 2), position = (0.5,7,-3), color = "#ffffff", collider='box')
sphere5 = Entity(model = 'sphere', scale = (1, 1, 2), position = (1,8,-3), color = "#ffffff", collider='box')
sphere6 = Entity(model = 'sphere', scale = (1, 1, 2), position = (0,8,-3), color = "#ffffff", collider='box')
sphere7 = Entity(model = 'sphere', scale = (1, 1, 2), position = (-1,8,-3), color = "#ffffff", collider='box')
sphere8 = Entity(model = 'sphere', scale = (1, 1, 2), position = (1.5,9,-3), color = "#ffffff", collider='box')
sphere9 = Entity(model = 'sphere', scale = (1, 1, 2), position = (-0.5,9,-3), color = "#ffffff", collider='box')
sphere10 = Entity(model = 'sphere', scale = (1, 1, 2), position = (0.5,9,-3), color = "#ffffff", collider='box')
sphere11 = Entity(model = 'sphere', scale = (1, 1, 2), position = (-1.5,9,-3), color = "#ffffff", collider='box')




def update():
   sphere1.y += 0.1
   if sphere2.intersects(sphere1).hit:
       sphere2.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('1번핀 충돌!')
   else:
    print('1번핀 충돌안하는중')
   if sphere3.intersects(sphere1).hit:
       sphere3.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('2번핀 충돌안하는중')
   else:
    print('2번핀 충돌안하는중')    
   if sphere4.intersects(sphere1).hit:
       sphere4.position += Vec3(ran.uniform(0,2),ran.uniform(0,0))
       print('3번핀 충돌안하는중')
   else:
    print('3번핀 충돌안하는중')    
   if sphere5.intersects(sphere1).hit:
       sphere5.position += Vec3(ran.uniform(0,5),ran.uniform(0,0))
       print('4번핀 충돌!')
   else:
    print('4번핀 충돌안하는중')    
   if sphere6.intersects(sphere1).hit:
       sphere6.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('5번핀 충돌!')
   else:
    print('5번핀 충돌안하는중')       
   if sphere7.intersects(sphere1).hit:
       sphere7.position += Vec3(ran.uniform(0,5),ran.uniform(0,0))
       print('6번핀 충돌!')
   else:
    print('6번핀 충돌안하는중')    
   if sphere8.intersects(sphere1).hit:
       sphere8.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('7번핀 충돌!')
   else:
    print('7번핀 충돌안하는중')      
   if sphere9.intersects(sphere1).hit:
       sphere9.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('8번핀 충돌!')
   else:
    print('8번핀 충돌안하는중')      
   if sphere10.intersects(sphere1).hit:
       sphere10.position += Vec3(ran.uniform(0,4),ran.uniform(0,0))
       print('9번핀 충돌!')    
   else:
    print('9번핀 충돌안하는중')      
   if sphere11.intersects(sphere1).hit:
       sphere11.position += Vec3(ran.uniform(0,3),ran.uniform(0,0))
       print('10번핀 충돌!')
   else:
    print('10번핀 충돌안하는중')      





app.run()