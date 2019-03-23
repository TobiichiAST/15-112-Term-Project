import random
import pygame
import sys
from ClassesAndHelperFunctions import *
##Classes and helper functions

def pve(bot,map):
    pygame.init()
    displayWidth=640
    displayHeight=360
    FPS=60
    gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))
    clock=pygame.time.Clock()
    turn='natural'
    gameState='game'
    ##initial value of pygame
    botLearningCount=0
    playerResurrectCount=0
    enemyResurrectCount=0
    ##initial value of my own
    player=newPlayer([100,0])
    player.scale(0.55)  
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)
    playerEstoc=makeEstoc(player)
    playerEstocGroup=pygame.sprite.Group()
    playerEstocGroup.add(playerEstoc)
    # set up player
    enemy=newEnemy([500,0])
    enemy.scale(0.55)
    enemyGroup=pygame.sprite.Group()
    enemyGroup.add(enemy)
    enemyEstoc=makeEstoc(enemy)
    enemyEstocGroup=pygame.sprite.Group()
    enemyEstocGroup.add(enemyEstoc)
    # set up enemy
    WeaponGroup = pygame.sprite.Group()
    weaponGroupCount=0
    groundIMG=pygame.image.load('Resources/image/'+map+'/ground.png')
    ground=Ground(groundIMG)
    groundHitBoxIMG=pygame.image.load('Resources/image/'+map+'/groundHitBox.png')
    groundHitBox=GroundHITBOX(groundHitBoxIMG)
    groundPlayerWinningIMG=pygame.image.load('Resources/image/'+map+'/groundPlayerWinning.png')
    groundPlayerWinning=GroundHITBOX(groundPlayerWinningIMG)
    groundEnemyWinningIMG=pygame.image.load('Resources/image/'+map+'/groundEnemyWinning.png')
    groundEnemyWinning=GroundHITBOX(groundEnemyWinningIMG)
    
    playerGoIMG=pygame.image.load('Resources/image/playerGo.png')
    playerGo=GroundHITBOX(playerGoIMG)
    playerGoGroup=pygame.sprite.Group()
    playerGoGroup.add(playerGo)
    
    enemyGoIMG=pygame.image.load('Resources/image/enemyGo.png')
    enemyGo=GroundHITBOX(enemyGoIMG)
    enemyGoGroup=pygame.sprite.Group()
    enemyGoGroup.add(enemyGo)
    
    music=pygame.mixer.Sound('Resources/audio/'+map+'/0.wav')
    music.play()
    win=pygame.mixer.Sound('Resources/audio/'+map+'/1.wav')
    ##load Image
    groundGroup = pygame.sprite.Group()
    groundGroup.add(ground)
    groundGroupHITBOX = pygame.sprite.Group()
    groundGroupHITBOX.add(groundHitBox)
    groundPlayerWin = pygame.sprite.Group()
    groundPlayerWin.add(groundPlayerWinning)
    groundEnemyWin = pygame.sprite.Group()
    groundEnemyWin.add(groundEnemyWinning)
    ##put image into pygame sprite groups
            
