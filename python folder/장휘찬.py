
from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.

app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

count = 0
level = 0
max = 0
uncount = 0
class Planet(Entity):
    def __init__(self,tex, pos,rea,pro):
        super().__init__(
            model='plane',
            texture=tex,
            scale=(2, 2, 2),
            rotation = (270,0,0),
            position= pos,
            collider = 'box' #클릭을 구현하려면 반드시 충돌체가 있어야함.
        )
        self.real = rea  
        self.fake = './스크린샷 2025-11-11 085601.png' ##뒷면~1235468855
        self.progress = pro
        
        
        #invoke(self.flip, delay=3)  ## 이 코드 실행하고나서 3초 뒤에 flip 함수 실행해라~ >> 카드 다시 뒷면으로 뒤집기 3초뒤에
    
    def flip(self): #뒷면으로 바꾸는 함수
        self.texture = self.fake   
    
    def unflip(self):
         self.texture = self.real 

    def portro(self):
        self.texture = self.progress

    




    def on_click(self): 
        global count
        global level
        global max
        global uncount

        if level == 0:
            if count == 0:
                invoke(self.flip, delay=0.2)
                count = 1
                print(count)
            if count == 1:
                invoke(self.unflip, delay=0.4)
                count = 2
                print(count)
        
            if count == 2:
                invoke(self.flip, delay=0.6)
                count = 3
                print(count)
            if count == 3:
                invoke(self.unflip, delay=0.8)
                count = 4
                print(count)
        
            if count == 4:
                invoke(self.flip, delay=1)
                count = 5
                print(count)
            if count == 5:
                invoke(self.unflip, delay=1.2)
                count = 6
                print(count)
        
            if count == 6:
                invoke(self.flip, delay=1.4)
                count = 7
                print(count)
            if count == 7:
                invoke(self.unflip, delay=1.6)

                count = 0
                max = 1
                
                
                print(count)
        
        

    



        
                
        
        




    
    








야돈 = Planet(tex = './스크린샷 2025-11-06 105446.png', pos = (0,0,0), rea = '.\스크린샷 2025-11-06 105511.png',pro = '.\스크린샷 2025-11-06 105511.png')
먹고자 = Planet(tex = './스크린샷 2025-11-18 084635.png', pos = (5,0,0), rea = '.\스크린샷 2025-11-18 084711.png',pro = '.\스크린샷 2025-11-18 084711.png')
랄토스 = Planet(tex = './스크린샷 2025-11-18 091814.png', pos = (-5,0,0), rea = './스크린샷 2025-11-18 090612.png',pro = '.\스크린샷 2025-11-18 090741.png')
냐옹 = Planet(tex = './스크린샷 2025-11-25 084543.png', pos = (-5,5,0), rea = './스크린샷 2025-11-25 084612.png',pro = '.\스크린샷 2025-11-18 090741.png')
치고마 = Planet(tex = './스크린샷 2025-11-25 084444.png', pos = (0,5,0), rea = './스크린샷 2025-11-25 084500.png',pro = '.\스크린샷 2025-11-18 090741.png')
모래꿍 = Planet(tex = './스크린샷 2025-11-25 084248.png', pos = (5,5,0), rea = './스크린샷 2025-11-25 084331.png',pro = '.\스크린샷 2025-11-18 090741.png')
망나뇽 = Planet(tex = './스크린샷 2025-11-25 085452.png', pos = (-5,-5,0), rea = './스크린샷 2025-11-25 085543.png',pro = '.\스크린샷 2025-11-18 090741.png')
조로아= Planet(tex = '.\스크린샷 2025-11-25 085325.png', pos = (5,-5,0), rea = './스크린샷 2025-11-25 085349.png',pro = '.\스크린샷 2025-11-18 090741.png')
리오르= Planet(tex = './스크린샷 2025-11-25 090630.png', pos = (0,-5,0), rea = './스크린샷 2025-11-25 090655.png',pro = '.\스크린샷 2025-11-18 090741.png')
잉어킹= Planet(tex = './스크린샷 2025-11-25 090854.png', pos = (-5,10,0), rea = './스크린샷 2025-11-25 090929.png',pro = '.\스크린샷 2025-11-18 090741.png')
에레키드= Planet(tex = './스크린샷 2025-11-25 091049.png', pos = (0,10,0), rea = './스크린샷 2025-11-25 091108.png',pro = '.\스크린샷 2025-11-18 090741.png')
아켄= Planet(tex = './스크린샷 2025-11-25 091613.png', pos = (5,10,0), rea = './스크린샷 2025-11-25 091630.png',pro = '.\스크린샷 2025-11-18 090741.png')







app.run()

