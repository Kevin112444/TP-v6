from cmu_112_graphics import *
import os
import random
import copy


class MyApp(App):

################################################################################
# These are the different classes. The subclasses will be for every individual 
# unit in the game.
# The assets used for this game:
# Sprites for the Units - https://aekashics.itch.io/aekashics-librarium-librarium-static-batch-megapack
# Sprites for the bases(portals) - https://elthen.itch.io/2d-pixel-art-portal-sprites
# Picture for background - https://www.freelancer.is/contest/Need-Background-for-D-Platformer-Game-We-will-work-for-more-after-the-contest-1372733-byentry-22150937?w=f&ngsw-bypass=
################################################################################
        
    class Units(object):
        def __init__(self,health,attack,movespd,range,cost):
            self.health = health   # current hp of the unit
            self.maxHealth = health # original hp of the unit
            self.attack = attack   # the damage per attack
            self.moveSpeed = movespd   # how fast the unit moves
            self.range = range   # how far the unit can attack
            self.cost = cost   # how much the unit will cost
            self.state = 'walk'   # what the unit is doing
            self.spriteCounter = 0  # for animation purposes

        
    class Base(Units):
        def __init__(self,absPos,relPos):
            self.health = 10000
            self.absPos = absPos   # absPos and relPos is used for scrolling
            self.relPos = relPos
    
    class Giant(Units):
        def __init__(self):
            self.age = 1
            self.attack = 2 * self.age
            self.range = 500
            self.state = 'idle'

        def action(self):
            if self.state == 'idle':
                return 2
            elif self.state == 'rangedFight':
                return 4
            elif self.state == 'meleeFight':
                return 6

# the different tuples represent which frame range is used    
    class Bat(Units):
        spritesheet = 0
        
        def __init__(self):
            super().__init__(8,1,40,0,200)
            
            
        def action(self):
            if self.state == 'walk':
                return (0,4)
            elif self.state == 'fight':
                return (38,42)

    class Owl(Units):
        spritesheet = 1
        def __init__(self): 
            super().__init__(7,2,25,200,250)
            self.projectile = 1
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,21)
                    
    class Peacock(Units):
        spritesheet = 2
        def __init__(self):
            super().__init__(12,5,20,0,275)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (36,50)
                
    class Rat(Units):
        spritesheet = 3
        def __init__(self): 
            super().__init__(30,10,10,0,500)
        
        def action(self):
            if self.state == 'walk':
                return (9,18)
            elif self.state == 'fight':
                return (18,32)

    class Anubis(Units):
        spritesheet = 4
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (42,48)
            elif self.state == 'fight':
                return (2,5)
    
    class Knight(Units):
        spritesheet = 5
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,5)
            elif self.state == 'fight':
                return (11,13)
    
    class Slime(Units):
        spritesheet = 6
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (9,14)
            elif self.state == 'fight':
                return (21,26)

    class Spore(Units):
        spritesheet = 7
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,5)
    
    class EarthWorm(Units):
        spritesheet = 8
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (18,27)
            elif self.state == 'fight':
                return (3,5)
    
    class Golem(Units):
        spritesheet = 9
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (6,11)
            elif self.state == 'fight':
                return (18,26)
    
    class Phoenix(Units):
        spritesheet = 10
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
    
    class WereWolf(Units):
        spritesheet = 11
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,6)
            elif self.state == 'fight':
                return (12,14)
    
    class DoppelSlime(Units):
        spritesheet = 12
        def __init__(self): 
            super().__init__(10,1,1,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (15,21)
            elif self.state == 'fight':
                return (9,18)
    
    class Slayer(Units):
        spritesheet = 13
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,35)
            elif self.state == 'fight':
                return (11,14)
    
    class Whale(Units):
        spritesheet = 14
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (36,45)
            elif self.state == 'fight':
                return (2,7)

    class Wyvern(Units):
        spritesheet = 15
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,8)
            elif self.state == 'fight':
                return (36,42)

    class Angel(Units):
        spritesheet = 16
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,9)
    
    class Boss(Units):
        spritesheet = 17
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,7)
    
    class Overmind(Units):
        spritesheet = 18
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (5,13)
            elif self.state == 'fight':
                return (4,7)
    
    class Spike(Units):
        spritesheet = 19
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,15)

