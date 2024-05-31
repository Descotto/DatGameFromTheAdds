import pygame
from settings import *
from player import Player




class Level:
    def __init__(self, surface):
        # level setup
        
        self.display_surface = surface
        self.setup_level()
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.current_x = 0
       

    def setup_level(self):
        
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()
        
        player_sprite = Player((10,10),
                                [self.visible_sprites, self.player]
                                )
        # setup tiles
        # for style,layout in layouts.items():
        #     for row_index, row in enumerate(layout):
        #         for col_index, cell in enumerate(row):

        #             x = col_index * tile_size
        #             y = row_index * tile_size
                    

        #             if cell != '-1':
        #                 if style == 'floor':
        #                     tile = Tile((x, y),[self.tiles], tile_size)
                            

        #                 if style == 'boundaries':
        #                     tile = Tile((x, y),[self.tiles], tile_size)

        #                 if style == 'enemy_boundaries':
        #                     tile = Tile((x, y),[self.enemy_boundaries], tile_size)
        #                 if style == 'loot':
        #                     loot = Loot_Box((x,y + 25),[self.loot,self.visible_sprites])

        #                 if style == 'player':
        #                     # CREATE PLAYER============================
        #                     player_sprite = Player(
        #                         (x,y),
        #                         [self.visible_sprites, self.player],
        #                         self.shoot,
        #                         self.toss_bomb
        #                         )    

        #                 if style == 'enemy':
        #                     enemy_sprite = Enemy(
        #                         (x,y),
        #                         [self.visible_sprites,self.enemies],
        #                         self.enemy_check_death,
        #                         self.enemy_shoot,
        #                         )
        #                 if style == 'elevators':
        #                     elevator = Elevator((x,y), [self.visible_sprites, self.elevators], self.elevator_threshold)
        #                 if style == 'elevator_threshold':
        #                     threshold = Tile((x,y),[self.elevator_threshold])
                        


        #                 if style == 'water':
        #                     effect = Particles((x,y),[self.visible_sprites],style)





    # def horizontal_movement_collision(self,leech):

    #     player = leech

    #     player.rect.x += player.direction.x * player.speed

    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.x < 0:
    #                 player.rect.left = sprite.rect.right
    #                 player.on_left = True
    #                 self.current_x = player.rect.left
    #             elif player.direction.x > 0:
    #                 player.rect.right = sprite.rect.left
    #                 player.on_right = True
    #                 self.current_x = player.rect.right

    #     if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
    #         player.on_left = False
    #     if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
    #         player.on_right = False

    # def vertical_movement_collision(self,leech):
    #     player = leech
        
    #     player.apply_gravity()

    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.y > 0:
    #                 player.rect.bottom = sprite.rect.top
    #                 player.direction.y = 0
    #                 player.on_ground = True
    #             elif player.direction.y < 0:
    #                 player.rect.top = sprite.rect.bottom
    #                 player.direction.y = 0
    #                 player.on_ceiling = True

    #         if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
    #             player.on_ground = False

    #         if player.on_ceiling and player.direction.y > 0:
    #             player.on_ceiling = False

    # PLAYER ACTIONS
        
    #================================================
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # ENEMY ACTIONS =================================

    
    # ================================================
            # //////////////////////////////////////
    # WEAPON ACTIONS =================================

    #=================================================
        # ////////////////////////////////////////////
# =================================================================
    def run(self):
        player = self.player.sprite
        self.visible_sprites.custom_draw(player)
        self.visible_sprites.update(player)
        self.visible_sprites.enemy_update(player)


        # level tiles
        # self.tiles.update(self.world_shift_x,self.world_shift_y)
        # self.tiles.draw(self.display_surface)
        # self.scroll_x()
        # self.scroll_y()

        # player
        self.player.update()
        # self.player.draw(self.display_surface)
        
        # # bullet
        # self.bullets.update()
        # self.bullets.draw(self.display_surface)

        # # granades
        # self.granades.update(self.enemies)
        # self.granades.draw(self.display_surface)
        # # particles
        # self.particles.update()
        # self.particles.draw(self.display_surface)

        # # enemies
        # self.enemies.update(self.player, self.world_shift)
        # self.enemies.draw(self.display_surface)

        # UI
        self.ui.display(player)

        # # Special Events Handlers
        # self.handle_death()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #CREATE FLOOR
        self.current_map = 1
        self.floor_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        #self.floor_surf = pygame.image.load(Maps_backgrounds[self.current_map]['url']).convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        # offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw floor
        floor_upset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_upset_pos)


        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == "enemy"]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
