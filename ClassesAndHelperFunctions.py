import random
import pygame
import sys
## import

def getBrounce(outline):
    maxX=0
    minX=999999
    for item in outline:
        x=item[0]
        if x>maxX:
            maxX=x
        if x<minX:
            minX=x
    return maxX,minX
    
def getListImages(image,w,h):
    width, height = image.get_size()
    images=[]
    if w!=None:
        for i in range( int( width / w ) ):
            images.append( image.subsurface( ( i * w, 0, w, h ) ).convert_alpha())
    else:
        images.append(image)
    return images
    
def scaleImage(imageDictionary,IMGscale):
    newDictionary={}
    for item in imageDictionary:
        newImages=[]
        for image in imageDictionary[item]:
            size=image.get_size()
            scaledImage=pygame.transform.scale(image,(int(size[0]*IMGscale), int(size[1]*IMGscale)))
            newImages.append(scaledImage)
        newDictionary[item]=newImages
    return newDictionary
    
def makeListImages(standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
    runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h):
    allImages={}
    stand1 = [standImage1]
    stand2 = [standImage2]
    stand3 = [standImage3]
    standHitBox = [standHitBox]
    jump=[jumpIMG]
    jumpAttack=[jumpAttackIMG]
    throwAttack=getListImages(throwAttackIMG,w,h)
    standWithoutWeapon=[standWithoutWeapon]
    run = getListImages(runImage,w,h)
    crawl = getListImages(crawlIMG,w,h)
    roll = getListImages(rollIMG,w,h)
    rollingAttack = getListImages(rollingAttackIMG,w,h)
    attack1= getListImages(attack1,w,h)
    attack2= getListImages(attack2,w,h)
    attack3= getListImages(attack3,w,h)
    allImages['stand1']=stand1
    allImages['stand2']=stand2
    allImages['stand3']=stand3
    allImages['standWithoutWeapon']=standWithoutWeapon
    allImages['standHitBox']=standHitBox
    allImages['jump']=jump
    allImages['jumpAttack']=jumpAttack
    allImages['throwAttack']=throwAttack
    allImages['run']=run
    allImages['crawl']=crawl
    allImages['roll']=roll
    allImages['rollingAttack']=rollingAttack
    allImages['attack1']=attack1
    allImages['attack2']=attack2
    allImages['attack3']=attack3
    return allImages    
    
def outOfScreen(item,screenWidth,turn=None):
    if turn==None or turn=='natural':
        if item.rect.x+item.smallX<0:
            item.rect.x=-item.smallX
        if item.rect.x+item.largeX>screenWidth:
            item.rect.x=screenWidth-item.largeX
    if turn=='player':
        if isinstance(item,Player):
            if item.rect.x+item.smallX<0:
                item.rect.x=-item.smallX
            if item.rect.x+item.smallX>screenWidth:
                item.rect.x=screenWidth-item.smallX
        else:
            if item.rect.x+item.smallX<0:
                item.rect.x=-item.smallX
            if item.rect.x+item.largeX>screenWidth:
                item.rect.x=screenWidth-item.largeX
    if turn=='enemy':
        if isinstance(item,Enemy):
            if item.rect.x+item.largeX<0:
                item.rect.x=-item.largeX
            if item.rect.x+item.largeX>screenWidth:
                item.rect.x=screenWidth-item.largeX
        else:
            if item.rect.x+item.smallX<0:
                item.rect.x=-item.smallX
            if item.rect.x+item.largeX>screenWidth:
                item.rect.x=screenWidth-item.largeX
    
    
    
    
def makeListImagesEstoc(attack1,attack2,attack3,w,h):
    allImages={}
    attack1= getListImages(attack1,w,h)
    attack2= getListImages(attack2,w,h)
    attack3= getListImages(attack3,w,h)
    allImages['attack1']=attack1
    allImages['attack2']=attack2
    allImages['attack3']=attack3
    return allImages
    
def died(item,displayHeight):
    if item.rect.y>displayHeight:
        return True
    return False
    
def synchronizeWinnning(player,ground,win):
    for groundObject in ground:
        for winMap in win:
            winMap.rect.x=groundObject.rect.x
    if pygame.sprite.spritecollide(player, win, False, pygame.sprite.collide_mask):
        return True
        
