from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# === 환경 ===
ground = Entity(model='plane', color=color.green, scale=(150,1,150), collider='box', texture='assets/잔디밭.jpg')
sky = Sky()

# === 플레이어 ===
player = FirstPersonController(model='cube', color=color.azure, speed=5, mouse_sensitivity=Vec2(40,40), position=(0,2,0))
player.cursor.visible = True
player.gravity = 1
player.jump_height = 2

# === 공 ===
ball = Entity(model='sphere', color=color.orange, scale=1, position=(0,1,5), collider='sphere')
ball_velocity = Vec3(0,0,0)
gravity = -9.8

# === 골대 ===
goal = Entity(model='cube', color = "#FFFFFF", position=(0,2,30), scale=(6,4,1), collider='box')

# === 점수 ===
score = 0
score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2, color=color.white)

# === 차징 시스템 ===
charging = False
charge_power = 0
max_power = 25

# === 커브 관련 변수 ===
spin = 0            # 좌우 회전값
spin_power = lerp(8, 10, charge_power)  # 커브 강도

# === 차징 게이지 ===
charge_bar_bg = Entity(parent=camera.ui, model='quad', color=color.rgba(255,255,255,100),
                       scale=(0.4,0.05), position=(0,-0.45))
charge_bar = Entity(parent=camera.ui, model='quad', color=color.red,
                    scale=(0.0,0.04), position=(-0.2,-0.45), origin=(-0.5,0))

charge_bar.enabled = False
charge_bar_bg.enabled = False

def input(key):
    global charging, charge_power, ball_velocity, spin, score

    # 달리기
    if key == 'right mouse down':
        player.speed = 10
    if key == 'right mouse up':
        player.speed = 5

    # 공 재소환
    if key == 'b':
        ball_velocity = Vec3(0,0,0)
        ball.position = player.position + camera.forward.normalized()
        ball.spin = 0

    if key == 'escape':
        application.quit()

    # 차징 시작
    if key == 'left mouse down':
        charging = True
        charge_power = 0
        spin = 0                      # 스핀 초기화
        charge_bar.enabled = True
        charge_bar_bg.enabled = True

    # 공 차기
    if key == 'left mouse up' and charging:
        charging = False
        charge_bar.enabled = False
        charge_bar_bg.enabled = False

        hit = raycast(camera.world_position, camera.forward, distance=3, ignore=[player])
        if hit.hit and hit.entity == ball:

            power = lerp(8, max_power, charge_power)

            # 기본 슛 방향
            dir = camera.forward.normalized()

            # 공 발사
            ball_velocity = dir * power
            ball_velocity.y = power / 2.5

            # 스핀값 공에 적용 (sign: 좌우)
            ball.spin = spin   # Entity 속성 추가

            print(f"POWER={power}, SPIN={spin}")

def update():
    global ball_velocity, charge_power, score, spin

    # === 커브(마그누스 효과) 적용 ===
    if hasattr(ball, 'spin'):
        ball_velocity.x += ball.spin * spin_power * time.dt
        ball.spin *= 0.98
        if abs(ball.spin) < 0.01:
            ball.spin = 0
    
    # === 공 이동 ===
    ball_velocity.y += gravity * time.dt
    ball.position += ball_velocity * time.dt

    # 바닥 충돌
    if ball.y <= 0.5:
        ball.y = 0.5
        ball_velocity.y *= -0.4
        ball_velocity.x *= 0.9
        ball_velocity.z *= 0.9

    # 감속
    if abs(ball_velocity.x) < 0.01: ball_velocity.x = 0
    if abs(ball_velocity.z) < 0.01: ball_velocity.z = 0
    
    # === 차징 중 q/e로 커브 조절 ===
    if charging:
        charge_power = min(charge_power + time.dt * 1.2, 1)
        charge_bar.scale_x = 0.4 * charge_power
        charge_bar.color = color.yellow if charge_power < 0.7 else color.red
        charge_bar.position = (-0.2 + 0.2 * charge_power, -0.45)

        # 스핀 조절
        if held_keys['q']:
            spin -= time.dt * 2
        if held_keys['e']:
            spin += time.dt * 2

    # === 골 판정 ===
    if ball.intersects(goal).hit:
        score += 1
        score_text.text = f'Score: {score}'
        ball.position = (0,1,5)
        ball_velocity = Vec3(0,0,0)
        ball.spin = 0

app.run()
