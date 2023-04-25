import pygame

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 900
WIN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Gorilla Game")
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 55, 55

ALMA_IMAGE = pygame.image.load('Alma.webp')
ALMA_FITTED = pygame.transform.scale(ALMA_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
FANNY_IMAGE = pygame.image.load('Fanny.webp')
FANNY_FITTED = pygame.transform.scale(FANNY_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

DROP_SPEED = 1.5
BULLET_SPEED = 2
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

def handleBullets(bullet, fanny, alma, isAlmaTurn):
    if isAlmaTurn:
        if bullet == None:
            return None
        if bullet.x > alma.x + alma.width:
            bullet.x -= BULLET_SPEED
            print("Fanny",bullet.x)
        elif bullet.x <= alma.x + alma.width:
            bullet.x = alma.x + alma.width - 50 - WINDOW_WIDTH
    else:
        if bullet == None:
            return None
        if bullet.x < fanny.x:
            bullet.x += BULLET_SPEED
            print("Alma",bullet.x)
        elif bullet.x >= fanny.x:
            bullet.x = fanny.x + 50 + WINDOW_WIDTH
        
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
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not intro and isAlmaTurn:
                    bullet = pygame.Rect(alma.x + alma.width//2, alma.y + alma.height//2, 5, 5)
                    isAlmaTurn = False
                elif event.key == pygame.K_SPACE and not intro and not isAlmaTurn:
                    bullet = pygame.Rect(fanny.x + fanny.width//2, fanny.y + fanny.height//2, 5, 5)
                    isAlmaTurn = True

                    
        if isAlmaTurn and not intro:
            mousePosition = pygame.mouse.get_pos()
            pygame.draw.line(WIN, 'Gold',(0,0), (WINDOW_WIDTH, WINDOW_HEIGHT))
            #pygame.display.update()
        elif not isAlmaTurn and not intro:
            pass


        if intro:
            intro = playersIntro(alma,fanny)
        
        if not intro:
            handleBullets(bullet, fanny, alma, isAlmaTurn)
            pass
        
        draw_window(alma, fanny, bullet, isAlmaTurn)
        
    pygame.quit()

if __name__ == "__main__":
    main()
