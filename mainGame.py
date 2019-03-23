# This project use the pygame module, all pygame functions are made with the pygame page:
# http://www.pygame.org/news
from startPage import *
from pvp import *
from pve import *
from aiBot import *
bot=Bot()

def main():
    pygame.init()
    displayWidth=640
    displayHeight=360
    FPS=60
    gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))
    clock=pygame.time.Clock()
    ##initial value of pygame
    end=False
    while not end:
        fps =  clock.get_fps()
        pygame.display.set_caption('15-112 Term Project (Version: Final Version) FPS:'+str(int(fps)))
        result=startPage()
        if result[2]=='p':
            pvp(result[3:])
        if result[2]=='e':
            pve(bot,result[3:])
        
        
        
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()