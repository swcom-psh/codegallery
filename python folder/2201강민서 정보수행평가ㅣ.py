from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

ground = Entity(model='plane', texture='grass', scale=(100,0,100), collider='box')
player = FirstPersonController(model='cube', origin_y=-.5, color=color.orange)

pickup = Entity(model='sphere', position=(1,0,0))
speed = 0
max_distance = 10
start_position = Vec3(0,0,0)
moving = False
direction = Vec3(0,0,0)

def input(key):
    global start_position  #전역변수
    global moving
    global direction
   
    if key == 'escape':
        application.quit()
   
    #if key == 'q' and not moving:
        # 이동 시작
        #speed = 3
      #  start_position = pickup.position
       # direction = (player.forward).normalized()
 
       
    if key == 'q':
       
        if abs(player.x - pickup.x) < 5 or abs(player.z - pickup.z)<5:
            pickup.speed = 10                
            #start_position= pickup.position
            direction = (player.forward).normalized()
            moving = True
           
           


        #if distance(pickup, player) > 1:
         #   if distance(pickup, player) < 3 :            
               # pickup.speed = 10                
                #pickup.position = start_position
                #direction = (player.forward).normalized()
                #moving = True
       
           
           
       
       

def update():
    a = player.position - pickup.position
    print(f'a값 {a}')
    global speed, moving, start_position, direction
   
    # 플레이어 이동
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1
    player.z += held_keys['w'] * 0.1
    player.z -= held_keys['s'] * 0.1
   
    # pickup 이동
    if moving:
        pickup.position += direction * speed * time.dt
       
        # 최대 거리 도달 시 멈춤
        if distance(pickup.position, start_position) >= max_distance:
            moving = False
            speed = 0
    
    if distance(pickup, player) < 1:
        speed = 3
        start_position = pickup.position
        direction = (player.forward).normalized()
       
        moving = True



   






app.run()