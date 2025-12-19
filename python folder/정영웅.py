import pygame
import random
from PIL import Image, ImageDraw, ImageFilter
import os


def create_sword_texture(level):
    img = Image.new("RGBA", (128, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

 
    blade_color = (200, 200, 200)

    if level < 1:
        blade_color = (180, 180, 180)
    elif level < 5:
        blade_color = (210, 210, 220)
    elif level < 10:
        blade_color = (120, 170, 255)  
    elif level < 13:
        blade_color = (180, 130, 255)  
    elif level < 15:
        blade_color = (255, 220, 90)   
    else:
        blade_color = (255, 70, 70)    

    
    draw.rectangle((50, 20, 78, 220), fill=blade_color)

    
    draw.rectangle((44, 220, 84, 255), fill=(80, 50, 20))

    
    draw.rectangle((35, 210, 93, 220), fill=(150, 150, 150))

    
    if level >= 5:
        glow = Image.new("RGBA", (128, 256), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        aura_color = blade_color + (120,)
        g.ellipse((10, 0, 118, 256), fill=aura_color)
        glow = glow.filter(ImageFilter.GaussianBlur(15))
        img = Image.alpha_composite(glow, img)

   
    if level >= 10:
        lightning = Image.new("RGBA", (128, 256), (0, 0, 0, 0))
        g = ImageDraw.Draw(lightning)
        x, y = 50, 30
        for i in range(4):
            g.line((x, y, x + 20, y + 40), fill=(255, 255, 255, 200), width=2)
            x += random.randint(-20, 20)
            y += 40
        lightning = lightning.filter(ImageFilter.GaussianBlur(2))
        img = Image.alpha_composite(img, lightning)

    img.save(f"sword_textures/sword_{level}.png")



os.makedirs("sword_textures", exist_ok=True)
for lv in range(16):
    create_sword_texture(lv)



pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("검 강화 RPG")


WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (150, 150, 150)
ORANGE = (255, 140, 0)
RED = (200, 0, 0)
BLUE = (70, 130, 255)
GREEN = (100, 255, 100)
GOLD = (255, 215, 0)


FONT_BIG = pygame.font.SysFont("malgungothic", 40)
FONT_MED = pygame.font.SysFont("malgungothic", 25)
FONT_SMALL = pygame.font.SysFont("malgungothic", 18)


level = 0
gold = 100000
success_rate = 60


game_started = False
message = ""


class Button:
    def __init__(self, rect, color, text, text_color=WHITE):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)
        txt = FONT_MED.render(self.text, True, self.text_color)
        txt_rect = txt.get_rect(center=self.rect.center)
        surf.blit(txt, txt_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



btn_upgrade = Button((SCREEN_WIDTH//4 - 75, SCREEN_HEIGHT - 80, 150, 50), ORANGE, "강화하기")
btn_sell = Button((SCREEN_WIDTH*3//4 - 75, SCREEN_HEIGHT - 80, 150, 50), RED, "판매하기")
btn_start = Button((SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT//2 + 50, 150, 50), BLUE, "게임 시작")


def load_sword_texture(lv):
    path = f"sword_textures/sword_{lv}.png"
    return pygame.image.load(path).convert_alpha()

sword_texture = load_sword_texture(level)


def draw_success_gauge(surf, rate, pos, size):

    pygame.draw.rect(surf, GRAY, (*pos, size[0], size[1]), border_radius=8)
    inner_height = int(size[1] * rate / 100)

    pygame.draw.rect(surf, GREEN, (pos[0], pos[1] + size[1] - inner_height, size[0], inner_height), border_radius=8)
 
    text = FONT_SMALL.render(f"성공 확률: {rate}%", True, WHITE)
    surf.blit(text, (pos[0] + size[0] + 10, pos[1] + size[1]//2 - text.get_height()//2))



def draw_game_ui():
    screen.fill((20, 20, 30))  

  
    title = FONT_BIG.render(" 검 강화 RPG ", True, GOLD)
    screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))

    
    sword_rect = sword_texture.get_rect(center=(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 - 20))
    screen.blit(sword_texture, sword_rect)

  
    level_text = FONT_MED.render(f"강화 단계: +{level}", True, WHITE)
    gold_text = FONT_MED.render(f"골드: {gold}", True, WHITE)
    screen.blit(level_text, (20, 80))
    screen.blit(gold_text, (20, 120))

    
    gauge_pos = (sword_rect.right + 20, sword_rect.top + 50)
    draw_success_gauge(screen, success_rate, gauge_pos, (25, 150))

   
    btn_upgrade.draw(screen)
    btn_sell.draw(screen)

  
    if message:
        msg_color = GREEN if "성공" in message else RED
        msg_surf = FONT_MED.render(message, True, msg_color)
        screen.blit(msg_surf, (SCREEN_WIDTH//2 - msg_surf.get_width()//2, SCREEN_HEIGHT - 110))



def draw_start_screen():
    screen.fill((10, 10, 40))  
  
    title = FONT_BIG.render("⚔ 검 강화 RPG ⚔", True, BLUE)
    screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//3))

 
    btn_start.draw(screen)



def try_upgrade():
    global level, gold, success_rate, sword_texture, message

   
    cost = 5000 + level * 3000
    if gold < cost:
        message = "검을 강화할 돈이 부족해...."
        return

    gold -= cost

   
    base_rate = max(10, 100 - level * 10)
    success = random.randint(1, 100) <= base_rate

    if success:
        if level < 15:
            level += 1
        message = f"검이 더욱 강해졌다 +{level}"
    else:
        message = "검이 부서졌다..."

  
    sword_texture = load_sword_texture(level)

  
    success_rate = max(5, 100 - level * 7)



running = True
while running:
    if not game_started:
        draw_start_screen()
    else:
        draw_game_ui()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if btn_start.is_clicked(event.pos):
                    game_started = True
                    message = ""
            else:
                if btn_upgrade.is_clicked(event.pos):
                    try_upgrade()
                elif btn_sell.is_clicked(event.pos):
                    message = f"검을 대장장이에게 넘겼다! 골드 +{level * 40000}"
                    gold += level * 40000
                    level = 0
                    sword_texture = load_sword_texture(level)
                    success_rate = 60

pygame.quit()
