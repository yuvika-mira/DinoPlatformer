import pygame as pg


#define game variables
ts = 50 #størrelse på tiles

#jungel platformer
jordImg = pg.image.load("bilder/lavabakgrunn/jord.png")
steinImg = pg.image.load("bilder/lavabakgrunn/stein.png")
            

class Platformer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        r = 0
        for rad in data:
            k = 0
            for tile in rad: 
                if tile == 1:
                    img = pg.transform.scale(steinImg, (ts, ts))
                    imgRect = img.get_rect()
                    imgRect.x = k * ts
                    imgRect.y = r * ts
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                    
                if tile == 2:
                    img = pg.transform.scale(jordImg, (ts, ts))
                    imgRect = img.get_rect()
                    imgRect.x = k * ts
                    imgRect.y = r * ts
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                
                if tile == 3:
                    lava = Lava(k*ts, r*ts)
                    lava_group.add(lava)
                    #appender ikke til tile list fordi da ville spillerene kunne kolidert som med platformer
                
                if tile == 4:
                    spike = Monster(k*ts, r*ts + 12)
                    spike_group.add(spike)
                    
                    
                k += 1
            r += 1

    def draw(self, surface):
        for tile in self.tile_list:
            surface.blit(tile[0], tile[1])
           # pg.draw.rect(surface, (255,0,0), tile[1], 2)

#henter klassen sprite som er i pygame systemet, der finnes allerede sprite, kan bruke group
class Monster(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        #viktig at det er self.image slik at sprite klassen kan lese det av til draw
        self.image = pg.image.load("bilder/jungelbakgrunn/spike.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.marginer = 1
        self.teller = 0
        
    def update(self, surface):
        self.rect.x += self.marginer
        self.teller +=1
        if self.teller > ts*2:
            #minus fordi da bytter den retning, posetiv retning blir negativ og negativ blir posetiv
            self.marginer *= -1
            self.teller = 0
            
        
        surface.blit(self.image, self.rect)
        

spike_group = pg.sprite.Group()

class Lava(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        lavaImg = pg.image.load("bilder/lavabakgrunn/lava.png")
        self.image = pg.transform.scale(lavaImg, (ts, ts))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
lava_group = pg.sprite.Group()

lavaData = [ 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

platformer = Platformer(lavaData)
