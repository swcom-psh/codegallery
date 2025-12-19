from ursina import*         

app=Ursina()#app이라는 객체에 우르시나 월드를 불려온다.
EditorCamera()



def input(key):
    if key == 'escape':
        application.quit()
    if key == 'left mouse down':  # 마우스 왼쪽 버튼 눌렀을 때
        if mouse.hovered_entity == btn1: # 만약 마우스가 큐브 위에 있다면<< 이 부분이 필요하겠죠? 없으면 마우스 위치랑 관계없이 동작할테니
            btnnn=Planet(tex='/d.png', sc=2.5, pos=(-2.7,-1.3,0))
        if mouse.hovered_entity == btn3:
            btnnn=Planet(tex='/h.png', sc=2.5, pos=(1,-2.3,0))
        if mouse.hovered_entity == btn2:
            btnnn=Planet(tex='/gma.png', sc=2.5, pos=(4,0,0))
        if mouse.hovered_entity == btn4:
            btnnn=Planet(tex='/f.png', sc=2.5, pos=(-2.7,1.4,0))
        if mouse.hovered_entity == btn5:
            btnnn=Planet(tex='/j.png', sc=2.5, pos=(1.5,1.5,0))

class Planet(Entity):
    def __init__(self, tex, sc, pos, spin=0, orbit=0):
        super().__init__(
            model='quad',
            texture=tex,
            scale=sc,
            position=pos,
            spin=spin,
            orbit=orbit
        )
    

    
btn1 = Button(text='china', color=color.azure, scale=0.07, position=(-0.16,-0.1))
btn2 = Button(text='japan', color=color.azure, scale=0.07, parent=camera.ui, position=(0.27,-0.09))
btn3 = Button(text='korea', color=color.azure, scale=0.07, parent=camera.ui, position=(0.14,-0.06))
btn4 = Button(text='mongol', color=color.azure, scale=0.07, parent=camera.ui, position=(-0.15,0.15))
btn5 = Button(text='russia', color=color.azure, scale=0.07, parent=camera.ui, position=(-0.05,0.3))




earth=Planet(tex='./img.jpg', sc=7, pos=(0,0,5), spin=5, orbit=5)








app.run()