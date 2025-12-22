from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.
import random as ran


app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()



def input(key):
    if key == 'escape':
        application.quit()

class DNA(Entity):
    def __init__(self,tex,sc,pos,spin,):
        super().__init__(
            model = 'dna.glb',
            scale = sc,
            position = pos,
            spin = spin
        )
        

    def update(self):
        #self는 클래스 내부에서 생성되는 변수 등을
        #클래스 자기자신 내부에서 접근하기 위함
        self.rotation_y += self.spin




#DNA나선구조 = DNA(tex = 'textures/sun.jpg', sc = 0.1 , pos = (10,0,0), spin = 1)
#DNA나선구조 = DNA(tex = 'textures/sun.jpg', sc = 0.1 , pos = (10,337.5,0), spin = 1)
#DNA나선구조 = DNA(tex = 'textures/sun.jpg', sc = 0.1 , pos = (10,-337.5,0), spin = 1)



for i in range(99):
    DNA나선구조 = DNA(tex = 'grass' ,  sc = 0.1 , pos = (10,-337.5 * i,0), spin = 1.5)
    DNA나선구조 = DNA(tex = 'grass' , sc = 0.1 , pos = (10,337.5 * i,0), spin = 1.5)





app.run()