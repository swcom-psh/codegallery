from ursina import *


app = Ursina()
EditorCamera()

class Planet(Entity): #태양
    def __init__(self, texture, pos, scale):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = pos,
            scale = scale,
            collider ='box')
        self.pivot()
    def pivot(self):
        self.pi = Entity(position = (0,0,0))
        self.parent = self.pi


ground= Entity(model='plane', #땅(식물잎)
               scale= (10,0,10), 
               position=(0,-8,0),
               texture='youjin\잎.jpg', 
               collider='box')

sun = Planet( texture= 'textures/sun.jpg',#태양
              pos = (0,5, 0),
                scale = 1)

light = Entity(parent = sun,#산소=흰색,빛=노랑색 
                model = 'sphere',
                scale = 1 ,
                position = (0,0,0),
                collider ='box', 
                color=color.yellow )

tt1=Text(text='solar energy')
tt2=Text(text='o2')
tt1.enabled=False
tt2.enabled=False

def update():
   if light.color == color.yellow:#만약 노랑색이라면 아래로!
       light.y -= 5*time.dt
       tt1.enabled=True
       tt2.enabled=False

       if light.intersects(ground).hit:#GROUND에 충돌(충돌한다 = 광합성)하면 흰색으로!
            light.color = color.white
            tt2.enabled=True
            tt1.enabled=False

   else: light.y += 5*time.dt#노랑색이 아니라면 위로!
   
   if light.y >= -1:
       light.color = color.yellow#광합성은 계속된드아ㅏㅏㅏㅏ
          
app.run()    













 #  또한 클래스는 Planet 클래스를 정의하여 태양 객체를 하나의 단위로 관리하는 데 사용되었으며,
 #  __init__에서 행성의 모델·위치·크기를 설정하고 pivot() 메서드에서 self.pi라는 중심축을 생성해 객체가 특정 축을 기준으로 관리될 수 있도록 구조화했다.
 #  이 두 요소는 프로그램의 동작 흐름과 객체 기능을 조직적으로 구성하는 데 필수적인 역할을 했다.  
     
#이 프로그램에서 사용한 주요 자료구조는 변수와 클래스 내부 인스턴스 변수이다. 
# 먼저 변수는 light.y, light.color, time.dt처럼 객체의 위치·상태·속도를 저장하고 변경하는 데 사용되었으며,
#  특히 light.y는 빛의 상하 이동을 표현하고, light.color는 노란색과 흰색을 오가며 충돌 여부에 따른 움직임 변화를 만들었다.
#  클래스 내부 인스턴스 변수는 Planet 클래스에서 중심축을 만들기 위해 사용되었는데, self.pi는 행성의 기준점을 저장하는 변수이고
#  self.parent = self.pi를 통해 태양의 위치 관리와 구조적 확장이 가능해졌다. 이 두 자료구조를 통해 객체의 상태를 저장하면서 움직임과 구조를 안정적으로 구현할 수 있었다
        
    
        
        
#  (1) 빛의 상·하 이동과 색 변화 알고리즘
#내가 직접 만든 핵심 알고리즘 중 하나는 빛(light)이 위와 아래로 반복해서 이동하면서 색이 바뀌는 과정이다.
#  update() 함수 안에서 light.color를 기준으로 이동 방향을 정했는데, 빛이 노란색일 때는 light.y -= 5*time.dt로 아래 방향으로 움직이고,
#  땅(ground)에 닿으면 light.color = color.white로 바뀐다. 반대로 흰색이 되면 light.y += 5*time.dt로 위로 이동하며, 
# 일정 높이 이상 올라가면 다시 light.color = color.yellow로 바뀌어 방향을 되돌린다. 
# 이 알고리즘을 통해 빛이 마치 광합성 과정에서 잎을 향해 내려오고 다시 위로 되돌아가는 것처럼 보이도록 만들었다. 
# 내가 직접 조건문을 이용해 색과 위치를 연결시킨 부분이 이 프로그램의 실제 작동을 결정하는 핵심 흐름이다.

#(2) Planet 클래스의 중심축(pivot) 생성 알고리즘
#두 번째 핵심 알고리즘은 태양 객체를 만들 때 사용한 Planet 클래스 내부의 pivot 알고리즘이다.
#  Planet 클래스를 정의하면서 태양이 기준점을 갖도록 self.pi = Entity(position=(0,0,0))라는 축을 만들고,
#  self.parent = self.pi로 태양의 부모를 축으로 설정했다. 이 알고리즘 덕분에 태양이 하나의 고정된 축을 기준으로 놓이게 ela





