from ursina import *
app = Ursina()
EditorCamera()

lst = [
 '수행1.jpg', '수행2.jpg', '수행3.jpg', '수행4.jpg', '수행5.jpg',
 '수행6.jpg', '수행7.jpg', '수행8.jpg', '수행9.jpg', '수행10.jpg',
 '수행11.jpg', '수행12.jpg', '수행13.jpg', '수행14.jpg', '수행15.jpg',
 '수행16.jpg', '수행17.jpg', '수행18.jpg', '수행19.jpg', '수행20.jpg',
 '수행21.jpg', '수행22.jpg', '수행23.jpg', '수행24.jpg', '수행25.jpg',
 '수행26.jpg', '수행27.jpg', '수행28.jpg', '수행29.jpg', '수행30.jpg',
 '수행31.jpg', '수행32.jpg', '수행33.jpg', '수행34.jpg', '수행35.jpg'
]


i = 0

def input(key):
    global i
    if key == 'escape':
        application.quit()
    if key == 'left mouse down':  # 마우스 왼쪽 버튼 눌렀을 때
        if mouse.hovered_entity == a: # 만약 마우스가 큐브 위에 있다면<< 이 부분이 필요하겠죠? 없으면 마우스 위치랑 관계없이 동작할테니
            i += 1
            print(f'i값 {i}')
            china.texture = lst[i]
            a.color = color.random_color()  # 큐브의 색상을 랜덤으로 변경
        if mouse.hovered_entity == b: # 만약 마우스가 큐브 위에 있다면<< 이 부분이 필요하겠죠? 없으면 마우스 위치랑 관계없이 동작할테니
            b.color = color.random_color()  # 큐브의 색상을 랜덤으로 변경
            i -= 1
            china.texture = lst[i]
        if i >= 34:
            
            i = 0
      
            

china = Entity(
     model='plane',
     texture = lst[i],  ##lst[i]
     scale=1000,
     position=(0,0,0),
     rotation = (0,270,0)
)


a = Entity(
     model = 'cube',
     texture = 'arrow_right',
     position = (0,-250,700),
     scale = 500,
     rotation = (90,180,90),
     collider = 'box'
)

b = Entity(
     model = 'cube',
     texture = 'arrow_right',
     position = (0,-250,-700),
     scale = 500,
     rotation = (0,-90,180),
     collider = 'box'
)


         

app.run()
