from ursina import *

app = Ursina()

window.color = color.gray
camera.orthographic = True
camera.fov = 1

left_paddle = Entity(scale=(1/32,6/32), x=-.75, model='quad', origin_x=.5, collider='box')
right_paddle = duplicate(left_paddle, x=left_paddle.x*-1, rotation_z=left_paddle.rotation_z+180)

floor = Entity(model='quad', y=-.5, origin_y=.5, collider='box', scale=(2,10), visible=False)
ceiling = duplicate(floor, y=.5, rotation_z=180, visible=False)
left_wall = duplicate(floor, x=-.5*window.aspect_ratio, rotation_z=90, visible=True)
right_wall = duplicate(floor, x=.5*window.aspect_ratio, rotation_z=-90, visible=True)

left_score = 0
right_score = 0
max_score = 3
game_paused = False 
collision_cooldown = .15
ball = Entity(model='circle', scale=.05, collider='box', speed=0, collision_cooldown=collision_cooldown)

score_text = Text(text=f"{left_score} : {right_score}", position=(0, .45), scale=2, origin=(0, 0))

def update():
    global left_score, right_score, game_paused

    if game_paused:
        return 

    ball.collision_cooldown -= time.dt
    ball.position += ball.right * time.dt * ball.speed
    

    left_paddle.y += (held_keys['w'] - held_keys['s']) * time.dt * 1 # held keys가 왜 있는거지?
    right_paddle.y += (held_keys['up arrow'] - held_keys['down arrow']) * time.dt * 1 # held keys가 왜 있는거지?
    

    if ball.collision_cooldown > 0:
        return

    hit_info = ball.intersects()
    if hit_info.hit:
        ball.collision_cooldown = collision_cooldown

        if hit_info.entity in (left_paddle, right_paddle):
            ball.rotation_z += 180 * (-1 if hit_info.entity == left_paddle else 1)
            ball.rotation_z -= (hit_info.entity.world_y - ball.y) * 20 * 32 * (-1 if hit_info.entity == left_paddle else 1)
            ball.speed *= 1.1

        elif hit_info.entity == right_wall:
            left_score += 1
            update_score()

        elif hit_info.entity == left_wall:
            right_score += 1
            update_score()

        particle = Entity(model='quad', position=hit_info.world_point, scale=0, texture='circle', add_to_scene_entities=False)
        particle.animate_scale(.2, .5, curve=curve.out_expo)
        particle.animate_color(color.clear, duration=.5, curve=curve.out_expo)
        destroy(particle, delay=.5)

    if ball.y > ceiling.y - ball.scale_y/2 or ball.y < floor.y + ball.scale_y/2:
        ball.rotation_z = -ball.rotation_z  

def update_score():
    global left_score, right_score, game_paused
    score_text.text = f"{left_score} : {right_score}"

    if left_score >= max_score or right_score >= max_score:
        winner_text = Text(f"{'Left' if left_score >= max_score else 'Right'} Player Wins!", y=0, scale=2, origin=(0, 0))
        ball.speed = 0
        game_paused = True 
        invoke(destroy, winner_text, delay=3)
    else:
        reset()

def reset():
    ball.position = (0, 0, 0)
    ball.rotation = (0, 0, 0)
    ball.speed = 10
    for paddle in (left_paddle, right_paddle):
        paddle.collision = True
        paddle.y = 0

info_text = Text("game start!", y=-.40)

def input(key):
    global game_paused

    if key == 'space' and not game_paused:  
        info_text.enabled = False
        reset()

app.run()
