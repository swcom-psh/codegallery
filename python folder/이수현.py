from ursina import *
import random

app = Ursina()

# 기본 하늘과 바닥
sky = Sky()
ground = Entity(model='plane', color=color.green, scale=(100,1,100), y=-1)

# 비나 눈 입자를 저장할 리스트
particles = []

# 현재 날씨 상태
weather = 'sunny'

def create_particle():
    """비나 눈 입자 생성"""
    if weather == 'rain':
        particle = Entity(model='sphere', color=color.azure, scale=0.05, y=5, x=random.uniform(-5,5), z=random.uniform(-5,5))
    elif weather == 'snow':
        particle = Entity(model='sphere', color=color.white, scale=0.08, y=5, x=random.uniform(-5,5), z=random.uniform(-5,5))
    else:
        return
    particles.append(particle)

def update():
    # 입자 생성 (비/눈일 때만)
    if weather in ['rain', 'snow'] and random.random() < 0.1:
        create_particle()

    # 입자 이동
    for p in particles:
        p.y -= 0.05 if weather == 'rain' else 0.02
        if p.y < -1:
            destroy(p)
            particles.remove(p)

def input(key):
    global weather
    if key == '1':
        weather = 'sunny'
        sky.color = color.rgb(135, 206, 235)  # 맑은 하늘색
        print("☀️ 맑은 날씨입니다.")
    elif key == '2':
        weather = 'rain'
        sky.color = color.rgb(100, 100, 150)
        print("🌧 비가 오는 날씨입니다.")
    elif key == '3':
        weather = 'snow'
        print("❄️ 눈이 오는 날씨입니다.")

app.run()


