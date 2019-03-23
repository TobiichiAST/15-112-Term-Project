import pygame
import random
import sys
from ClassesAndHelperFunctions import *

def startPage():
    pygame.init()
    displayWidth=640
    displayHeight=360
    FPS=60
    gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))
    clock=pygame.time.Clock()
    ##pygame initials
    
    player=newPlayer([400,0])
    player.scale(0.55)  
    playerEstoc=makeEstoc(player)
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)
    playerEstocGroup=pygame.sprite.Group()
    playerEstocGroup.add(playerEstoc)
    enemyIMG=pygame.image.load('Resources/image/startPage/pveIMG.png')
    pve=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pveGroup=pygame.sprite.Group()
    pveGroup.add(pve)
    enemyIMG=pygame.image.load('Resources/image/startPage/pvpIMG.png')
    pvp=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pvpGroup=pygame.sprite.Group()
    pvpGroup.add(pvp)
    enemyIMG=pygame.image.load('Resources/image/startPage/pvpMario.png')
    pvpMario=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pvpMarioGroup=pygame.sprite.Group()
    pvpMarioGroup.add(pvpMario)
    enemyIMG=pygame.image.load('Resources/image/startPage/pveMario.png')
    pveMario=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pveMarioGroup=pygame.sprite.Group()
    pveMarioGroup.add(pveMario)
    enemyIMG=pygame.image.load('Resources/image/startPage/pvpTest.png')
    pvpTest=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pvpTestGroup=pygame.sprite.Group()
    pvpTestGroup.add(pvpTest)
    enemyIMG=pygame.image.load('Resources/image/startPage/pveTest.png')
    pveTest=Enemy([0,0],enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,enemyIMG,640,360)
    pveTestGroup=pygame.sprite.Group()
    pveTestGroup.add(pveTest)
    enemyEstocGroup=pygame.sprite.Group()
    WeaponGroup = pygame.sprite.Group()
    weaponGroupCount=0
    ## loading player,enemy, weapons on the ground, weapon of player and enemy
    
    groundHitBoxIMG=pygame.image.load('Resources/image/startPage/startHugeGround.png')
    groundHitBox=GroundHITBOX(groundHitBoxIMG)
    groundGroupHITBOX = pygame.sprite.Group()
    groundGroupHITBOX.add(groundHitBox)
    
    quitIMG=pygame.image.load('Resources/image/startPage/startQuit.png')
    quitHitBox=GroundHITBOX(quitIMG)
    quitGroup = pygame.sprite.Group()
    quitGroup.add(quitHitBox)
    
    helpIMG=pygame.image.load('Resources/image/startPage/startHelp.png')
    helpHitBox=GroundHITBOX(helpIMG)
    helpGroup = pygame.sprite.Group()
    helpGroup.add(helpHitBox)
    
    setIMG=pygame.image.load('Resources/image/startPage/startSetting.png')
    setHitBox=GroundHITBOX(setIMG)
    setGroup = pygame.sprite.Group()
    setGroup.add(setHitBox)
    
    creditIMG=pygame.image.load('Resources/image/startPage/startCredit.png')
    creditHitBox=GroundHITBOX(creditIMG)
    creditGroup = pygame.sprite.Group()
    creditGroup.add(creditHitBox)
    
    helpShow=pygame.image.load('Resources/image/startPage/Help.png')
    helpShow=GroundHITBOX(helpShow)
    helpShowGroup = pygame.sprite.Group()
    helpShowGroup.add(helpShow)
    
    SetShow=pygame.image.load('Resources/image/startPage/Set.png')
    SetShow=GroundHITBOX(SetShow)
    setShowGroup = pygame.sprite.Group()
    setShowGroup.add(SetShow)
    
    CreditShow=pygame.image.load('Resources/image/startPage/Credit.png')
    CreditShow=GroundHITBOX(CreditShow)
    CreditShowGroup = pygame.sprite.Group()
    CreditShowGroup.add(CreditShow)
    
    CreditShowUp=pygame.image.load('Resources/image/startPage/CreditShow.png')
    CreditShowUp=LongShow(CreditShowUp)
    CreditShowUpGroup = pygame.sprite.Group()
    CreditShowUpGroup.add(CreditShowUp)
    
    Instruction=pygame.image.load('Resources/image/startPage/instruction.png')
    Instruction=GroundHITBOX(Instruction)
    InstructionGroup = pygame.sprite.Group()
    InstructionGroup.add(Instruction)
    
    pveHelp=pygame.image.load('Resources/image/startPage/pveHelp.png')
    pveHelp=GroundHITBOX(pveHelp)
    pveHelpGroup = pygame.sprite.Group()
    pveHelpGroup.add(pveHelp)
    
    pvpHelp=pygame.image.load('Resources/image/startPage/pvpHelp.png')
    pvpHelp=GroundHITBOX(pvpHelp)
    pvpHelpGroup = pygame.sprite.Group()
    pvpHelpGroup.add(pvpHelp)
    
    howToControl=pygame.image.load('Resources/image/startPage/howToControl.png')
    howToControl=GroundHITBOX(howToControl)
    howToControlGroup = pygame.sprite.Group()
    howToControlGroup.add(howToControl)
    
    Control=pygame.image.load('Resources/image/startPage/Control.png')
    Control=GroundHITBOX(Control)
    ControlGroup = pygame.sprite.Group()
    ControlGroup.add(Control)
    
    mapState='middle'
    music=pygame.mixer.Sound('Resources/audio/startPage/0.wav')
    music.play()
    
    ## loading background and instructions
    
    crashed=False
    while not crashed:
        if groundHitBox.rect.x==-1*displayWidth and killed(player,pveGroup,playerEstocGroup):
            mapState='right'
        if player.rect.x<-40 and mapState=='right' and player.rect.y==242:
            mapState='middle'
        if groundHitBox.rect.x==-1*displayWidth and killed(player,pvpGroup,playerEstocGroup):
            mapState='left'
        if player.rect.x>540 and mapState=='left' and player.rect.y==242:
            mapState='middle'
            
        if mapState=='left' and groundHitBox.rect.x==0 and killed(player,pvpMarioGroup,playerEstocGroup):
            music.fadeout(1000)
            return 'pvpmario'
        
        if mapState=='right' and groundHitBox.rect.x==-2*displayWidth and killed(player,pveMarioGroup,playerEstocGroup):
            music.fadeout(1000)
            return 'pvemario'
            
        if mapState=='left' and groundHitBox.rect.x==0 and killed(player,pvpTestGroup,playerEstocGroup):
            music.fadeout(1000)
            return 'pvptest'
            
        if mapState=='right' and groundHitBox.rect.x==-2*displayWidth and killed(player,pveTestGroup,playerEstocGroup):
            music.fadeout(1000)
            return 'pvetest'
            
        
        ## if the enemy was hitted by the weapon
            
        if mapState=='right' and groundHitBox.rect.x>-1261:
            difference=groundHitBox.rect.x+(displayWidth)*2
            value=difference//20
            groundHitBox.rect.x-=value
            pve.rect.x-=value
            pvp.rect.x-=value
            differenceForPlayer=player.rect.x+10
            value=differenceForPlayer//20
            player.rect.x-=value
        elif -1280<groundHitBox.rect.x<=-1261 and mapState=='right':
            groundHitBox.rect.x-=1
            pve.rect.x-=1
            pvp.rect.x-=1
        if mapState=='middle' and groundHitBox.rect.x<-640:
            difference=groundHitBox.rect.x+(displayWidth)
            value=difference//20
            groundHitBox.rect.x-=value
            pve.rect.x-=value
            pvp.rect.x-=value
            differenceForPlayer=331-player.rect.x
            value=differenceForPlayer//20
            player.rect.x+=value
        
        if mapState=='left' and groundHitBox.rect.x<0:
            difference=groundHitBox.rect.x
            value=difference//20
            groundHitBox.rect.x-=value
            pve.rect.x-=value
            pvp.rect.x-=value
            differenceForPlayer=500-player.rect.x
            value=differenceForPlayer//20
            player.rect.x+=value
            
        if mapState=='middle' and groundHitBox.rect.x>-640:
            difference=groundHitBox.rect.x+(displayWidth)
            value=difference//20
            groundHitBox.rect.x-=value
            pve.rect.x-=value
            pvp.rect.x-=value
            differenceForPlayer=331-player.rect.x
            value=differenceForPlayer//20
            player.rect.x+=value
        if mapState=='middle' and groundHitBox.rect.x>-640:
            groundHitBox.rect.x-=1
            pve.rect.x-=1
            pvp.rect.x-=1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if repr(event)=='''<Event(2-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 1})>''':
                if player.haveWeapon:
                    player.changeAttackState(1)
                else:
                    if player.pickUpWeapon(WeaponGroup):
                        if len(playerEstocGroup)!=0:
                            estocDrop=makeEstocWithoutMaster([playerEstoc.rect.x,playerEstoc.rect.y])
                            WeaponGroup.add(estocDrop)
                        playerEstoc=makeEstoc(player)
                        playerEstocGroup=pygame.sprite.Group()
                        playerEstocGroup.add(playerEstoc)
                        
            if repr(event)=='''<Event(2-KeyDown {'unicode': 'w', 'key': 119, 'mod': 0, 'scancode': 13})>''':
                if player.haveWeapon:
                    player.changeAttackState(-1)
        ## change attackHeight, pick up weapon, and quit
                
                
        fps =  clock.get_fps()
        pygame.display.set_caption('15-112 Term Project (Version: Final Version) [Menu] FPS:'+str(int(fps)))
        key = pygame.key.get_pressed()
        playerPressed,enemyPressed=False,False
        
        
        
        ## hit the instructions

        playerPressed=attack(player,playerEstoc,groundGroupHITBOX,displayWidth)
        
        if key[player.move[2]]:
            if withWeapon(player):
                if player.attack(0.5,groundGroupHITBOX):
                    playerEstoc.attack()
                    playerPressed=True
                elif player.jumpAttack(groundGroupHITBOX,displayWidth):
                    playerPressed=True
                    player.fallingSpeed=0
            elif player.jumpAttack(groundGroupHITBOX,displayWidth):
                playerPressed=True
                player.fallingSpeed=0
        ## attack
        
        playerorenemyGravity(playerGroup,groundGroupHITBOX)
        weaponGravity(WeaponGroup,groundGroupHITBOX)
        ## Gravity
        if groundHitBox.rect.x%640==0:
            for i in range(2):
                if key[player.move[i]]:
                    if player.runUpdate(0.5,i):
                        player.direction=i
                        playerPressed=True
                    player.changeMask()
                    playerHitWall = pygame.sprite.spritecollide(player, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                    if playerHitWall:
                        player.rect.x -= player.dx * [-1, 1][i]
                    outOfScreen(player,displayWidth)
        ## run
                
        if not playerPressed:
            player.notPressing(player.direction)
        ## stand
        if groundHitBox.rect.x%640==0:
            jumpPlayer(player,key)
        ## jump
        
        rollcrawlPlayerOrEnemy(player,key,groundGroupHITBOX,displayWidth)
        ## crawl or roll
            
        if key[player.move[4]] and player.state=='throwAttack':
            moving=False
            for i in range(2):
                if key[player.move[i]]:
                    moving=True
                    player.throwAttack(0.5,i)
                    if key[player.move[2]]:
                        player.throw()
                        playerEstoc.master=None
                        playerEstoc.direction=player.direction
                    player.changeMask()
                    playerHitWall = pygame.sprite.spritecollide(player, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                    if playerHitWall:
                        player.rect.x -= player.dx * [-1, 1][i]
                    outOfScreen(player,displayWidth)
            if moving==False:
                if key[player.move[2]]:
                    player.throw()
                    playerEstoc.master=None
                    playerEstoc.direction=player.direction
                player.throwAttack(0.5,None)
        elif player.onSky==False and player.state=='throwAttack':
            player.state='stand'
        ## throw
        
        player.changeMaskBack()
        
        for item in playerEstocGroup:
            if item.update(enemyEstocGroup,groundGroupHITBOX):
                playerEstocGroup.remove(item)
                estocDrop=makeEstocWithoutMaster([item.rect.x,item.rect.y])
                WeaponGroup.add(estocDrop)
        ## player's flying Estoc hit something thus it falls down and 'becomes' a normal estoc
        gameDisplay.fill((255,255,255))
        drawed=False
        credit=False
        if mapState=='middle' and groundHitBox.rect.x==-displayWidth:
            player.changeMask()
            if pygame.sprite.spritecollide(player, quitGroup, False, pygame.sprite.collide_mask):
                pygame.quit()
                quit()
                sys.exit()
    
            if pygame.sprite.spritecollide(player, helpGroup, False, pygame.sprite.collide_mask):
                helpShowGroup.draw(gameDisplay)
                if canAttack(player) or playerEstoc.master==None:
                    playerEstocGroup.draw(gameDisplay)
                playerGroup.draw(gameDisplay)
                drawed=True
                
            if pygame.sprite.spritecollide(player, setGroup, False, pygame.sprite.collide_mask):
                setShowGroup.draw(gameDisplay)
                if canAttack(player) or playerEstoc.master==None:
                    playerEstocGroup.draw(gameDisplay)
                playerGroup.draw(gameDisplay)
                drawed=True
                
            if pygame.sprite.spritecollide(player, creditGroup, False, pygame.sprite.collide_mask):
                CreditShowGroup.draw(gameDisplay)
                CreditShowUpGroup.draw(gameDisplay)
                if CreditShowUp.rect.y+CreditShowUp.image.get_size()[1]>displayHeight:
                    CreditShowUp.rect.y-=2
                if canAttack(player) or playerEstoc.master==None:
                    playerEstocGroup.draw(gameDisplay)
                playerGroup.draw(gameDisplay)
                drawed=True
                credit=True
                
            if 271<player.rect.x<395 and player.rect.y==242:
                InstructionGroup.draw(gameDisplay)
                
            if  pygame.sprite.spritecollide(player, howToControlGroup, False, pygame.sprite.collide_mask):
                ControlGroup.draw(gameDisplay)
                if canAttack(player) or playerEstoc.master==None:
                    playerEstocGroup.draw(gameDisplay)
                playerGroup.draw(gameDisplay)
                drawed=True
            
            player.changeMaskBack()
        
        if mapState=='right' and groundHitBox.rect.x==-2*displayWidth:
            if -7<player.rect.x<67:
                pveHelpGroup.draw(gameDisplay)
                
        if mapState=='left' and groundHitBox.rect.x==0:
            if 437<player.rect.x<513:
                pvpHelpGroup.draw(gameDisplay)
            
        
        if drawed==False:
            if canAttack(player) or playerEstoc.master==None:
                playerEstocGroup.draw(gameDisplay)
            playerGroup.draw(gameDisplay)
            WeaponGroup.draw(gameDisplay)
            groundGroupHITBOX.draw(gameDisplay)
            pveGroup.draw(gameDisplay)
            pvpGroup.draw(gameDisplay)
        
        if credit==False:
            CreditShowUp.rect.y=0
            

        ## draw all the things that needed to be drawed
        
        pygame.display.update()
        clock.tick(FPS)