"""
KILDE TIL MYNTER: author: Puddin - https://opengameart.org/content/rotating-coinhttps://opengameart.org/content/rotating-coin , lisensen gir oss tillatelse til å bruke den som vi ønsker

Kilde til gridbakgrunn, author: coding with russ, link: https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=1
Kilde til kollisjoner, author: coding with russ, link: https://www.youtube.com/watch?v=BHr9jxKithk
Kilder til knapper, author: coding with russ, link: https://www.youtube.com/watch?v=G8MYGDf_9ho&t=965s

Kilder til Platformer:
Ørken, author: Tio Aimar, link: https://opengameart.org/content/2d-platformer-desert-pack
Jungel, author: Tio Aimar, link: https://opengameart.org/content/2d-platformer-jungle-pack
Vinter, author: Tio Aimar, link: https://opengameart.org/content/2d-platformer-snow-pack
Lava, author: Tio Aimar, link: https://opengameart.org/content/2d-platformer-volcano-pack-11 

Karakterer:
Dinosaurer, author: ScissorMarks , link: https://arks.itch.io/dino-characters
Monstere/Spikes, author: Bevouliin, link: https://opengameart.org/content/bevouliin-free-ingame-items-spike-monsters #Knapp bilder: Rebecca Tønjum
inspirasjon til karakterer: https://www.youtube.com/watch?v=UdsNBIzsmlI , https://www.youtube.com/watch?v=B6DrRN5z_uU
"""


import pygame as pg
from pygame.locals import *
import random
import time

import jungellevel
import snowlevel
import lavalevel
import orkenlevel


WIDTH = 1200
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (245, 110, 110)
GREEN = (121, 227, 109)
BLUE = (110, 110, 245)
transparent = (0, 0, 0, 0)

score1 = 0
score2 = 0
FPS = 60
ts = 50
img_size = (55, 55)

instruks1 = 'rød dinosaur - piltaster til bevegelse, hopp med opp tast'
instruks2 = 'blå dinosaur - bruk A, D til å bevegelse og W til å hoppe'
instruks3 = 'MÅL: førstemann til å samle 10 mynter!'
instruks4 = 'Ikke treff lavaen og monstrene, da mister du penger! - Lykke til'


bgImg = "bgImgJungel"


pg.init()

clock = pg.time.Clock()

surface = pg.display.set_mode(SIZE)
pg.display.set_caption("Mira og Rebecca sitt spill")

       
#laster inn knapp bilder
vinterK = pg.image.load("bilder/knapper/vinterKnapp.png")
orkenK = pg.image.load("bilder/knapper/ørkenKnapp.png")
jungelK = pg.image.load("bilder/knapper/jungelKnapp.png")
lavaK = pg.image.load("bilder/knapper/lavaKnapp.png")
instK = pg.image.load("bilder/knapper/instKnapp.png")
backK = pg.image.load("bilder/knapper/backKnapp.png")



sunImg = pg.image.load("bilder/jungelbakgrunn/sun.png")
sunImg = pg.transform.scale(sunImg, (ts, ts))
#bakgrunnbilder
bgImgJungel = pg.image.load("bilder/jungelbakgrunn/bg_jungle.png")
bgImgSne = pg.image.load("bilder/snowbakgrunn/bg_snow.png")
bgImgLava = pg.image.load("bilder/lavabakgrunn/bg_volcano.png")
bgImgØrk = pg.image.load("bilder/sandbakgrunn/bg_desert.png")


#BILDER TIL BLÅ DINO
walkHoyre = [pg.image.load('bilder/dino/blå/run1.png'), pg.image.load('bilder/dino/blå/run2.png'), pg.image.load('bilder/dino/blå/run3.png'), pg.image.load('bilder/dino/blå/run4.png'), pg.image.load('bilder/dino/blå/run5.png'), pg.image.load('bilder/dino/blå/run6.png'), pg.image.load('bilder/dino/blå/run7.png')]
walkVenstre = [pg.image.load('bilder/dino/blå/run1.png'), pg.image.load('bilder/dino/blå/run2.png'), pg.image.load('bilder/dino/blå/run3.png'), pg.image.load('bilder/dino/blå/run4.png'), pg.image.load('bilder/dino/blå/run5.png'), pg.image.load('bilder/dino/blå/run6.png'), pg.image.load('bilder/dino/blå/run7.png')]
standing = pg.image.load('bilder/dino/blå/stille.png')
hurt = pg.image.load("bilder/dino/blå/hurt.png")

