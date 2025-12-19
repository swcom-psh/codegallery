from ursina import *

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


message = Text("", scale=2, position=(0, 0.2, 0))
result = Text("", scale=1.5, position=(0, 0, 0))

waiting = False
start_time = 0

def new_round():
    global waiting, start_time
    waiting = False
    message.text = "Ready.."
    

    delay = random.uniform(1,3)

    def show_click():
        global waiting, start_time
        message.text = "CLICK!"
        waiting = True
        start_time = time.time()

    invoke(show_click, delay=delay)

new_round()

def input(key):
    global waiting
    if key == "left mouse down":
        if not waiting:
            result.text = "too early!"
            invoke(new_round, delay=1.5)
        else:
            reaction = time.time() - start_time   
            print(f' 값2: {reaction}')
            result.text = f"your speed : {reaction:f} sec"  
            waiting = False
            invoke(new_round, delay=1.5)
    
    if key == "space":
        if not waiting:      
            result.text = "too early!"
            invoke(new_round, delay=1.5)
        else:
            reaction = time.time() - start_time   
            print(f' 값: {reaction}')
            result.text = f"your speed : {reaction:f} sec"  
            waiting = False
            invoke(new_round, delay=1.5)

app.run()
 