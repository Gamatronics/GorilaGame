import pygame
import math
pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 900
WIN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Gorilla Game")
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

FPS = 60
PUTA_MADRE = pygame.mixer.Sound("audio alma.mp3")
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 55

ALMA_IMAGE = pygame.image.load('Alma.webp')
ALMA_FITTED = pygame.transform.scale(ALMA_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
FANNY_IMAGE = pygame.image.load('Fanny.webp')
FANNY_FITTED = pygame.transform.scale(FANNY_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

DROP_SPEED = 1.5
BULLET_SPEED = 2
NORMALIZER_X = 0.02
NORMALIZER_Y = 0.15
gravity = 9.81
#FLOOR_SIZE = [(0,300),(200, 300),(200,500),(0,500)]
#FLOOR = pygame.draw.polygon(WIN, GREEN,((0,300),(200, 300),(200,500),(0,500)))

FLOOR = pygame.Rect(0, 300, WINDOW_WIDTH, WINDOW_HEIGHT - 300)

#This will be used for random generation of the different floor levels (if needed)
#We might not even need a class
class Floors:
    def __init__(self, originx, originy, width, height): 
        self.height = height
        self.width = width
        self.originx = originx
        self.originy = originy
    
    def createRect(self):
        floor = pygame.Rect(self.originx, self.originy, self.width, self.height)
        return floor

#Instantiation example
#FLOOR1 = Floors(0, 300, 100, 200).createRect()



def draw_window(alma, fanny, bullet, isAlmaTurn):
    WIN.fill(WHITE)
    WIN.blit(ALMA_FITTED, (alma.x, alma.y))
    WIN.blit(FANNY_FITTED, (fanny.x, fanny.y))
    #pygame.draw.polygon(WIN, GREEN,((0,300),(200, 300),(200,500),(0,500)))
    if bullet != None:
        pygame.draw.rect(WIN, BLACK, bullet)
    pygame.draw.rect(WIN, GREEN, FLOOR)
    if isAlmaTurn and not intro:
        pygame.draw.line(WIN, 'Black',(alma.x+alma.width//2,alma.y+alma.height//2), pygame.mouse.get_pos())
    elif not isAlmaTurn and not intro:
        pygame.draw.line(WIN, 'Black',(fanny.x+fanny.width//2,fanny.y+fanny.height//2), pygame.mouse.get_pos())
    pygame.display.update()

def playersIntro(alma, fanny):
    flag = False
    if alma.y + PLAYER_HEIGHT < FLOOR.y:
        alma.y += DROP_SPEED
        flag = True
    if fanny.y + PLAYER_HEIGHT < FLOOR.y:
        fanny.y += DROP_SPEED
        flag = True
    if flag:
        return True
    else:
        return False

def handleBullets(bullet, fanny, alma, isAlmaTurn, mouse_pos):
    global gravity
    if isAlmaTurn:
        if bullet == None:
            return None
        Vx = ((fanny.x + fanny.width//2) - mouse_pos[0])*NORMALIZER_X
        Vy = ((fanny.y + fanny.height//2) - mouse_pos[1])*NORMALIZER_Y
        angle = math.degrees(math.atan(Vy/Vx))
        bullet.x = bullet.x - Vx
        gravity += 1
        bullet.y = bullet.y - Vy + gravity
        if bullet.y > fanny.y + fanny.height or bullet.y < -100:
            gravity = 0
            bullet.y = WINDOW_HEIGHT + 50
        if bullet.x + bullet.width > alma.x and bullet.x + bullet.width < alma.width + alma.x and bullet.y + bullet.height > alma.y and bullet.y + bullet.height < alma.y + alma.height:
            pygame.mixer.Sound.play(PUTA_MADRE)
    else:
        if bullet == None:
            return None
        Vx = (mouse_pos[0] - (alma.x + alma.width//2))*NORMALIZER_X
        Vy = ((alma.y + alma.height//2) - mouse_pos[1])*NORMALIZER_Y
        angle = math.degrees(math.atan(Vy/Vx))
        bullet.x = bullet.x + Vx
        gravity += 1
        bullet.y = bullet.y - Vy + gravity
        if bullet.y > alma.y + alma.height or bullet.y < -100:
            gravity = 0
            bullet.y = WINDOW_HEIGHT + 50
        if bullet.x + bullet.width > fanny.x and bullet.x + bullet.width < fanny.width + fanny.x and bullet.y + bullet.height > fanny.y and bullet.y + bullet.height < fanny.y + fanny.height:
            pygame.mixer.Sound.play(PUTA_MADRE)
        
##PENDING HOW TO GET RID OF BULLET WHEN COLLIDING

def main():
    alma = pygame.Rect(200, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    fanny = pygame.Rect(600, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    global intro
    intro = True
    bullet = None
    isAlmaTurn = True
    mouse_pos = (0,0)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not intro and isAlmaTurn:
                mouse_pos = pygame.mouse.get_pos()
                bullet = pygame.Rect(alma.x + alma.width//2, alma.y + alma.height//2, 5, 5)
                isAlmaTurn = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not intro and not isAlmaTurn:
                mouse_pos = pygame.mouse.get_pos()
                bullet = pygame.Rect(fanny.x + fanny.width//2, fanny.y + fanny.height//2, 5, 5)
                isAlmaTurn = True

                    
        if isAlmaTurn and not intro:
           pass
        elif not isAlmaTurn and not intro:
            pass


        if intro:
            intro = playersIntro(alma,fanny)
        
        if not intro:
            handleBullets(bullet, fanny, alma, isAlmaTurn, mouse_pos)
            pass
        
        draw_window(alma, fanny, bullet, isAlmaTurn)
        
    pygame.quit()

if __name__ == "__main__":
    main()
