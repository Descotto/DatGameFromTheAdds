import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        # self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.Surface((64,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # player status
        self.status = 'idle'
        self.shooting = False
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # player stats
        self.stats = {
            'hp': 20,
            'tp': 100,
        }
        self.name = 'Mike'
        self.hp = self.stats['hp']
        self.tp = self.stats['tp']
        self.xp = 0
        self.to_level = 50

    

        # weapons

        # actions

        
        # cooldowns
        # self.bullet_cooldown = 0.5
        # self.last_shoot_time = 0
        # self.mg_cooldown = 0.05
        # self.last_mg_time = 0
        # self.bomb_cooldown = 2
        # self.last_bomb_time = 0
        self.vulnerable_cooldown = 0.3
        self.last_vulnerable_time = 0
        # self.bomb_regen_cooldown = 30000
        # self.last_regen_time = 0

    # def import_character_assets(self):
    #     character_path = 'assets/graphics/player/'
    #     self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[], 'shoot':[]}

    #     for animation in self.animations.keys():
    #         full_path = character_path + animation
            
    #         self.animations[animation] = import_folder(full_path)

    # def animate(self):
    #     animation = self.animations[self.status]

    #     # loop over frame index
    #     self.frame_index += self.animation_speed
    #     if self.frame_index >= len(animation):
    #         self.frame_index = 0

    #     image = animation[int(self.frame_index)]
    #     if self.facing_right:
    #         self.image = image
    #     else:
    #         flipped_image = pygame.transform.flip(image,True,False)
    #         self.image = flipped_image

    #     # set the rect
    #     if self.on_ground and self.on_right:
    #         self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
    #     elif self.on_ground and self.on_left:
    #         self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
    #     elif self.on_ground:
    #         self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
    #     elif self.on_ceiling and self.on_right:
    #         self.rect = self.image.get_rect(topright = self.rect.topright)
    #     elif self.on_ceiling and self.on_left:
    #         self.rect = self.image.get_rect(topleft = self.rect.topleft)
    #     elif self.on_ceiling:
    #         self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        # if keys[pygame.K_SPACE] and self.on_ground:
        #     self.jump()

        # if keys[pygame.K_s]:
        #     self.shoot()
        #     self.shooting = True
        # else:
        #     self.shooting = False

            
    def get_status(self):
        if self.direction.y <0:
            self.status = 'jump'
        elif self.direction.y >1:
            self.status = 'fall'
        elif self.shooting:
            self.status = 'shoot'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
                
    # def apply_gravity(self):
    #     self.direction.y += self.gravity
    #     self.rect.y += self.direction.y

    # def jump(self):
    #     self.direction.y = self.jump_speed
 

            

    def update(self,particles):
        self.get_input(particles)
        self.get_status()
        # self.animate()
        
        