################################################################################
# These are the functions for the game functionality and for your side of
# the game
################################################################################      
    def appStarted(self):        
        self.timerDelay = 1
        self.sheets = []
        self.background = self.loadImage('Assets/Backgrounds/background.png')
        self.age = 0   # current age
        self.enemyAge = 0
        self.exp = 0
        self.enemyExp = 0
        self.expCounter = 0
        self.alive = []   # all the ally units that are alive right now
        self.enemyAlive = []
        self.sprites = []   # contains all the frames of the units
        self.enemySprites = []
        self.enemySpriteCounters = []
        self.spriteCounters = []   # counters count the frame
        self.absLocation = []   # abs and rel locations used for scrolling purposes
        self.relLocation= []
        self.enemyAbsLocation = []
        self.enemyRelLocation = []
        self.icons = []   # image of the unit in the button 
        self.allyBase = self.Base(.05 * self.width, .05 * self.width)
        self.enemyBase = self.Base( 1.95 * self.width, 1.95 * self.width)
        self.baseSprites = []
        self.baseCounter = 0
        self.baseAnimate()
        self.costs = [200,250,]
        self.money = 1000
        self.enemyMoney = 1000
        self.giants = []
        self.giantSprites = []
        self.giantSpriteCounters = []
        self.giantSpawn()
        self.giantAnimate()
        self.projectileSprites = []
        self.enemyProjectileSprites = []
        self.projectiles = [] 
        self.enemyProjectiles = []
        self.projectilesAttack = []
        self.enemyProjectilesAttack = []
        self.projectileAbsLocation = []
        self.projectileRelLocation = []
        self.enemyProjectileAbsLocation = []
        self.enemyProjectileRelLocation = []
        self.iconLoader()  
              
    def keyPressed(self,event):
        # used for scrolling left and right
        # if a is pressed and your display window can still scroll left
        if event.key == 'a' and (self.allyBase.relPos < (.1  * self.width)):
            self.allyBase.relPos += self.width * .1
            self.enemyBase.relPos += self.width * .1
            for pos in range(len(self.relLocation)):
                self.relLocation[pos] += self.width * .1
            for pos in range(len(self.enemyRelLocation)):
                self.enemyRelLocation[pos] += self.width * .1
            for pos in range(len(self.projectileRelLocation)):
                self.projectileRelLocation[pos] += self.width * .1
            for pos in range(len(self.enemyProjectileRelLocation)):
                self.enemyProjectileRelLocation[pos] += self.width * .1
        # if d is pressed and your display window can still scroll right
        elif event.key == 'd' and (self.enemyBase.relPos > (.95 * self.width)):
            self.allyBase.relPos -= self.width * .1
            self.enemyBase.relPos -= self.width * .1
            for pos in range(len(self.relLocation)):
                self.relLocation[pos] -= self.width * .1
            for pos in range(len(self.enemyRelLocation)):
                self.enemyRelLocation[pos] -= self.width * .1
            for pos in range(len(self.projectileRelLocation)):
                self.projectileRelLocation[pos] -= self.width * .1
            for pos in range(len(self.enemyProjectileRelLocation)):
                self.enemyProjectileRelLocation[pos] -= self.width * .1

    def giantSpawn(self):
        giant = 'giant'
        giant = self.Giant()
        self.giants.append(giant)
        self.giantSpriteCounters.append(0)
        enemyGiant = 'enemyGiant' 
        enemyGiant = self.Giant()
        self.giants.append(enemyGiant)
        self.giantSpriteCounters.append(0)
    
    def giantAction(self):
        giant = self.giants[0]
        self.giantSpriteCounters[0] = (1 + self.giantSpriteCounters[0]) % len(self.giantSprites[giant.action()])
        if (len(self.enemyAlive) > 0):
            if 0 < self.dist(self.enemyAbsLocation[0], self.allyBase.absPos) <= giant.range:
                if giant.state != 'rangedFight':
                    giant.state = 'rangedFight'
                    self.giantSpriteCounters[0] = 0
            elif self.dist(self.enemyAbsLocation[0], self.allyBase.absPos) <= 0:
                if giant.state != 'meleeFight':
                    giant.state = 'meleeFight'
                    self.giantSpriteCounters[0] = 0
            else:
                if giant.state != 'idle':
                    giant.state = 'idle'
                    self.giantSpriteCounters[0] = 0
        elif giant.state != 'idle':
                giant.state = 'idle'
                self.giantSpriteCounters[0] = 0
    
    def enemyGiantAction(self):
        giant = self.giants[1]
        self.giantSpriteCounters[1] = (1 + self.giantSpriteCounters[1]) % len(self.giantSprites[giant.action()+ 1])
        if (len(self.alive) > 0):
            if 0 < self.dist(self.enemyBase.absPos, self.absLocation[0]) <= giant.range:
                if giant.state != 'rangedFight':
                    giant.state = 'rangedFight'
                    self.giantSpriteCounters[1] = 0
            elif self.dist(self.enemyBase.absPos, self.absLocation[0]) <= 0:
                if giant.state != 'meleeFight':
                    giant.state = 'meleeFight'
                    self.giantSpriteCounters[1] = 0
            else:
                if giant.state != 'idle':
                    giant.state = 'idle'
                    self.giantSpriteCounters[1] = 0
        elif giant.state != 'idle':
            giant.state = 'idle'
            self.giantSpriteCounters[1] = 0

    def drawGiants(self,canvas):
        giant = self.giants[0]
        canvas.create_image(self.allyBase.relPos + 50, .72 * self.height, \
            image=ImageTk.PhotoImage(self.giantSprites[giant.action()][self.giantSpriteCounters[0]]))
        enemyGiant = self.giants[1]
        canvas.create_image(self.enemyBase.relPos - 50, .72 * self.height, \
            image=ImageTk.PhotoImage(self.giantSprites[enemyGiant.action()+1][self.giantSpriteCounters[1]]))
    
    def giantFight(self):
        giant = self.giants[0]
        if giant.state == 'meleeFight':
                if (self.giantSpriteCounters[0] == len(self.giantSprites[giant.action()]) -1) and len(self.enemyAlive) > 0:
                    self.enemyAlive[0].health -= giant.attack
        elif giant.state == 'rangedFight':
                if (self.giantSpriteCounters[0] == len(self.giantSprites[giant.action()]) //2) and len(self.enemyAlive) > 0:
                    self.projectiles.append(self.giantSprites[0])
                    self.projectilesAttack.append(giant.attack)
                    self.projectileAbsLocation.append(self.allyBase.absPos + 50)
                    self.projectileRelLocation.append(self.allyBase.relPos + 50)
        enemyGiant = self.giants[1]
        if enemyGiant.state == 'meleeFight':
                if (self.giantSpriteCounters[1] == len(self.giantSprites[enemyGiant.action()]) -1) and len(self.alive) > 0:
                    self.alive[0].health -= enemyGiant.attack
        elif enemyGiant.state == 'rangedFight':
                if (self.giantSpriteCounters[1] == len(self.giantSprites[enemyGiant.action()]) //2) and len(self.alive) > 0:
                    self.enemyProjectiles.append(self.giantSprites[1])
                    self.enemyProjectilesAttack.append(enemyGiant.attack)
                    self.enemyProjectileAbsLocation.append(self.enemyBase.absPos - 50)
                    self.enemyProjectileRelLocation.append(self.enemyBase.relPos - 50)
                    
    # function for summoning a new unit                    
    def spawn(self,unit):
        self.alive.append(unit)
        self.spriteCounters.append(0)
        self.absLocation.append(self.allyBase.absPos)
        self.relLocation.append(self.allyBase.relPos)
        self.money -= unit.cost
        self.Animate()

    def enemySpawn(self,unit):
        self.enemyAlive.append(unit)
        self.enemySpriteCounters.append(0)
        self.enemyAbsLocation.append(self.enemyBase.absPos)
        self.enemyRelLocation.append(self.enemyBase.relPos)
        self.enemyMoney -= unit.cost
        self.enemyAnimate()  

    def fighting(self):
        for unit in range(len(self.alive)):
            if self.alive[unit].state == 'fight' and self.alive[unit].range == 0:
                if (self.spriteCounters[unit] == len(self.sprites[unit]) -1) and len(self.enemyAlive) > 0:
                    self.enemyAlive[0].health -= self.alive[unit].attack
            elif self.alive[unit].state == 'fight' and self.alive[unit].range > 0:
                if (self.enemySpriteCounters[unit] == len(self.enemySprites[unit]) // 2) and len(self.enemyAlive) > 0:
                    self.projectiles.append(self.projectileSprites[self.alive[unit].projectile])
                    self.projectilesAttack.append(self.alive[unit].attack)
                    self.projectileAbsLocation.append(self.absLocation[unit])
                    self.projectileRelLocation.append(self.relLocation[unit])
        for unit in range(len(self.enemyAlive)):
            if self.enemyAlive[unit].state == 'fight' and self.enemyAlive[unit].range == 0:
                if (self.enemySpriteCounters[unit] == len(self.enemySprites[unit])-1) and len(self.alive) > 0:
                        self.alive[0].health -= self.enemyAlive[unit].attack
            elif self.enemyAlive[unit].state == 'fight' and self.enemyAlive[unit].range > 0:
                if (self.enemySpriteCounters[unit] == len(self.enemySprites[unit]) // 2) and len(self.enemyAlive) > 0:
                    self.enemyProjectiles.append(self.enemyProjectileSprites[self.enemyAlive[unit].projectile])
                    self.enemyProjectilesAttack.append(self.enemyAlive[unit].attack)
                    self.enemyProjectileAbsLocation.append(self.enemyAbsLocation[unit])
                    self.enemyProjectileRelLocation.append(self.enemyRelLocation[unit])

    def death(self):
        if len(self.alive) > 0 and self.alive[0].health <= 0:
            self.enemyExp += self.alive[0].cost
            self.alive.pop(0)
            self.sprites.pop(0)
            self.spriteCounters.pop(0)
            self.absLocation.pop(0)
            self.relLocation.pop(0)
        if len(self.enemyAlive) > 0 and self.enemyAlive[0].health <= 0:
            self.exp += self.enemyAlive[0].cost
            self.enemyAlive.pop(0)
            self.enemySprites.pop(0)
            self.enemySpriteCounters.pop(0)
            self.enemyAbsLocation.pop(0)
            self.enemyRelLocation.pop(0)

    def mousePressed(self,event):
        if (.85 * self.height) <= event.y <= (.99 * self.height):
            #leftmost button
            if (.01 * self.width) <= event.x <= (.09 * self.width):
                if self.age == 0 and self.money >= self.costs[0]:
                    newBat = 'bat' + str(len(self.sprites))
                    newBat = self.Bat()
                    self.spawn(newBat)
                elif self.age == 1:
                    newAnubis = 'anubis'+ str(len(self.sprites))
                    newAnubis = self.Anubis()
                    self.spawn(newAnubis)
                elif self.age == 2:
                    newEarthworm = 'earthworm'+ str(len(self.sprites))
                    newEarthworm = self.EarthWorm()
                    self.spawn(newEarthworm)
                elif self.age == 3:
                    newDoppelSlime = 'doppelslime'+ str(len(self.sprites))
                    newDoppelSlime = self.DoppelSlime()
                    self.spawn(newDoppelSlime)
                elif self.age == 4:
                    newAngel = 'angel'+ str(len(self.sprites))
                    newAngel = self.Angel()
                    self.spawn(newAngel)
            # second button
            elif (.12 * self.width) <= event.x <= (.2 * self.width):
                if self.age == 0:
                    newOwl = 'owl' + str(len(self.sprites))
                    newOwl = self.Owl()
                    self.spawn(newOwl)
                elif self.age == 1:
                    newKnight = 'knight'+ str(len(self.sprites))
                    newKnight = self.Knight()
                    self.spawn(newKnight)
                elif self.age == 2:
                    newGolem = 'golem'+ str(len(self.sprites))
                    newGolem = self.Golem()
                    self.spawn(newGolem)
                elif self.age == 3:
                    newSlayer = 'slayer'+ str(len(self.sprites))
                    newSlayer = self.Slayer()
                    self.spawn(newSlayer)
                elif self.age == 4:
                    newBoss = 'boss'+ str(len(self.sprites))
                    newBoss = self.Boss()
                    self.spawn(newBoss)
            # third button
            elif (.23 * self.width) <= event.x <= (.31 * self.width):
                if self.age == 0:
                    newPeacock = 'peacock' + str(len(self.sprites))
                    newPeacock = self.Peacock()
                    self.spawn(newPeacock)
                elif self.age == 1:
                    newSlime = 'slime'+ str(len(self.sprites))
                    newSlime = self.Slime()
                    self.spawn(newSlime)
                elif self.age == 2:
                    newPhoenix = 'phoenix'+ str(len(self.sprites))
                    newPhoenix = self.Phoenix()
                    self.spawn(newPhoenix)
                elif self.age == 3:
                    newWhale = 'whale'+ str(len(self.sprites))
                    newWhale = self.Whale()
                    self.spawn(newWhale)
                elif self.age == 4:
                    newOvermind = 'overmind'+ str(len(self.sprites))
                    newOvermind = self.Overmind()
                    self.spawn(newOvermind)
            # fourth button
            elif (.34 * self.width) <= event.x <= (.42 * self.width):
                if self.age == 0:
                    newRat = 'rat' + str(len(self.sprites))
                    newRat = self.Rat()
                    self.spawn(newRat)
                elif self.age == 1:
                    newSpore = 'spore ' + str(len(self.sprites))
                    newSpore = self.Spore()
                    self.spawn(newSpore)
                elif self.age == 2:
                    newWerewolf = 'werewolf'+ str(len(self.sprites))
                    newWerewolf = self.WereWolf()
                    self.spawn(newWerewolf)
                elif self.age == 3:
                    newWyvern = 'wyvern'+ str(len(self.sprites))
                    newWyvern = self.Wyvern()
                    self.spawn(newWyvern)
                elif self.age == 4:
                    newSpike = 'spike'+ str(len(self.sprites))
                    newSpike = self.Spike()
                    self.spawn(newSpike)

    def evolving(self):
        self.expCounter += 1
        if self.exp >= 5000 and self.age < 5:
            self.age += 1
        if self.enemyExp >= 5000 and self.enemyAge < 5:
            self.age += 1
        if self.expCounter % 3 == 0:
            self.exp += 1
            self.enemyExp += 1
        
        
    # function creates the sprites for newly summoned units and updates the old sprites if they change action
    # modified version of the sprite animations at https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    def Animate(self):
        for count in range(len(self.alive)):
            unit = self.alive[count]
            pic = self.sheets[unit.spritesheet]
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9),\
                        512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 6)
                sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
                unitSprite.append(sprite)
            if count >= len(self.sprites):
                self.sprites.append(unitSprite)
            else:
                self.sprites[count] = unitSprite
    
    def enemyAnimate(self):
        for count in range(len(self.enemyAlive)):
            unit = self.enemyAlive[count]
            pic = self.sheets[unit.spritesheet]
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9),\
                        512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 6)
                unitSprite.append(sprite)
            if count >= len(self.enemySprites):
                self.enemySprites.append(unitSprite)
            else:
                self.enemySprites[count] = unitSprite

    def giantAnimate(self):
        giantPic = self.loadImage('Assets/Sprites/Defense/Giant.png')
        giantProjectile = self.loadImage('Assets/Sprites/Defense/Giant_Projectile.png')
        giantProjectile = self.scaleImage(giantProjectile, 3)
        self.giantSprites.append(giantProjectile)
        self.giantSprites.append(giantProjectile.transpose(Image.FLIP_LEFT_RIGHT))
        enemySprites = []
        sprites=[]
        for i in range(4):
            sprite = giantPic.crop((0 + 100 * i  , 0, 100 + 100 * i , 100))
            sprite = self.scaleImage(sprite, 3)
            enemySprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
            sprites.append(sprite)
            enemySprites.append(enemySprite)
        self.giantSprites.append(sprites)
        self.giantSprites.append(enemySprites)
        enemySprites = []
        sprites = []
        for i in range(9):
            sprite = giantPic.crop((0 + 100 * i  , 200, 100 + 100 * i , 300))
            sprite = self.scaleImage(sprite, 3)
            enemySprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
            sprites.append(sprite)
            enemySprites.append(enemySprite)
        self.giantSprites.append(sprites + sprites[::-1])
        self.giantSprites.append(enemySprites + enemySprites[::-1])
        enemySprites = []
        sprites = []
        for i in range(7):
            sprite = giantPic.crop((0 + 100 * i  , 400, 100 + 100 * i , 500))
            sprite = self.scaleImage(sprite, 3)
            enemySprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
            sprites.append(sprite)
            enemySprites.append(enemySprite)
        self.giantSprites.append(sprites)
        self.giantSprites.append(enemySprites)
        
    #similar to animate function above but for the two bases, no need to constantly update like above
    def baseAnimate(self):
        pic = self.loadImage("Assets/Backgrounds/allyPortal.png") 
        allyBaseSprites = []
        for i in range(4):
            sprite = pic.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4) 
            allyBaseSprites.append(sprite)   
        self.baseSprites.append(allyBaseSprites)    
        pic2 = self.loadImage("Assets/Backgrounds/enemyPortal.png")     
        enemyBaseSprites = []   
        for i in range(4):
            sprite = pic2.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4)  
            sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT) 
            enemyBaseSprites.append(sprite)
        self.baseSprites.append(enemyBaseSprites)

    def enemyAI(self):
        if (len(self.enemyAlive) < 5):
            num = random.randint(0,3)
            if self.enemyAge == 0:
                if num == 0:
                    newBat = 'bat' + str(len(self.enemySprites))
                    newBat = self.Bat()
                    self.enemySpawn(newBat)
                elif num == 1:
                    newOwl = 'owl'+ str(len(self.enemySprites))
                    newOwl = self.Owl() 
                    self.enemySpawn(newOwl)
                elif num == 2:
                    newPeacock = 'peacock'+ str(len(self.enemySprites))
                    newPeacock = self.Peacock()
                    self.enemySpawn(newPeacock)
                elif num == 3:
                    newRat = 'rat'+ str(len(self.sprites))
                    newRat = self.Rat()
                    self.enemySpawn(newRat) 

    # Loads and imports different images for the icons of the units and projectiles
    def iconLoader(self):
        path = 'Assets/Sprites'
        for folder in os.listdir(path):
            images = os.listdir(path + '/' + folder)
            for spritesheets in images:
                sheet = self.loadImage(path + '/' + folder + '/' + spritesheets)
                self.sheets.append(sheet)
                icon = sheet.crop((0,0,512,512))
                icon = sprite = self.scaleImage(icon, (self.height / 700 + self.width / 1400) / 12)
                self.icons.append(icon)
        path = 'Assets/Projectiles'
        for spritesheet in os.listdir(path):
            pic = self.loadImage (path + '/' + spritesheet)
            self.projectileSprites.append(pic)
            self.enemyProjectileSprites.append(pic.transpose(Image.FLIP_LEFT_RIGHT))

    # distance between two units
    def dist(self,x1,x2):
        return ( (x1 - 512 * ((self.height / 700 + self.width / 1400) / 12)) - \
            (x2 + 512 * ((self.height / 700 + self.width / 1400) / 12))   )

    def movement(self):
        for unit in range(len(self.alive)):
            self.spriteCounters[unit] = (1 + self.spriteCounters[unit]) % len(self.sprites[unit])
            # makes sure units don't overlap 
            if unit == 0:
                if (len(self.enemyAlive) > 0):
                    if self.dist(self.enemyAbsLocation[0], self.absLocation[0]) <= self.alive[0].range:
                        if self.alive[0].state == 'walk':
                            self.alive[0].state = 'fight'
                            self.spriteCounters[0] = 0
                            self.Animate()
                    else:
                        if self.alive[0].state == 'fight':
                            self.alive[0].state = 'walk'
                            self.spriteCounters[0] = 0
                            self.Animate()
                    if (self.dist(self.enemyAbsLocation[0], self.absLocation[0]) >= 0):
                        self.absLocation[0] += self.alive[0].moveSpeed
                        self.relLocation[0] += self.alive[0].moveSpeed
                elif (self.dist(self.enemyBase.absPos, self.absLocation[0]) > 0):
                    if self.alive[0] != 'walk':
                        self.alive[0].state = 'walk'
                        self.Animate()
                    self.absLocation[0] += self.alive[0].moveSpeed
                    self.relLocation[0] += self.alive[0].moveSpeed
            else:
                if (len(self.enemyAlive) > 0):
                    if (self.dist(self.enemyAbsLocation[0], self.absLocation[unit]) <= self.alive[unit].range):
                        if self.alive[unit].state == 'walk':
                            self.alive[unit].state = 'fight'
                            self.spriteCounters[unit] = 0
                            self.Animate()
                    if (self.dist(self.absLocation[unit-1],self.absLocation[unit]) > self.alive[unit].moveSpeed):
                        self.absLocation[unit] += self.alive[unit].moveSpeed
                        self.relLocation[unit] += self.alive[unit].moveSpeed
                else:
                    if self.alive[unit].state == 'fight':
                        self.alive[unit].state = 'walk'
                        self.spriteCounters[unit] = 0
                        self.Animate()
                    if (self.dist(self.absLocation[unit-1],self.absLocation[unit]) > self.alive[unit].moveSpeed):
                        self.absLocation[unit] += self.alive[unit].moveSpeed
                        self.relLocation[unit] += self.alive[unit].moveSpeed
        for unit in range(len(self.enemyAlive)):
            self.enemySpriteCounters[unit] = (1 + self.enemySpriteCounters[unit]) % len(self.enemySprites[unit])
            if unit == 0: 
                if (len(self.alive) > 0):
                    if (self.dist(self.enemyAbsLocation[0], self.absLocation[0]) <= self.enemyAlive[0].range):
                        if self.enemyAlive[0].state == 'walk':
                            self.enemyAlive[0].state = 'fight'
                            self.enemySpriteCounters[0] = 0
                            self.enemyAnimate()
                    else:
                        if self.enemyAlive[0].state == 'fight':
                            self.enemyAlive[0].state = 'walk'
                            self.enemySpriteCounters[0] = 0
                            self.Animate()
                        if (self.dist(self.enemyAbsLocation[0], self.absLocation[0],) >= 0):
                            self.enemyAbsLocation[0] -= self.enemyAlive[0].moveSpeed
                            self.enemyRelLocation[0] -= self.enemyAlive[0].moveSpeed
                elif (self.dist(self.enemyAbsLocation[0], self.allyBase.absPos)) > 0:
                    if self.enemyAlive[0].state != 'walk':
                        self.enemyAlive[0].state = 'walk'
                        self.enemyAnimate()
                    self.enemyAbsLocation[0] -= self.enemyAlive[0].moveSpeed
                    self.enemyRelLocation[0] -= self.enemyAlive[0].moveSpeed
            else:
                if (len(self.alive) > 0):
                    if (self.dist(self.enemyAbsLocation[unit], self.absLocation[0]) <= self.enemyAlive[unit].range):
                        if self.enemyAlive[unit].state == 'walk':
                            self.enemyAlive[unit].state = 'fight'
                            self.enemySpriteCounters[unit] = 0
                            self.enemyAnimate()
                    if (self.dist(self.enemyAbsLocation[unit],self.enemyAbsLocation[unit-1]) > self.enemyAlive[unit].moveSpeed):
                        self.enemyAbsLocation[unit] -= self.enemyAlive[unit].moveSpeed
                        self.enemyRelLocation[unit] -= self.enemyAlive[unit].moveSpeed
                else:
                    if self.enemyAlive[unit].state == 'fight':
                            self.enemyAlive[unit].state = 'walk'
                            self.enemySpriteCounters[unit] = 0
                            self.enemyAnimate() 
                    if (self.dist(self.enemyAbsLocation[unit],self.enemyAbsLocation[unit-1]) > self.enemyAlive[unit].moveSpeed):
                        self.enemyAbsLocation[unit] -= self.enemyAlive[unit].moveSpeed
                        self.enemyRelLocation[unit] -= self.enemyAlive[unit].moveSpeed
    
    def projectileMovement(self):
        index = 0
        while index < len(self.projectiles):
            if len(self.enemyAlive) > 0 and self.dist(self.enemyAbsLocation[0],self.projectileAbsLocation[index]) < 25:
                self.enemyAlive[0].health -= self.projectilesAttack[index]
                self.projectilesAttack.pop(index)
                self.projectileAbsLocation.pop(index)
                self.projectileRelLocation.pop(index)
                self.projectiles.pop(index)
            else:
                self.projectileAbsLocation[index] += 25
                self.projectileRelLocation[index] += 25
                index += 1
        index = 0
        while index < len(self.enemyProjectiles):
            if len(self.alive) > 0 and self.dist(self.enemyProjectileAbsLocation[index],self.absLocation[0]) < 25:
                self.alive[0].health -= self.enemyProjectilesAttack[index]
                self.enemyProjectilesAttack.pop(index)
                self.enemyProjectileAbsLocation.pop(index)
                self.enemyProjectileRelLocation.pop(index)
                self.enemyProjectiles.pop(index)
            else:
                self.enemyProjectileAbsLocation[index] -= 25
                self.enemyProjectileRelLocation[index] -= 25
                index += 1
        
    def timerFired(self):
        self.background = self.background.resize((self.width,self.height))
        self.evolving()
        self.giantAction()
        self.enemyGiantAction()
        self.enemyAI()
        self.death()
        self.projectileMovement()
        self.fighting()
        self.giantFight()
        self.movement()
        self.baseCounter = (1 + self.baseCounter) % 3
        self.money += 1
        self.enemyMoney += 1
        
    # instructions for drawing the UI
    def interface(self,canvas): 
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.background))
        # this draws the buttons for summoning the unit
        for unit in range(4):
            canvas.create_rectangle((.01 + .11 * unit) * self.width, .85 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "Teal")
            canvas.create_image((.05 + .11 * unit) * self.width, .88 * self.height, image = ImageTk.PhotoImage(self.icons[4 * self.age + unit]))
            canvas.create_rectangle((.01  + .11 * unit) * self.width, .95 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "White")
        # this draws the evolve button     
        if self.age < 5:
            canvas.create_rectangle(.75 * self.width, .05 * self.height, .85 * self.width, .15 * self.height, fill = "White" )
            canvas.create_rectangle(.75 * self.width, .05 * self.height, .75 * self.width + (self.exp / 5000) * (.1 * self.width), .15 * self.height, fill = "lightblue")
            canvas.create_text(.8 * self.width, .1 * self.height, text = f'{self.exp} / 5000 EXP', font = 'Helvetica 12 bold')
        canvas.create_text(.05 * self.width, .1 * self.height, text = f'${self.money}', font = "Helvetica 25 bold")  

    def drawHealthbars(self,canvas):
        for sprite in range(len(self.alive)):
            unit = self.alive[sprite]
            pos = self.relLocation[sprite]
            canvas.create_rectangle(pos-25, .66 * self.height, pos + 25, .67 * self.height, fill = "white")
            canvas.create_rectangle(pos-25, .66 * self.height, pos - 25 + (50 * (unit.health / unit.maxHealth)), .67 * self.height, fill = "green")
        for sprite in range(len(self.enemyAlive)):
            unit = self.enemyAlive[sprite]
            pos = self.enemyRelLocation[sprite]
            canvas.create_rectangle(pos-25, .66 * self.height, pos + 25, .67 * self.height, fill = "white")
            canvas.create_rectangle(pos-25, .66 * self.height, pos - 25 + (50 * (unit.health / unit.maxHealth)), .67 * self.height, fill = "green")

    def drawSprites(self,canvas):
        for sprite in range(len(self.sprites)):
            unit = self.sprites[sprite]
            canvas.create_image(self.relLocation[sprite], .72 * self.height, \
                image=ImageTk.PhotoImage(unit[self.spriteCounters[sprite]]))
        for sprite in range(len(self.enemySprites)):
            unit = self.enemySprites[sprite]
            canvas.create_image(self.enemyRelLocation[sprite], .72 * self.height, \
                image=ImageTk.PhotoImage(unit[self.enemySpriteCounters[sprite]]))

    def drawProjectiles(self,canvas):
        for count in range(len(self.projectiles)):
            canvas.create_image(self.projectileRelLocation[count], .72 * self.height, \
                image=ImageTk.PhotoImage(self.projectiles[count]))
        for i in range(len(self.enemyProjectiles)):
            canvas.create_image(self.enemyProjectileRelLocation[i], .75 * self.height, \
                image=ImageTk.PhotoImage(self.enemyProjectiles[i]))

    def drawBases(self,canvas):
        canvas.create_image(self.allyBase.relPos, .68 * self.height, \
            image=ImageTk.PhotoImage(self.baseSprites[0][self.baseCounter]))
        canvas.create_image(self.enemyBase.relPos, .68 * self.height, \
            image=ImageTk.PhotoImage(self.baseSprites[1][self.baseCounter]))

    def redrawAll(self,canvas):
        self.interface(canvas)
        self.drawGiants(canvas)
        self.drawBases(canvas)
        self.drawSprites(canvas)
        self.drawProjectiles(canvas)
        self.drawHealthbars(canvas)
                        
MyApp(width=1400, height=700)