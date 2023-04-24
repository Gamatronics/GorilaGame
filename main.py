import pygame

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 900
WIN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Gorilla Game")
WHITE = (255,255,255)
GREEN = (0,255,0)

FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 55, 55

ALMA_IMAGE = pygame.image.load('Alma.webp')
ALMA_FITTED = pygame.transform.scale(ALMA_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
FANNY_IMAGE = pygame.image.load('Fanny.webp')
FANNY_FITTED = pygame.transform.scale(FANNY_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))


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



def draw_window(alma, fanny):
    WIN.fill(WHITE)
    WIN.blit(ALMA_FITTED, (alma.x, alma.y))
    WIN.blit(FANNY_FITTED, (fanny.x, fanny.y))
    #pygame.draw.polygon(WIN, GREEN,((0,300),(200, 300),(200,500),(0,500)))
    pygame.draw.rect(WIN, GREEN, FLOOR)
    pygame.display.update()





def main():
    alma = pygame.Rect(200, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    fanny = pygame.Rect(600, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if alma.y + PLAYER_HEIGHT < FLOOR.y:
            alma.y += 1
        if fanny.y + PLAYER_HEIGHT < FLOOR.y:
            fanny.y += 1
        draw_window(alma, fanny)

    pygame.quit()

if __name__ == "__main__":
    main()