#BILDER TIL RØD DINO
walkRight = [pg.image.load('bilder/dino/rød/run1.png'), pg.image.load('bilder/dino/rød/run2.png'), pg.image.load('bilder/dino/rød/run3.png'), pg.image.load('bilder/dino/rød/run4.png'), pg.image.load('bilder/dino/rød/run5.png'), pg.image.load('bilder/dino/rød/run6.png'), pg.image.load('bilder/dino/rød/run7.png')]
walkLeft = [pg.image.load('bilder/dino/rød/run1.png'), pg.image.load('bilder/dino/rød/run2.png'), pg.image.load('bilder/dino/rød/run3.png'), pg.image.load('bilder/dino/rød/run4.png'), pg.image.load('bilder/dino/rød/run5.png'), pg.image.load('bilder/dino/rød/run6.png'), pg.image.load('bilder/dino/rød/run7.png')]
stille = pg.image.load('bilder/dino/rød/stille.png')
skadet = [pg.image.load("bilder/dino/rød/hurt.png"), pg.image.load('bilder/dino/rød/stille.png'), pg.image.load("bilder/dino/rød/hurt.png"), pg.image.load('bilder/dino/rød/stille.png'), pg.image.load("bilder/dino/rød/hurt.png"), pg.image.load('bilder/dino/rød/stille.png')]


#bildet til mynt
coinImg = pg.image.load('bilder/coins/coin_0.png')

#lyder
coinCollect = pg.mixer.Sound("sounds/coincollect.mp3")
winner = pg.mixer.Sound("sounds/winner.mp3")
hitSound = pg.mixer.Sound("sounds/hit.mp3")





class Knapp():
    def __init__(self, x, y, image, scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pg.transform.scale(image, (int(w *scale),int(h*scale)))
        self.rect = self.image.get_rect()
        #plasserer rect der vi vil ha den
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        trykk = False
        #finner posisjonen til musen
        pos = pg.mouse.get_pos()
        #check mouse over and click [0] betyr venstre klikk
        if self.rect.collidepoint(pos) and pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            trykk = True
            
        #resetter knappetrykk
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #draw button    
        surface.blit(self.image, (self.rect.x, self.rect.y))
            
        return trykk
        #slik at vi kan bruke knappetrykk i funksjoner seinere
        
        
vinter = Knapp(250, 300, vinterK, 1)
orken = Knapp(650, 300, orkenK, 1)
jungel = Knapp(250, 450, jungelK, 1)
lava = Knapp(650, 450, lavaK, 1)
inst = Knapp(450, 100, instK, 1)
back = Knapp(900, 140, backK, 0.75)





class Character():
    def __init__(self, x, y, image, right, left):
        self.image = image
        self.image = pg.transform.scale(self.image, img_size)
        self.right = right
        self.left = left
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.vy = 0 #konstant som brukes til tyngdekraften
        self.dx = 0
        self.dy = 0
        
        self.animation_count = 0
        self.fall_count = 0
        self.walkCount = 0
        
        self.speed = 5
        self.jumpCount = 0
        
        self.isHurt = False
        

    def update(self):
    
        self.dy = 0
        
        #tyngdekraft
        self.vy += 2
        self.dy += self.vy

        #kollisjoner med platformer
        for tile in level.platformer.tile_list:
            
            #kollisjoner i x retning
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.w, self.h):
                self.dx = 0
                
            #kollisjoner i y retning
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.w, self.h):
                #kollisjon ovenifra, fek hodet til karateren kræsjer i noe
                if self.vy < 0: #når bevegelse i y retning er neagtiv = oppover på skjermen
                    self.dy = tile[1].bottom - self.rect.top
                    self.vy = 0 #slik at det blir realistisk fall
                    
                #kollisjoner nedifra, fek beina på en platform
                elif self.vy >= 0: #når bevegelse i y retning er posetiv = nedover på skjermen
                    self.dy = tile[1].top - self.rect.bottom
                    #self.rect.y = tile[1].top - self.h
                    self.vy = 0 # realistisk fall
      
        
        #oppdaterer spiller sin plassering
        self.rect.x += self.dx
        self.rect.y += self.dy

        #slik at karakteren ikke faller ut av skjermen, kan være relevant for lava?
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.dy = 0

        
        if self.isHurt == True:
            surface.blit(pg.image.load("bilder/dino/rød/hurt.png"), self.rect)
        else:
            surface.blit(self.image, self.rect)



    def jump(self):
        self.vy = -20
        self.jumpCount += 1
        """
        if self.jumpCount == 4:
            self.jumpCount = 0
            self.vy = 20
        """
        
    def kollisjon(self):
        #kollisjon med høyre vegg
        if self.rect.x + self.rect.width >= WIDTH:
            self.rect.x = WIDTH - self.rect.width
                
    #kollisjon med venstre vegg
        if self.rect.x <= 0:
            self.rect.x = 10