##main game
    crashed=False
    while not crashed:
        if gameState=='game':
            for item in playerGroup:
                if killed(item,enemyGroup,playerEstocGroup):
                    enemyGroup.remove(enemy)
                    enemyEstocGroup.remove(enemyEstoc)
                    estocDrop=makeEstocWithoutMaster(enemyEstoc.rect.center)
                    WeaponGroup.add(estocDrop)
                    bot.update_scores()
            for item in enemyGroup:
                if killed(item,playerGroup,enemyEstocGroup):
                    playerGroup.remove(player)
                    playerEstocGroup.remove(playerEstoc)
                    estocDrop=makeEstocWithoutMaster(playerEstoc.rect.center)
                    WeaponGroup.add(estocDrop)
                    bot.update_scores()
            ## if the the player or enemy was hitted by the weapon(die)       
            if canAttack(player) and canAttack(enemy):
                for item in playerEstocGroup:
                    if pygame.sprite.spritecollide(item,enemyEstocGroup,False,pygame.sprite.collide_mask):
                        if enemy.rect.x>player.rect.x:
                            difference=(enemy.rect.x+enemy.smallX)-(player.rect.x+player.largeX)
                            value=(112-difference)//6
                            enemy.rect.x+=value
                            player.rect.x-=value
                            outOfScreen(player,displayWidth,turn)
                            outOfScreen(enemy,displayWidth,turn)
                            if pygame.sprite.spritecollide(enemy,groundGroupHITBOX,False,pygame.sprite.collide_mask):
                                enemy.rect.x-=value
                            if pygame.sprite.spritecollide(player,groundGroupHITBOX,False,pygame.sprite.collide_mask):
                                player.rect.x+=value
                        if player.rect.x>enemy.rect.x:
                            difference=(player.rect.x+player.smallX)-(enemy.rect.x+enemy.largeX)
                            value=(112-difference)//6
                            enemy.rect.x-=value
                            player.rect.x+=value
                            outOfScreen(player,displayWidth,turn)
                            outOfScreen(enemy,displayWidth,turn)
                            if pygame.sprite.spritecollide(enemy,groundGroupHITBOX,False,pygame.sprite.collide_mask):
                                enemy.rect.x+=value
                            if pygame.sprite.spritecollide(player,groundGroupHITBOX,False,pygame.sprite.collide_mask):
                                player.rect.x-=value
            ## estoc hit function work!
            xDifference=enemy.rect.x-(enemy.rect.x)%10-(player.rect.x-(player.rect.x)%10)
            yDifference=enemy.rect.y-(enemy.rect.y)%40-(player.rect.y-(player.rect.y)%40)
            enemyState=player.state
            if enemyState=='runAttack':
                enemyState='attack'
            myState=enemy.state
            attackHeightDifference=player.attackHeight-enemy.attackHeight
            if myState not in ['attack','runAttack','throwAttack','standWithouWeapon','rollingAttack','jumpAttack'] and enemyState not in ['throwAttack','standWithoutWeapon'] and -200<xDifference<200 and -200<yDifference<200 and len(playerGroup)!=0:
                botAction=bot.act(xDifference,yDifference,enemyState,myState,attackHeightDifference)
            else:
                botAction=1
                if playerorenemyGravity(enemyGroup,groundGroupHITBOX) and random.randint(0,10)==1:
                    botAction=3
            ## The action the AI
            
            if synchronizeWinnning(player,groundGroup,groundPlayerWin):
                if map!='test':
                    music.stop()
                    win.play()
                    gameState='win'
                else:
                    bot.update_scores()
                    music.stop()
                    return pve(bot,map)
            
            if synchronizeWinnning(enemy,groundGroup,groundEnemyWin):
                if map!='test':
                    music.stop()
                    win.play()
                    gameState='win'
                else:
                    bot.update_scores()
                    music.stop()
                    return pve(bot,map)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
                # quit
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and map=='test':
                    music.fadeout(1000)
                    win.play()
                    return
                    
                if botAction==5:
                    if enemy.haveWeapon:
                        enemy.changeAttackState(1)
                    else:
                        if enemy.pickUpWeapon(WeaponGroup):
                            if len(enemyEstocGroup)!=0:
                                estocDrop=makeEstocWithoutMaster(enemyEstoc.rect.center)
                                WeaponGroup.add(estocDrop)
                            enemyEstoc=makeEstoc(enemy)
                            enemyEstocGroup=pygame.sprite.Group()
                            enemyEstocGroup.add(enemyEstoc)
                if botAction==4:
                    if enemy.haveWeapon:
                        enemy.changeAttackState(-1)
                        if (player.state=='attack' or player.state=='runningAttack' or player.state=='stand') and player.haveWeapon:
                            playerEstoc.update(enemyEstocGroup,groundGroupHITBOX)
                            enemyEstoc.update(playerEstocGroup,groundGroupHITBOX)
                            if pygame.sprite.spritecollide(enemyEstoc, playerEstocGroup, False, pygame.sprite.collide_mask):
                                playerEstocGroup.remove(playerEstoc)
                                estocDrop=makeEstocWithoutMaster(playerEstoc.rect.center)
                                WeaponGroup.add(estocDrop)
                                player.haveWeapon=False
                # enemy
    
                if repr(event)=='''<Event(2-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 1})>''':
                    if player.haveWeapon:
                        player.changeAttackState(1)
                    else:
                        if player.pickUpWeapon(WeaponGroup):
                            if len(playerEstocGroup)!=0:
                                estocDrop=makeEstocWithoutMaster(playerEstoc.rect.center)
                                WeaponGroup.add(estocDrop)
                            playerEstoc=makeEstoc(player)
                            playerEstocGroup=pygame.sprite.Group()
                            playerEstocGroup.add(playerEstoc)
                
                            
                if repr(event)=='''<Event(2-KeyDown {'unicode': 'w', 'key': 119, 'mod': 0, 'scancode': 13})>''':
                    if player.haveWeapon:
                        player.changeAttackState(-1)
                        if (enemy.state=='attack' or enemy.state=='runningAttack' or enemy.state=='stand') and enemy.haveWeapon:
                            playerEstoc.update(enemyEstocGroup,groundGroupHITBOX)
                            enemyEstoc.update(playerEstocGroup,groundGroupHITBOX)
                            if pygame.sprite.spritecollide(playerEstoc, enemyEstocGroup, False, pygame.sprite.collide_mask):
                                enemyEstocGroup.remove(enemyEstoc)
                                estocDrop=makeEstocWithoutMaster(enemyEstoc.rect.center)
                                WeaponGroup.add(estocDrop)
                                enemy.haveWeapon=False
                # player
            ## change the attack height
            
            fps =  clock.get_fps()
            pygame.display.set_caption('15-112 Term Project (Version: Alpha Version) [Main Game] FPS:'+str(int(fps)))
            key = pygame.key.get_pressed()
            playerPressed,enemyPressed=False,False
            ## initial values of every frame
            
            playerPressed=attack(player,playerEstoc,groundGroupHITBOX,displayWidth,turn)
            
            if key[player.move[2]]:
                if withWeapon(player):
                    if player.attack(0.5,groundGroupHITBOX):
                        playerEstoc.attack()
                        playerPressed=True
                    elif player.jumpAttack(groundGroupHITBOX,displayWidth,turn):
                        playerPressed=True
                        player.fallingSpeed=0
                elif player.jumpAttack(groundGroupHITBOX,displayWidth,turn):
                    playerPressed=True
                    player.fallingSpeed=0
                    
            enemyPressed=attack(enemy,enemyEstoc,groundGroupHITBOX,displayWidth,turn)
            
            if botAction==0:
                if withWeapon(enemy):
                    if enemy.attack(0.5,groundGroupHITBOX):
                        enemyEstoc.attack()
                        enemyPressed=True
                    elif enemy.jumpAttack(groundGroupHITBOX,displayWidth,turn):
                        enemyPressed=True
                        enemy.fallingSpeed=0
                elif enemy.jumpAttack(groundGroupHITBOX,displayWidth,turn):
                    enemyPressed=True
                    enemy.fallingSpeed=0
            ## attack
    
            playerorenemyGravity(playerGroup,groundGroupHITBOX)
            
            weaponGravity(WeaponGroup,groundGroupHITBOX)
            if player.rect.y>displayHeight:
                playerGroup.remove(player)
                playerEstocGroup.remove(playerEstoc)
            if enemy.rect.y>displayHeight:
                enemyGroup.remove(enemy)
                enemyEstocGroup.remove(enemyEstoc)
            ## Gravity
            
            for i in range(2):
                if key[player.move[i]]:
                    currentLargeX=player.largeX
                    currentSmallX=player.smallX
                    if player.runUpdate(0.5,i):
                        player.direction=i
                        playerPressed=True
                    player.changeMask()
                    playerHitWall = pygame.sprite.spritecollide(player, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                    if playerHitWall:
                        player.rect.x -= player.dx * [-1, 1][i]
                    outOfScreen(player,displayWidth,turn)
                    
            if botAction==1 or botAction==2:
                i=botAction-1
                currentLargeX=enemy.largeX
                currentSmallX=enemy.smallX
                if enemy.runUpdate(0.5,i):
                    enemy.direction=i
                    enemyPressed=True
                enemy.changeMask()
                enemyHitWall = pygame.sprite.spritecollide(enemy, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                if enemyHitWall:
                    enemy.rect.x -= enemy.dx * [-1, 1][i]
                outOfScreen(enemy,displayWidth,turn)
            ## run
            
            if not enemyPressed:
                enemy.notPressing(enemy.direction)
            if not playerPressed:
                player.notPressing(player.direction)
            ## stand
            if botAction==3:
                jumpAI(enemy)
            jumpPlayer(player,key)
            ## jump
            
            rollcrawlAI(enemy,botAction,groundGroupHITBOX,displayWidth,turn)
            rollcrawlPlayerOrEnemy(player,key,groundGroupHITBOX,displayWidth,turn)
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
                        outOfScreen(player,displayWidth,turn)
                if moving==False:
                    if key[player.move[2]]:
                        player.throw()
                        playerEstoc.master=None
                        playerEstoc.direction=player.direction
                    player.throwAttack(0.5,None)
            elif player.onSky==False and player.state=='throwAttack':
                player.state='stand'
            # player
            ## throw
            
            player.changeMaskBack()
            enemy.changeMaskBack()
            
            for item in playerEstocGroup:
                if item.update(enemyEstocGroup,groundGroupHITBOX):
                    playerEstocGroup.remove(item)
                    estocDrop=makeEstocWithoutMaster(item.rect.center)
                    WeaponGroup.add(estocDrop)
                    
            for item in enemyEstocGroup:
                if item.update(playerEstocGroup,groundGroupHITBOX):
                    enemyEstocGroup.remove(item)
                    estocDrop=makeEstocWithoutMaster(item.rect.center)
                    WeaponGroup.add(estocDrop)
            ## player's or enemy's Estoc hit something thus it falls down and 'becomes' a normal estoc
            maxXP,minXP=getBrounce(pygame.mask.from_surface(player.allImages['standHitBox'][0]).outline())
            maxXE,minXE=getBrounce(pygame.mask.from_surface(enemy.allImages['standHitBox'][0]).outline())
            
            if turn=='natural':
                pass
            elif turn=='player':
                if len(enemyGroup)==0:
                    difference=minXP+player.rect.x-displayWidth/5
                    difference=int(difference/20)
                    player.rect.x-=difference
                    ground.rect.x-=difference
                    groundHitBox.rect.x-=difference
                if len(enemyGroup)!=0:
                    if enemy.rect.x>player.rect.x:
                        middle=(maxXE+minXP+player.rect.x+enemy.rect.x)/2
                        difference=int((middle-displayWidth/2)/10)
                    if player.rect.x>enemy.rect.x:
                        middle=(maxXP+minXE+player.rect.x+enemy.rect.x)/2
                        difference=int((middle-displayWidth/2)/10)
                    player.rect.x-=difference
                    enemy.rect.x-=difference
                    ground.rect.x-=difference
                    groundHitBox.rect.x-=difference
                    if enemy.rect.x+(maxXE+minXE)/4<0:
                        enemyGroup.remove(enemy)
                        enemyEstocGroup.remove(enemyEstoc)
                        estocDrop=makeEstocWithoutMaster(enemyEstoc.rect.center)
                        WeaponGroup.add(estocDrop)
                for item in WeaponGroup:
                    item.rect.x-=difference
            elif turn=='enemy':
                if len(playerGroup)==0:
                    difference=displayWidth*4/5-(enemy.rect.x+maxXE)
                    difference=int(difference/20)
                    enemy.rect.x+=difference
                    ground.rect.x+=difference
                    groundHitBox.rect.x+=difference
                if len(playerGroup)!=0:
                    if enemy.rect.x>player.rect.x:
                        middle=(maxXE+minXP+player.rect.x+enemy.rect.x)/2
                        difference=int((middle-displayWidth/2)/10)
                    if player.rect.x>enemy.rect.x:
                        middle=(maxXP+minXE+player.rect.x+enemy.rect.x)/2
                        difference=int((middle-displayWidth/2)/10)
                    player.rect.x-=difference
                    enemy.rect.x-=difference
                    ground.rect.x-=difference
                    groundHitBox.rect.x-=difference
                    if player.rect.x+(maxXP+minXP)*2/3>displayWidth:
                        playerGroup.remove(player)
                        playerEstocGroup.remove(playerEstoc)
                        estocDrop=makeEstocWithoutMaster(playerEstoc.rect.center)
                        WeaponGroup.add(estocDrop)
                    difference=-difference
                for item in WeaponGroup:
                    item.rect.x+=difference
            if ground.rect.x>0:
                difference=ground.rect.x
                ground.rect.x=0
                groundHitBox.rect.x=0
                player.rect.x-=difference
                enemy.rect.x-=difference
                for item in WeaponGroup:
                    item.rect.x-=difference
            if ground.image.get_size()[0]+ground.rect.x<displayWidth:
                difference=displayWidth-(ground.image.get_size()[0]+ground.rect.x)
                ground.rect.x+=difference
                groundHitBox.rect.x+=difference
                player.rect.x+=difference
                enemy.rect.x+=difference
                for item in WeaponGroup:
                    item.rect.x+=difference
            ## move camera
            
            if len(playerGroup)==0 and len(enemyGroup)==0:
                turn='natural'
            elif len(playerGroup)!=0 and len(enemyGroup)!=0 and turn=='natural':
                pass
            elif len(playerGroup)!=0 and len(enemyGroup)==0:
                turn='player'
            elif len(playerGroup)==0 and len(enemyGroup)!=0:
                turn='enemy'
            
            ## who's turn
            
            if len(playerGroup)==0 and len(enemyGroup)==0:
                pass
            if len(playerGroup)==0:
                playerResurrectCount+=1
            if len(enemyGroup)==0:
                enemyResurrectCount+=1
            if playerResurrectCount>FPS*2:
                playerResurrectCount=0
                playerX=random.randint(0,displayWidth*3/5)
                playerNew=newPlayer([playerX,0])
                playerNew.scale(0.55)
                playerGroup.add(playerNew)
                playerEstoc=makeEstoc(playerNew)
                playerEstocGroup.add(playerEstoc)
            if enemyResurrectCount>FPS*2:
                enemyResurrectCount=0
                enemyX=random.randint(displayWidth*3/5,displayWidth)
                enemyNew=newEnemy([enemyX,0])
                enemyNew.scale(0.55)
                enemyGroup.add(enemyNew)
                enemyEstoc=makeEstoc(enemyNew)
                enemyEstocGroup.add(enemyEstoc)
            for item in playerGroup:
                player=item
            for item in enemyGroup:
                enemy=item
            for item in playerEstocGroup:
                playerEstoc = item
            for item in enemyEstocGroup:
                enemyEstoc = item 
            ##resurrect
            if len(playerGroup)!=0 and len(enemyGroup)!=0:
                faceingEachOther(player,enemy)
        else:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    return
            
        gameDisplay.fill((255,255,255))
        groundGroup.draw(gameDisplay)
        if canAttack(player) or playerEstoc.master==None:
            playerEstocGroup.draw(gameDisplay)
        if canAttack(enemy) or enemyEstoc.master==None:
            enemyEstocGroup.draw(gameDisplay)
        if len(playerGroup)!=0:
            playerGroup.draw(gameDisplay)
        if len(enemyGroup)!=0:
            enemyGroup.draw(gameDisplay)
        WeaponGroup.draw(gameDisplay)
        if turn=='player':
            playerGoGroup.draw(gameDisplay)
        if turn=='enemy':
            enemyGoGroup.draw(gameDisplay)
        ## draw all the things that needed to be drawed
        
        pygame.display.update()
        clock.tick(FPS)