def newPlayer(pos):
    playerStandIMG1 = pygame.image.load('Resources/image/playerStand1.png')
    playerStandIMG2 = pygame.image.load('Resources/image/playerStand2.png')
    playerStandIMG3 = pygame.image.load('Resources/image/playerStand3.png')
    playerStandHitBox = pygame.image.load('Resources/image/playerStandHitBox.png')
    jumpIMG = pygame.image.load('Resources/image/playerJump.png')
    jumpAttackIMG = pygame.image.load('Resources/image/playerJumpAttack.png')
    throwAttackIMG = pygame.image.load('Resources/image/playerThrow.png')
    runIMG = pygame.image.load('Resources/image/playerRunning.png')
    crawlIMG = pygame.image.load('Resources/image/playerCrawl.png')
    rollIMG=pygame.image.load('Resources/image/playerRolling.png')
    rollingAttackIMG=pygame.image.load('Resources/image/playerRollingAttack.png')
    move1=pygame.image.load('Resources/image/playerAttackHigh.png')
    move2=pygame.image.load('Resources/image/playerAttackMid.png')
    move3=pygame.image.load('Resources/image/playerAttackLow.png')
    standWithoutWeapon=pygame.image.load('Resources/image/playerStandNoWeapon.png')
    result=Player(pos,playerStandIMG1,playerStandIMG2,playerStandIMG3,playerStandHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,runIMG,crawlIMG,rollIMG,rollingAttackIMG,move1,move2,move3,252,212)
    return result
    
def newEnemy(pos):
    playerStandIMG1 = pygame.image.load('Resources/image/playerStand1.png')
    playerStandIMG2 = pygame.image.load('Resources/image/playerStand2.png')
    playerStandIMG3 = pygame.image.load('Resources/image/playerStand3.png')
    playerStandHitBox = pygame.image.load('Resources/image/playerStandHitBox.png')
    jumpIMG = pygame.image.load('Resources/image/playerJump.png')
    jumpAttackIMG = pygame.image.load('Resources/image/playerJumpAttack.png')
    throwAttackIMG = pygame.image.load('Resources/image/playerThrow.png')
    runIMG = pygame.image.load('Resources/image/playerRunning.png')
    crawlIMG = pygame.image.load('Resources/image/playerCrawl.png')
    rollIMG=pygame.image.load('Resources/image/playerRolling.png')
    rollingAttackIMG=pygame.image.load('Resources/image/playerRollingAttack.png')
    move1=pygame.image.load('Resources/image/playerAttackHigh.png')
    move2=pygame.image.load('Resources/image/playerAttackMid.png')
    move3=pygame.image.load('Resources/image/playerAttackLow.png')
    standWithoutWeapon=pygame.image.load('Resources/image/playerStandNoWeapon.png')
    result=Enemy(pos,playerStandIMG1,playerStandIMG2,playerStandIMG3,playerStandHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,runIMG,crawlIMG,rollIMG,rollingAttackIMG,move1,move2,move3,252,212)
    result.direction=0
    result.image=pygame.transform.flip(result.image, True, False)
    result.mask = pygame.mask.from_surface(result.image)
    return result
    
def makeEstoc(player):
    attactIMG1=pygame.image.load('Resources/image/estocHigh.png')
    attactIMG2=pygame.image.load('Resources/image/estocMid.png')
    attactIMG3=pygame.image.load('Resources/image/estocLow.png')
    playerEstoc=Estoc(attactIMG1,attactIMG2,attactIMG3,player)
    return playerEstoc
    
def makeEstocWithoutMaster(pos):
    attactIMG1=pygame.image.load('Resources/image/estocHigh.png')
    attactIMG2=pygame.image.load('Resources/image/estocMid.png')
    attactIMG3=pygame.image.load('Resources/image/estocLow.png')
    myEstoc=EstocWithoutMaster(attactIMG1,attactIMG2,attactIMG3,pos)
    return myEstoc
 
def killed(player,enemyGroup,playerEstocGroup):
    for item in playerEstocGroup:
        if player.state=='attack' or player.state=='stand' or player.state=='runAttack' or player.state=='stand' or player.state=='rollingAttack' or player.haveWeapon==False:
            if pygame.sprite.spritecollide(item, enemyGroup, False, pygame.sprite.collide_mask):
                sound=random.randint(0,1)
                if sound==0:
                    pygame.mixer.Sound('Resources/audio/death/0.wav').play()
                else:
                    pygame.mixer.Sound('Resources/audio/death/1.wav').play()
                return True
    if player.state=='jumpAttack':
        if pygame.sprite.spritecollide(player, enemyGroup, False, pygame.sprite.collide_mask):
            sound=random.randint(0,1)
            if sound==0:
                pygame.mixer.Sound('Resources/audio/death/0.wav').play()
            else:
                pygame.mixer.Sound('Resources/audio/death/1.wav').play()
            return True
            
