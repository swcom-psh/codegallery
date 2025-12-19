from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
#EditorCamera()


class Player(FirstPersonController):
     def __init__(self):
          super().__init__(
               speed = 10,
               scale = 1
          )           
          
          
class Exit(Entity):
     def __init__(self, x, z): # for문에서 전달한 i, j값을 Exit 클래스의 x, z 변수안에 저장
          super().__init__(
               model = 'cube',
               color = color.black90,
               position = (x * 5, 0, z * 5) , # 전달받은 i, j 값을 이용하여 좌표를 설정
               scale = (5, 5, 5)
          )
          self.player = player # 외부 플레이어의 정보를 Exit 클래스의 self.player 변수 안에 저장합니다.
     
     def update(self):
          self.playerCollision()     

     def playerCollision(self): #플레이어와 충돌을 감지하는 메서드 함수를 정의합니다.
        distance = (self.player.position - self.position).length()
        #print(distance) 
        if distance < 3: #만약 플레이어가 탈출구에 근접하면
             self.clear.visible = True 
             self.player.enabled = False 

     




def input(key):
     if key == 'escape':
          application.quit()


player = Player()



MAP =[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [1,'3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'2',1]
]





for i in range(len(MAP)):
    for j in range(len(MAP[i])):
          if MAP[i][j]:
               if MAP[i][j] == '3':
                    player.position = (i * 5, 0, j * 5)
                    continue
               if MAP[i][j] == '2':
                    exitdoor = Exit(i,j) # exitdoor 객체를 생성하고, Exit 클래스 호출하며 i, j 값 전달     
                    continue               

               wall = Entity(                
                    model = 'cube',
                    color = '#d1a432',
                    position = (i * 5, 0, j * 5),
                    scale = (5,5,5),
                    collider = 'box',
                    texture = 'brick'
                    )
              
          
          
         
Ground = Entity(
     model = 'plane',
     texture = 'sky_sunset',  #질감 종류: brick(벽돌), grass(풀밭), white_cube(하얀큐브), noise(노이즈패턴), sky_sunset(노을이지는하늘), shore(물가풍경)
     position = (50,-1,50),
     scale = (150,1,150),
     collider = 'mesh'
)


Sky(texture = "sky_sunset")

app.run()
