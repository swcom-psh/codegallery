from ursina import * 
app = Ursina() 
EditorCamera() 

# --- 엔티티(객체) 정의 ---
cube = Entity() 
cube2 = Entity() 
cube3 = Entity() 
cube4 = Entity() 
cube5 = Entity()        
camera.fov = 100
camera.position = (18,-8,0)

# --- [변경됨] 한글 변수 초기화 ---
수직 = 0       # 기존 vy
중력 = -1       # 기존 g
타이머 = 0        # 점선 효과를 위해 시간을 잴 변수

# 위치 설정 (기존과 동일)
#cube3.y -= 10 
#cube4.y -= 10 
cube3.x += 20
cube4.x += 20
cube2.y -= 15
cube5.x += 20
cube5.y -= 15
선 = Entity(
    model=Mesh(   
        vertices=[(0,0,0), (18,0,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(0,-15,0), (18,-15,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(0,4,0), (0,-4,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(0,-11,0), (0,-19,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(20,0,0), (38,0,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(20,4,0), (20     ,-4,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(20,-15,0), (38,-15,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)

선 = Entity(
    model=Mesh(   
        vertices=[(20,-11,0), (20,-19,0)], # [(시작점 x,y,z), (끝점 x,y,z)]
        mode='line',    # 선 모드로 설정
        thickness=2     # 선의 두께 (원하는 대로 조절 가능)
    ),
    color=color.white     # 선 색상
)



# --- 업데이트 함수 정의 ---
def update():
   
   
    # 함수 밖의 한글 변수를 수정하기 위해 global로 가져옵니다.
    global 수직, 타이머 


    # --- 1. 수평 이동 ---
    cube.x += 0.3 * time.dt
    cube2.x += 0.3 * time.dt
    cube3.x += 0.3 * time.dt
    cube4.x += 0.3 * time.dt
    cube5.x += 0.3 * time.dt

    # --- 2. 물리 계산 (한글 변수 사용) ---
    # 수직속도에 중력을 더해줍니다.
    

    # 스페이스바를 누르면 수직속도를 높입니다.
    if held_keys['space']:
        수직 += 3 * time.dt

    # --- 3. 위치 변경 ---
    # 계산된 수직속도만큼 y위치를 바꿉니다.
    cube.y += 수직 * time.dt
    cube2.y -= 수직 * time.dt 
    cube3.y += 수직 * time.dt 
    cube4.y -= 수직 * time.dt 
    Entity(model='sphere', scale=0.1, position=cube.position, color=color.yellow, destroy_after=5)
    Entity(model='sphere', scale=0.1, position=cube2.position, color=color.yellow, destroy_after=5)
    Entity(model='sphere', scale=0.1, position=cube3.position, color=color.yellow, destroy_after=5)
    Entity(model='sphere', scale=0.1, position=cube5.position, color=color.yellow, destroy_after=5)

    if cube.y > -4: 
            # 위치를 딱 -7로 고정 (땅에 파묻히지 않게)
        수직 += 중력 * time.dt 
        
         # 떨어지는 속도를 0으로 만듦 (계속 추락하는 힘 제거)
    if cube.y < -4: 
        수직 = 0    
    # --- 4. 점선 궤적 만들기 (한글 변수 사용) ---
    타이머 += time.dt  # 타이머에 흐른 시간을 계속 더합니다.
    
    if cube.y > 4: 
        수직 = -0.1




    # 2초 주기로 반복 (1초 생성 + 1초 멈춤 = 2초)
    if 타이머 > 1: 
        타이머 = 0  # 2초가 지나면 0으로 초기화

    # 타이머가 1초보다 작을 때만(0~1초) 궤적을 생성합니다.
    if 타이머 < 0.5:
        Entity(model='sphere', scale=0.1, position=cube4.position, color=color.yellow, destroy_after=5)


# --- 실행 ---
app.run()