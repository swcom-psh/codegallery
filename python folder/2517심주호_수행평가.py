from ursina import * #우르시나 라이브러리의 모든 기능(=*)을 가져온다.
from ursina.prefabs.first_person_controller import FirstPersonController



app =  Ursina()
EditorCamera()
#player = FirstPersonController()
camera.position = (0, 245, 0)
camera.rotation_x = 90


def input(key):
    if key == 'escape':
        application.quit()




cube = Entity(model = 'cube' , position = (85, 0, 0), scale = (5,5,40), color = color.gold) 


cube7 = Entity(model = 'cube' , position = (-85, 0, 0), scale = (5,5,40), color = color.gold)




cube13 = Entity(model = 'cube' , position = (0, 0, -45), scale = (170,4,4), color = color.gray)
cube14 = Entity(model = 'cube' , position = (0, 0, 45), scale = (170,4,4), color = color.gray)

cube15 = Entity(model = 'cube' , position = (-85, 0, 30), scale = (4,4,30), color = color.gray)
cube16 = Entity(model = 'cube' , position = (85, 0, 30), scale = (4,4,30), color = color.gray)
cube17 = Entity(model = 'cube' , position = (85, 0, -27), scale = (4,4,33), color = color.gray)
cube18 = Entity(model = 'cube' , position = (-85, 0, -27), scale = (4,4,33), color = color.gray)




ground = Entity(model = 'plane', scale = (180,0,100), collider = 'box', position= (0, 0, 0), texture= 'textures/textures\잔디.jpg')


class Player(Entity):
    def __init__(self, control_key, start_x, start_z, color_type):
        super().__init__(
            model='cube',                
            color=color_type,            
            scale=(6, 6, 6),            
            position=(start_x, 3, start_z), 
            collider='box'               
        )
        self.control_key = control_key     
        self.speed = 30                   
        
        
        if self.control_key == 'WASD':
            self.keys = ['w', 's', 'a', 'd']
        else: 
            self.keys = ['up arrow', 'down arrow', 'left arrow', 'right arrow']

    def update(self):
        self.x += held_keys[self.keys[3]] * time.dt * self.speed
        self.x -= held_keys[self.keys[2]] * time.dt * self.speed 
        self.z += held_keys[self.keys[0]] * time.dt * self.speed 
        self.z -= held_keys[self.keys[1]] * time.dt * self.speed 
        
       
        boundary = 85
        
        if self.x > boundary: self.x = boundary
        if self.x < -boundary: self.x = -boundary
        if self.z > boundary: self.z = boundary
        if self.z < -boundary: self.z = -boundary

start_pos_offset = 35 

# Player 1 파랑이 (WASD)
player1 = Player(
    control_key='WASD',
    start_x=-50,
    start_z=0, # 아래쪽 시작
    color_type=color.blue
)
# player 2 붉은이 (방향키)
player2 = Player(
    control_key='ARROW',
    start_x=50,
    start_z=0,  # 위쪽 시작
    color_type=color.red
)

ball = Entity(
    model = 'sphere',
    position = (0, 1, 0),
    scale = 3,
    color = "#c50ff3ff",
    collider= 'box'


)


def update():
    if ball.intersects(player1).hit:
        ball.position = player1.position + Vec3(5,0,0)
        if held_keys['f']:
            for i in range(50):
                ball.x += 3 *time.dt

    if ball.intersects(player2).hit:
        ball.position = player2.position + Vec3(-5,0,0)
        if held_keys['k']:
            for i in range(50):
                ball.x += 3 *time.dt













       

def input(key):
    if key == 'escape':
        application.quit()



app.run()