class Player1(Character):
    def __init__(self, x, y, image, right, left):
        super().__init__(x, y, image, right, left)
        
        
        self.tStart = pg.time.get_ticks() - 3000
    
    def move(self):
        self.dx = 0
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.dx = -self.speed
            
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
                
            self.walkCount += 1


            self.image = self.left[self.walkCount//3]
            self.image = pg.transform.scale(self.image, img_size)        
            self.image = pg.transform.flip(self.image, True, False)
            
        if keys[pg.K_RIGHT]:
            self.dx = self.speed
            
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
                
            self.walkCount += 1


            self.image = self.left[self.walkCount//3]
            self.image = pg.transform.scale(self.image, img_size)        
            self.image = pg.transform.flip(self.image, False, False)
            
            
            


            #surface.blit(self.l, (self.rect.x, self.rect.y))


class Player2(Character):
    def __init__(self, x, y, image, right, left):
        super().__init__(x, y, image, right, left)
        
        self.tStart = pg.time.get_ticks() - 3000 
    
    def move(self):
        self.dx = 0
        
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.dx = -self.speed
            
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
                
            self.walkCount += 1


            self.image = self.left[self.walkCount//3]
            self.image = pg.transform.scale(self.image, img_size)        
            self.image = pg.transform.flip(self.image, True, False)
            
        if keys[pg.K_d]:
            self.dx = self.speed
            
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
                
            self.walkCount += 1


            self.image = self.left[self.walkCount//3]
            self.image = pg.transform.scale(self.image, img_size)        
            self.image = pg.transform.flip(self.image, False, False)


            #surface.blit(self.l, (self.rect.x, self.rect.y))
    

         
def tegnTekst(tekst, x, y, farge, fontSize):
    #henter font
    font = pg.font.SysFont('Arial', fontSize)
    
    #laget et tekstbilde
    textImg = font.render(tekst, True, farge)
    

    #putter x,y i midten av rektangelet 
    surface.blit(textImg, (x, y))         



def tegnScore():
   
    font = pg.font.SysFont('Arial', 20)
    
    scoreR = font.render(f'score rød dino:{score1}', True, BLACK) 
    surface.blit(scoreR, (900, 50))#kordinatpareet viser hvor rektangelboksen har kordinater
    
    #henter
    scoreB = font.render(f'score blå dino:{score2}', True, BLACK)
    surface.blit(scoreB, (200, 50))
    


playSound = True

def nyttSpill():
    global playSound, gamePaused

    if score1 >= 10:
        gameOver = True
        surface.fill(BLUE)
        tegnTekst('RØD DINOSAUR VANT!', 320, 200, WHITE, 40)
        tegnTekst('Gratulerer, avslutt spillet for å begynne på nytt!', 180, 300, BLACK, 40)
        if playSound:
            winner.play()
            playSound = False
        
        
    elif score2 >= 10:
        gameOver = True
        surface.fill(BLUE)
        if playSound:
            winner.play()
            playSound = False
        tegnTekst('BLÅ DINOSAUR VANT!', 320, 200, WHITE, 40)
        tegnTekst('Gratulerer, avslutt spillet for å begynne på nytt!', 180, 300, BLACK, 40)
        

"""      
def hurt(player, score):
            if pg.time.get_ticks() - player.tStart > 3000:
                score -= 5
                #player.isHurt = True
                player.tStart = pg.time.get_ticks()
       
        if pg.sprite.spritecollide(player, spike_group, False):
            if pg.time.get_ticks() - player1.tStart > 3000:
                score -= 5
                player.isHurt = True
                player.tStart = pg.time.get_ticks()
                
        player.isHurt = False
        
"""


def monsterKollisjon():
    hurt  = 0
    
    global score1, score2
    
    if pg.sprite.spritecollide(player1, level.spike_group, False):
        if pg.time.get_ticks() - player1.tStart > 3000:
            score1 -= 5
        
            """
            if hurt + 1 >= 21:
                hurt = 0
                
            hurt += 1
            
            image = skadet[hurt//3]
            image = pg.transform.scale(image, img_size)        

            surface.blit(image, player1.rect)
            """
            
            player1.tStart = pg.time.get_ticks()
            hitSound.play()

    if pg.sprite.spritecollide(player1, level.lava_group, False):
        if pg.time.get_ticks() - player1.tStart > 3000:
            score1 -= 5
            player1.tStart = pg.time.get_ticks()
            hitSound.play()

                
    if pg.sprite.spritecollide(player2, level.spike_group, False):
        if pg.time.get_ticks() - player2.tStart > 3000:
            score2 -= 5
            player2.tStart = pg.time.get_ticks()
            hitSound.play()

    if pg.sprite.spritecollide(player2, level.lava_group, False):
        if pg.time.get_ticks() - player2.tStart > 3000:
            score2 -= 5
            player2.tStart = pg.time.get_ticks()       
            hitSound.play()









coins = []
   
def Nymynt():
    global coins
    for i in range(10):
        x = random.randint(20, 1200)
        y = random.randint(20, 500)
        s = pg.Rect(x, y, 23, 23)
        coins.append(s)



player1 = Player1(1000, 600, stille, walkRight, walkLeft)
player2 = Player2(200, 600, standing, walkHoyre, walkVenstre)





Nymynt()

t1 = time.time()

gameOver = True
gamePaused = False


run = True
while run:
    
    clock.tick(FPS)

    t2 = time.time()
    dt = t2 - t1
    
    
        
#MAIN MENU
    if gamePaused == False:
        surface.fill(RED)
        tegnTekst("VELG ET LEVEL FOR Å STARTE", 300, 225, WHITE, 40)
        if vinter.draw() == True:
            gameOver = False
            bgImg = bgImgSne
            
        if lava.draw() == True:
            gameOver = False
            bgImg = bgImgLava
            
        if orken.draw() == True:
            gameOver = False
            bgImg = bgImgØrk
            
        if jungel.draw() == True:
            gameOver = False
            bgImg = bgImgJungel
            
        if inst.draw() == True:
            gamePaused = True
        
    #instrukser side
    if gamePaused == True:
        surface.fill(RED)
        instrukser1 = tegnTekst(instruks1, 100, 100, WHITE, 30)
        instrukser1 = tegnTekst(instruks2, 100, 200, WHITE, 30)
        instrukser3 = tegnTekst(instruks3, 250, 350, BLACK, 30)
        instrukser4 = tegnTekst(instruks4, 100, 400, BLACK, 30)
        instrukser4 = tegnTekst('trykk SPACE for pause!', 400, 500, WHITE, 30)

        if back.draw() == True:
            gamePaused = False

        
    if len(coins) > 20:
        for i in range(6):
            coins.pop(i)
            i += 1
            
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
          
        if event.type == pg.KEYDOWN:
            #sjekker om vi trykker på spacebar
            if event.key == pg.K_UP:
                #om dette skjer skal character hoppe
                player1.jump()
                    
            if event.key == pg.K_w:
                #om dette skjer skal character hoppe
                player2.jump()
            

            if event.key == pg.K_SPACE:
                if gameOver == False:
                    gameOver = True
                    


                
    if bgImg == bgImgSne:
        level = snowlevel
    if bgImg == bgImgJungel:
        level = jungellevel
    if bgImg == bgImgØrk:
        level = orkenlevel
    if bgImg == bgImgLava:
        level = lavalevel

    if gameOver == False:
        
        
        if dt >= 10.00:
            t1 = time.time()
            # Lager ny mynter
            Nymynt()
        
                    
        surface.blit(bgImg, (0, 0))
        surface.blit(sunImg, (100, 100))
        level.platformer.draw(surface)
    
    #    player.update()
    #    grid()

        #sjekker om noen mynter har blitt collected
        player1_rect = pg.Rect(player1.rect.x, player1.rect.y, player1.rect.width, player1.rect.height)
        player2_rect = pg.Rect(player2.rect.x, player2.rect.y, player2.rect.width, player2.rect.height)

    
        
        for c in coins: #om en mynt c
            surface.blit(coinImg, (c[0], c[1]))

            if c.colliderect(player1_rect): #hvis karakteren kolliderer med myntene 
                coins.remove(c) #så fjernes den mynten
                score1 += 1
                coinCollect.play()
            if c.colliderect(player2_rect):
                coins.remove(c) #så fjernes den mynten
                score2 += 1
                coinCollect.play()
                
                
        #kollisjoner med lava og monster
        monsterKollisjon()

        
        player1.move()
        player1.kollisjon()
        player1.update()

        
        player2.move()
        player2.kollisjon()
        player2.update()
        
        
        level.spike_group.update(surface)
        level.lava_group.draw(surface)
        

        tegnScore()
    nyttSpill()
    


    pg.display.flip()

pg.quit()