def attack(player,playerEstoc,groundGroupHITBOX,displayWidth,turn=None):
    if player.state=='attack':
        if player.attack(0.5,groundGroupHITBOX):
            playerEstoc.attack()
            return True
            
    if player.state=='runAttack':
        if player.attack(0.5,groundGroupHITBOX):
            playerEstoc.attack()
            return True
        
    if player.state=='jumpAttack':
        if player.jumpAttack(groundGroupHITBOX,displayWidth,turn):
            return True
        
    if player.state=='rollingAttack':
        if player.attack(0.5,groundGroupHITBOX):
            playerEstoc.attack()
            return True

def withWeapon(player):
    if player.state!='attack' and player.state!='runAttack' and player.state!='rollingAttack' and player.haveWeapon:
        return True
    return False
    
def playerorenemyGravity(group,groundGroupHITBOX):
    for item in group:
        item.changeMask()
        item.fallingSpeed+=item.gravity
        item.rect.y+=item.fallingSpeed
        playerHitGround = pygame.sprite.spritecollide(item, groundGroupHITBOX, False, pygame.sprite.collide_mask)
        if playerHitGround:
            if item.fallingSpeed<0:
                item.rect.y-=item.fallingSpeed
                item.fallingSpeed=0
                return
            item.onSky=False
            if item.state!='attack' and item.state!='runAttack' and item.state!='crawl' and item.state!='throwAttack' and item.state!='roll' and item.state!='rollingAttack':
                item.state='stand'
            item.rect.y-=item.fallingSpeed
            item.fallingSpeed=0
            return True
        
def weaponGravity(WeaponGroup,groundGroupHITBOX):
    for item in WeaponGroup:
        item.fallingSpeed+=item.gravity
        item.rect.y+=item.fallingSpeed
        weaponHitGround = pygame.sprite.spritecollide(item, groundGroupHITBOX, False, pygame.sprite.collide_mask)
        if weaponHitGround:
            item.rect.y-=item.fallingSpeed
            item.fallingSpeed=0
            
def jumpPlayer(player,key=None):
    if key!=None:
        if key[player.move[3]] and player.onSky==False and player.state!='attack' and player.state!='runAttack' and player.state!='rollingAttack':
            player.jump()
    elif player.onSky==False and player.state!='attack' and player.state!='runAttack' and player.state!='rollingAttack':
        player.jump()
    
def jumpAI(player):
    if player.onSky==False and player.state!='attack' and player.state!='runAttack' and player.state!='rollingAttack':
        player.jump()
        

