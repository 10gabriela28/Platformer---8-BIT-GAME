#Importing the libraries we'll use for this game.
import pygame
import math
from pygame import mixer
pygame.init()
mixer.init()



#Setting the game's display up.
WIDTH, HEIGHT = 829, 618
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Platformer")
ICON = pygame.image.load("icon.png")
pygame.display.set_icon(ICON)
BG = pygame.image.load("gamebg.png")
Win_Condition = False


#Importing the background music.
#mixer.music.load('bgmusic.mp3')
#mixer.music.set_volume(0.2)
#mixer.music.play()


#Importing the fighter we'll be playing with and its current available animations.
fighter = pygame.image.load("Troy.png")
fighter_walk_images = pygame.image.load("Troy.png")
velocity = 15



#Importing the fighter's profile
font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 25)
profile = pygame.image.load("profilewip.png")
score = "+100"
finalscore = font.render(score, True, (0, 0, 0))



#Importing the fighter's enemy's design.
#Goblin (Inspired by World//Zero)
goblin = pygame.image.load("slingshot goblin.png")


#Importing the winning message :D
font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 40)
message = "You did it! :D"
winningmessage = font.render(message, True, (0, 0, 0))

#Importing the losing message :(
font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 40)
oops = "Oops, you lost. :("
youlost = font.render(oops, True, (0, 0, 0))



#Importing the song credits.
font = pygame.font.Font("PixeloidSans-mLxMm.ttf", 10)
credits = "SONG NAME - 8 BIT RPG BATTLE - Retro Game Music | No Copyright Music"
songcredits = font.render(credits, True, (0, 0, 0))

#Adding the background into the game.
def draw():
    DISPLAY.blit(BG,(0, 0))

#Adding the fighter's profile.
def add_profile_at_location(a, b):
    DISPLAY.blit(pygame.transform.scale(profile, (460, 150)), (a, b))

#Adding the playable and non-playable characters.
def add_fighter_at_location(a, b):
    DISPLAY.blit(pygame.transform.scale(fighter, (180,180)), (a, b))

def add_goblin_at_location(a, b):
    DISPLAY.blit(pygame.transform.scale(goblin, (178, 178)), (a, b))


#Setting up the fighter.
class Player:
    def __init__(self, a, b, width, height):
        self.a = a
        self.b = b
        self.mask = 0
        self.width = width
        self.height = height
        self.projectiles = []

    def shoot(self):
        projectile = Projectile(self.a + self.width, self.b + self.height/2)
        self.projectiles.append(projectile)

    def main(self, DISPLAY):
        DISPLAY.blit(pygame.transform.scale(fighter_walk_images, (120, 120)), (self.a, self.b))
        


#The player's scale and coordinates.
Player.a = 130
Player.b = 280
player = Player(130, 280, 180, 180)



class Goblin:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

#The goblin's coordinates.
Goblin.a = 500
Goblin.b = 300



class Projectile:
    def __init__(self, a, b, speed=10):
        self.a = a
        self.b = b
        self.speed = speed
        self.image = pygame.image.load("charge.png")
    
    def move(self):
        self.a += self.speed
        
    def draw(self, display):
        DISPLAY.blit(self.image, (self.a, self.b))
        
projectiles = []


def main():
    
    run = True
    
    while run:
        
        CLOCK.tick(FPS)

        #Displaying the profile into the game.
        add_profile_at_location(0, 0)

        #Displaying the playable and non-playable characters.
        add_fighter_at_location(Player.a, Player.b)
        add_goblin_at_location(Goblin.a, Goblin.b)

        #Getting the playable character to shoot.
        for projectile in projectiles:
            projectile.draw(DISPLAY)
            projectile.move()
            if projectile.a > Goblin.a:
                    projectiles.remove(projectile)

        pygame.display.update()

        add_goblin_at_location(Goblin.a, Goblin.b)
        #Getting the goblin to walk (Kind of.)
        Goblin.a = Goblin.a + 0.8 * math.sin(3 * CLOCK.tick(FPS))
        
        #Getting the character to walk and shoot.
        player.main(DISPLAY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            Player.a -= velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            Player.a += velocity
        if keys[pygame.K_i]:
            projectile = Projectile(Player.a + 80, Player.b + 60)
            projectiles.append(projectile)
            for projectile in projectiles:
                if projectile.a > WIDTH:
                    projectiles.remove(projectile)
        
        
                        
    # If the player gets in contact with the goblin, the game is over.
        if(Player.a + 177 > Goblin.a):
            Player.a = -1000
            Player.b = -1000
            
                    
        else:
        # Getting the charge to be effective against the goblin.
            for projectile in projectiles:
                if (projectile.a > Goblin.a and projectile.a < Goblin.a + 178 and projectile.b > Goblin.b and projectile.b < Goblin.b + 178):
                    projectiles.remove(projectile)
                    Goblin.a = -1000
                    Goblin.b = -1000
                    Win_Condition = True
                
            

        #Keeping the game running.
        for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False
                    break
        
        draw()
        DISPLAY.blit(songcredits, (0, 605))
        if Goblin.b < 300:
            Player.a = 300
            Player.b = 300
            DISPLAY.blit(finalscore, (350, 200))
            DISPLAY.blit(winningmessage,(285, 500))
        elif Player.a < 0:
            Goblin.a = 320
            Goblin.b = 320
            DISPLAY.blit(youlost, (230, 500))
        
    

    pygame.display.flip()

                    
    


    pygame.quit()

if __name__ == "__main__":
    main()