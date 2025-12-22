from ursina import *
import random
#임찬오
app = Ursina()

class Mycamera(EditorCamera):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rotation = (90,0,0)
Mycamera(position = (5.5,17,6))

list_1 = [color.red, color.yellow, color.green]

def generate_board():
    return [[random.choice(list_1) for _ in range(5)] for _ in range(5)]

list_2 = generate_board()


win_text = Text(text="win!", position=(-0.74, 0.1), scale=2, color=color.white, visible=False)
restart_text = Text(text = 'Press R to Restart!',position=(-0.89, 0), scale=2, color=color.white, visible=False)

def check_victory():
    for row in list_2:
        if len(set(row)) == 1:
            win_text.visible = True
            restart_text.visible = True
            return True

    for col_idx in range(len(list_2[0])):
        column = [row[col_idx] for row in list_2]
        if len(set(column)) == 1:
            win_text.visible = True
            restart_text.visible = True
            return True

    return False

def create_board():
    global board_entities
    board_entities = []
    for i in range(len(list_2)):
        for j in range(len(list_2[i])):
            block = Entity(
                model='cube',
                color=list_2[i][j],
                scale=2,
                position=(i * 3, 0, j * 3),
                collider='box',
                texture = 'white_cube'
            )
            board_entities.append(block)
board_panel = Entity(model = 'quad',scale = 15, color="#000000", position = (6,0,6), double_sided=True, rotation=(90, 0, 0))
create_board()

def update():
    if check_victory():
        win_text.visible = True
        restart_text.visible = True

def input(key):
    if key == 'escape':
        application.quit()

    if key == 'r':
        restart_game()

def restart_game():
    global list_2, board_entities

    for block in board_entities:
        destroy(block)

    list_2 = generate_board()

    create_board()

    win_text.visible = False
    restart_text.visible = False

    print("게임이 새로 시작되었습니다!")

app.run()