def rollcrawlPlayerOrEnemy(player,key,groundGroupHITBOX,displayWidth,turn=None):
    if key[player.move[5]] and player.onSky==False and player.state!='attack' and (player.state=='crawl' or player.state=='roll') and player.state!='runAttack' and player.state!='rollingAttack':
        crawl=False
        if player.state=='crawl':
            for i in range(2):
                if key[player.move[i]]:
                    crawl=True
                    player.crawl(0.5,i)
                    player.changeMask()
                    playerHitWall = pygame.sprite.spritecollide(player, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                    if playerHitWall:
                        player.rect.x -= player.dx * [-1, 1][i]
                    outOfScreen(player,displayWidth,turn)
        if player.state=='roll':
            for i in range(2):
                if key[player.move[i]]:
                    crawl=True
                    player.roll(0.5,i)
                    player.changeMask()
                    playerHitWall = pygame.sprite.spritecollide(player, groundGroupHITBOX, False, pygame.sprite.collide_mask)
                    if playerHitWall:
                        player.rect.x -= player.dx * [-1, 1][i]
                    outOfScreen(player,displayWidth,turn)
        if crawl==False:
            player.crawl(0.5,None)
    elif player.onSky==False and player.state!='attack' and (player.state=='crawl' or player.state=='roll') and player.state!='runAttack' and player.state!='rollingAttack':
        player.state='stand'
        player.crawlCounter=0
        
def rollcrawlAI(player,action,groundGroupHITBOX,displayWidth,turn=None):
    if action==5 and player.onSky==False and player.state!='attack' and (player.state=='crawl' or player.state=='roll') and player.state!='runAttack' and player.state!='rollingAttack':
        player.crawl(0.5,None)
    elif player.onSky==False and player.state!='attack' and (player.state=='crawl' or player.state=='roll') and player.state!='runAttack' and player.state!='rollingAttack':
        player.state='stand'
        player.crawlCounter=0
        
def canAttack(player):
    if player.state=='stand' or player.state=='attack' or player.state=='runAttack' or player.state=='rollingAttack':
        return True
    return False
    
def faceingEachOther(player,enemy):
    playerDirection=enemy.rect.x-player.rect.x
    if playerDirection>0:
        if player.state=='stand':
            player.direction=1
        if enemy.state=='stand':
            enemy.direction=0
    else:
        if player.state=='stand':
            player.direction=0
        if enemy.state=='stand':
            enemy.direction=1
    
class Thing(pygame.sprite.Sprite):
    def __init__(self,pos,standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
    runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.allImages=makeListImages(standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
    runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h)
        self.image=standImage2
        self.dx=4
        self.dy=4
        self.originalCenter = pos
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.fallingSpeed=0
        self.gravity=1
        self.largeX,self.smallX=getBrounce(pygame.mask.from_surface(self.image).outline())
        self.runCounter = 0
        self.attackCounter = 0
        self.crawlCounter = 0
        self.throwAttackCount = 0
        self.onSky=False
        self.state='stand'
        self.attackHeight=2
        self.direction=1
        self.haveWeapon=True
        self.scaleS=1
        self.ImagesWH=(w,h)

    
    def scale(self,IMGscale):
        self.scaleS=IMGscale
        self.allImages=scaleImage(self.allImages,IMGscale)
        self.image=self.allImages['stand2'][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.originalCenter
        self.mask = pygame.mask.from_surface(self.image)
        self.largeX,self.smallX=getBrounce(pygame.mask.from_surface(self.image).outline())

        
    def runUpdate(self,num,direction):
        if self.state!='attack' and self.state!='runAttack' and self.state!='rollingAttack' and self.state!='crawl' and self.state!='roll' and self.state!='jumpAttack' and self.state!='throwAttack':
            self.direction=direction
            self.rect.x += self.dx * [-1, 1][direction]
            if self.state!='jump':
                self.runCounter+=num
                self.runCounter=self.runCounter%len(self.allImages['run'])
                self.image=self.allImages['run'][int(self.runCounter)]
                if direction==0:
                    self.image=pygame.transform.flip(self.image, True, False)
                self.mask = pygame.mask.from_surface(self.image)
                self.state='run'
            if self.runCounter%4==0:
                pygame.mixer.Sound('Resources/audio/run/0.wav').play()
            return True
            
    
    def notPressing(self,i):
        if self.onSky==False and self.state!='jump' and self.state!='crawl' and self.state!='throwAttack' and self.state!='roll':
            if self.haveWeapon==True:
                standState='stand'+str(4-self.attackHeight)
                self.image=self.allImages[standState][0]
            elif self.haveWeapon==False:
                self.image=self.allImages['standWithoutWeapon'][0]
            if self.direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            self.mask = pygame.mask.from_surface(self.image)
            self.runCounter=0
            self.state='stand'
        
    def changeMask(self):
        self.mask=pygame.mask.from_surface(self.allImages['standHitBox'][0])
        
    def changeMaskBack(self):
        self.mask = pygame.mask.from_surface(self.image)
        
    def changeAttackState(self,i):
        if self.haveWeapon and self.state!='attack' and self.state!='runAttack' and self.state!='rollingAttack':
            self.attackHeight+=i
            if self.attackHeight>3:
                if self.state=='run':
                    self.state='roll'
                else:
                    self.state='crawl'
                self.attackHeight=3
            if self.attackHeight<1:
                self.state='throwAttack'
                self.attackHeight=1

    def attack(self,num,groundGroupHITBOX):
        direction=self.direction
        if (self.state[0:5]=='stand' or self.state=='attack') and self.onSky==False and self.haveWeapon:
            attackState='attack'+str(self.attackHeight)
            self.attackCounter+=num
            if self.attackCounter>len(self.allImages[attackState])-1:
                self.attackCounter=0
                self.state='stand'
                return False
            self.image=self.allImages[attackState][int(self.attackCounter)]
            if direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            self.mask = pygame.mask.from_surface(self.image)
            self.state='attack'
            if self.attackCounter==1:
                sound=random.randint(0,3)
                if sound==0:
                    pygame.mixer.Sound('Resources/audio/attack/0.wav').play()
                elif sound==1:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==2:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==3:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
            return True
        if self.state=='run' or self.state=='runAttack':
            attackState='attack'+str(self.attackHeight)
            self.attackCounter+=num
            if self.attackCounter>len(self.allImages[attackState])-1:
                self.attackCounter=0
                self.state='stand'
                return False
            self.image=self.allImages[attackState][int(self.attackCounter)]
            if direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            if (self.dx-self.attackCounter//4)>0:
                self.rect.x+=(self.dx-self.attackCounter//4)* [-1, 1][direction]
            self.changeMask()
            if pygame.sprite.spritecollide(self, groundGroupHITBOX, False, pygame.sprite.collide_mask):
                self.rect.x-=(self.dx-self.attackCounter//4)* [-1, 1][direction]
            self.mask = pygame.mask.from_surface(self.image)
            self.state='runAttack'
            if self.attackCounter==1:
                sound=random.randint(0,3)
                if sound==0:
                    pygame.mixer.Sound('Resources/audio/attack/0.wav').play()
                elif sound==1:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==2:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==3:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
            return True
        if self.state=='roll' or self.state=='rollingAttack':
            self.attackCounter+=num
            if self.attackCounter>len(self.allImages['rollingAttack'])-1:
                self.attackCounter=0
                self.state='stand'
                return False
            self.image=self.allImages['rollingAttack'][int(self.attackCounter)]
            if direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            if (self.dx-self.attackCounter//2)>0:
                self.rect.x+=(self.dx-self.attackCounter//2)* [-1, 1][direction]
            self.changeMask()
            if pygame.sprite.spritecollide(self, groundGroupHITBOX, False, pygame.sprite.collide_mask):
                self.rect.x-=(self.dx-self.attackCounter//2)* [-1, 1][direction]
            self.mask = pygame.mask.from_surface(self.image)
            self.state='rollingAttack'
            if self.attackCounter==1:
                sound=random.randint(0,3)
                if sound==0:
                    pygame.mixer.Sound('Resources/audio/attack/0.wav').play()
                elif sound==1:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==2:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
                elif sound==3:
                    pygame.mixer.Sound('Resources/audio/attack/1.wav').play()
            return True 
    
    def throwAttack(self,num,direction):
        if self.haveWeapon:
            if direction!=None:
                self.direction=direction
                self.rect.x += (self.dx * [-1, 1][direction])
                self.throwAttackCount+=num
                self.throwAttackCount=self.throwAttackCount%(len(self.allImages['throwAttack'])-1)
                self.image=self.allImages['throwAttack'][int(self.throwAttackCount)+1]
                if direction==0:
                    self.image=pygame.transform.flip(self.image, True, False)
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image=self.allImages['throwAttack'][0]
                if self.direction==0:
                    self.image=pygame.transform.flip(self.image, True, False)
                self.mask = pygame.mask.from_surface(self.image)
            
    def jump(self):
        self.image=self.allImages['jump'][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.fallingSpeed=-17
        self.onSky=True
        self.state='jump'
        
    def jumpAttack(self,ground,displayWidth,turn=None):
        direction=self.direction
        if self.onSky==True:
            self.image=self.allImages['jumpAttack'][0]
            self.rect.x+=2 * [-1, 1][direction]
            self.changeMask()
            playerHitWall = pygame.sprite.spritecollide(self, ground, False, pygame.sprite.collide_mask)
            if playerHitWall:
                self.rect.x -= 2 * [-1, 1][direction]
            outOfScreen(self,displayWidth,turn)
            if direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            self.state='jumpAttack'
            self.mask = pygame.mask.from_surface(self.image)
            return True
            
    def crawl(self,num,direction):
        if direction!=None:
            self.direction=direction
            self.rect.x += (self.dx * [-1, 1][direction])/3
            self.crawlCounter+=num
            self.image=self.allImages['crawl'][int(self.crawlCounter)%len(self.allImages['crawl'])]
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image=self.allImages['crawl'][0]
            self.mask = pygame.mask.from_surface(self.image)
            
    def roll(self,num,direction):
        self.direction=direction
        self.crawlCounter+=num
        if self.dx/2>=self.crawlCounter*0.03:
            self.rect.x += (self.dx-self.crawlCounter* 0.01) * [-1, 1][direction]
            self.image=self.allImages['roll'][int(self.crawlCounter)%len(self.allImages['crawl'])]
            if direction==0:
                self.image=pygame.transform.flip(self.image, True, False)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.state='crawl'
            self.rect.x += (self.dx * [-1, 1][direction])/3
            self.crawlCounter=0
            self.image=self.allImages['crawl'][0]
            self.mask = pygame.mask.from_surface(self.image)
            
    def throw(self):
        self.haveWeapon=False
        self.state='standWithoutWeapon'
        
    def pickUpWeapon(self,WeaponGroup):
        for item in WeaponGroup:
            tempGroup = pygame.sprite.Group()
            tempGroup.add(item)
            if pygame.sprite.spritecollide(self, tempGroup, False, pygame.sprite.collide_mask):
                WeaponGroup.remove(item)
                self.haveWeapon=True
                return True
        
class Player(Thing):
    def __init__(self,pos,standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
    runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h):
        super().__init__(pos,standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
    runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h)
        self.move = [pygame.K_a, pygame.K_d, pygame.K_j,pygame.K_k,pygame.K_w,pygame.K_s]
                
class Enemy(Thing):
    def __init__(self,pos,standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
        runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h):
        super().__init__(pos,standImage1,standImage2,standImage3,standHitBox,jumpIMG,jumpAttackIMG,throwAttackIMG,standWithoutWeapon,
        runImage,crawlIMG,rollIMG,rollingAttackIMG,attack1,attack2,attack3,w,h)
        self.move = [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_KP1, pygame.K_KP2,pygame.K_UP,pygame.K_DOWN]

class Ground(pygame.sprite.Sprite):
    displayWidth=640
    displayHeight=360
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        size=image.get_size()
        IMGscale=Ground.displayHeight/size[1]
        scaledImage=pygame.transform.scale(image,(int(size[0]*IMGscale), int(size[1]*IMGscale)))
        self.image=scaledImage
        self.rect = self.image.get_rect()
        self.rect.x=-(self.image.get_size()[0])//2+Ground.displayWidth/2
        
class GroundHITBOX(Ground):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        size=image.get_size()
        IMGscale=Ground.displayHeight/size[1]
        scaledImage=pygame.transform.scale(image,(int(size[0]*IMGscale), int(size[1]*IMGscale)))
        self.image=scaledImage
        self.rect = self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.x=-(self.image.get_size()[0])//2+Ground.displayWidth/2
        
class LongShow(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        
class Estoc(pygame.sprite.Sprite):
    def __init__(self,image1,image2,image3,master):
        pygame.sprite.Sprite.__init__(self)
        self.allImages=makeListImagesEstoc(image1,image2,image3,master.ImagesWH[0],master.ImagesWH[1])
        scale=master.scaleS
        self.allImages=scaleImage(self.allImages,scale)
        self.image=self.allImages['attack2'][0]
        self.rect = self.image.get_rect()
        self.rect.center = master.originalCenter
        self.mask = pygame.mask.from_surface(self.image)
        self.gravity=1
        self.master=master
        
    def attack(self):
        direction=self.master.direction
        attackState='attack'+str(self.master.attackHeight)
        self.image=self.allImages[attackState][int(self.master.attackCounter)]
        if direction==0:
            self.image=pygame.transform.flip(self.image, True, False)
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self,enemyEstocGroup,groundGroupHITBOX):
        if self.master!=None:
            if self.master.state=='stand':
                state='attack'+str(self.master.attackHeight)
                self.image=self.allImages[state][0]
            if self.master.direction==1:
                self.rect.x=self.master.rect.x+25
            if self.master.direction==0:
                self.rect.x=self.master.rect.x-25
                if self.master.state=='stand':
                    self.image=pygame.transform.flip(self.image, True, False)
            self.rect.y=self.master.rect.y
        if self.master==None:
            self.rect.x+=8*self.direction
            if self.direction==0:
                self.rect.x+=-8
            if pygame.sprite.spritecollide(self, groundGroupHITBOX, False, pygame.sprite.collide_mask):
                return True
            for item in enemyEstocGroup:
                if item.master!=None and pygame.sprite.spritecollide(self, enemyEstocGroup, False, pygame.sprite.collide_mask):
                    return True
        self.mask = pygame.mask.from_surface(self.image)
                
class EstocWithoutMaster(pygame.sprite.Sprite):
     def __init__(self,image1,image2,image3,pos):
        pygame.sprite.Sprite.__init__(self)
        self.allImages=makeListImagesEstoc(image1,image2,image3,252,212)
        scale=0.55
        self.allImages=scaleImage(self.allImages,scale)
        self.image=self.allImages['attack3'][0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.gravity=1
        self.fallingSpeed=0
    