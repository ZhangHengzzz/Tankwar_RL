import random
from sprites import *
import pygame
from settings import Settings
from tank_war import TankWar

class AI_tank_war:

    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None
        self.winflag = True
        self.reset_flag = True
        self.score = 0
        self.last_score = 0
        self.reward = 0


    @staticmethod
    def __init_game():
        """
        初始化游戏的一些设置
        :return:
        """
        pygame.init()   # 初始化pygame模块
        pygame.display.set_caption(Settings.GAME_NAME)  # 设置窗口标题
        pygame.mixer.init()    # 初始化音频模块


    def __create_sprite(self):
        self.hero = Hero(Settings.HERO_IMAGE_NAME, self.screen)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for i in range(Settings.ENEMY_COUNT):
            direction = random.randint(0, 3)
            enemy = Enemy(Settings.ENEMY_IMAGES[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)
        self.__draw_map()

    def __draw_map(self):
        """
        绘制地图
        :return:
        """
        for y in range(len(Settings.MAP_ONE)):
            for x in range(len(Settings.MAP_ONE[y])):
                if Settings.MAP_ONE[y][x] == 0:
                    continue
                wall = Wall(Settings.WALLS[Settings.MAP_ONE[y][x]], self.screen)
                wall.rect.x = x*Settings.BOX_SIZE
                wall.rect.y = y*Settings.BOX_SIZE
                if Settings.MAP_ONE[y][x] == Settings.RED_WALL:
                    wall.type = Settings.RED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.IRON_WALL:
                    wall.type = Settings.IRON_WALL
                elif Settings.MAP_ONE[y][x] == Settings.WEED_WALL:
                    wall.type = Settings.WEED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.BOSS_WALL:
                    wall.type = Settings.BOSS_WALL
                    wall.life = 1
                self.walls.add(wall)


    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                TankWar.__game_over()

    def __check_collide(self):
        # 保证坦克不移出屏幕
        self.hero.hit_wall()
        for enemy in self.enemies:
            enemy.hit_wall_turn()

        # 子弹击中墙
        for wall in self.walls:
            # 我方英雄子弹击中墙
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                        self.last_score += 10
                    elif wall.type == Settings.BOSS_WALL:
                        self.last_score -= 100
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()
            # 敌方英雄子弹击中墙
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if pygame.sprite.collide_rect(wall, bullet):
                        if wall.type == Settings.RED_WALL:
                            wall.kill()
                            bullet.kill()
                        elif wall.type == Settings.BOSS_WALL:
                            self.last_score -= 100
                            self.game_still = False
                        elif wall.type == Settings.IRON_WALL:
                            bullet.kill()

            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    self.last_score -= 1
                    # 移出墙内
                    self.hero.move_out_wall(wall)

            # 敌方坦克撞墙
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # 子弹击中、敌方坦克碰撞、敌我坦克碰撞
        # pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        for enemy in self.enemies:
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(bullet, enemy):
                    enemy.kill()
                    bullet.kill()
                    self.last_score += 100

        # 敌方子弹击中我方
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(bullet, self.hero):
                    bullet.kill()
                    self.hero.kill()
                    self.last_score -= 100

    def __update_sprites(self):
        if self.hero.is_moving:
            self.hero.update()
        self.walls.update()
        self.hero.bullets.update()
        self.enemies.update()
        for enemy in self.enemies:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)
        self.enemies.draw(self.screen)
        self.hero.bullets.draw(self.screen)
        self.screen.blit(self.hero.image, self.hero.rect)
        self.walls.draw(self.screen)


    def __check_over(self):
        if not self.enemies:
            self.last_score += 1000
            self.winflag = False

    def decode_action(self, action):
        if action == 0:
            # 按下左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif action == 1:
            # 按下右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif action == 2:
            # 按下上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif action == 3:
            # 按下下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        else:
            # 坦克发子弹
            self.hero.shot()


    def reset(self):
        self.__init_game()
        self.__create_sprite()
        self.score = 0
        self.last_score = 0
        self.reset_flag = True
        self.hero.is_alive = True
        self.game_still = True
        self.winflag = True

    def next(self, action):
        print('action:', action)
        self.decode_action(action)
        print('score:{} reward:{} alive:{}'.format(self.score, self.reward, self.hero.is_alive))
        image = pygame.surfarray.array3d(pygame.display.get_surface())
        if self.last_score != self.score:
            self.reward = self.last_score - self.score
            self.score = self.last_score
        else:
            self.reward = -0.01
        if self.hero.is_alive and self.game_still and self.winflag:
            self.reset_flag = True
        else:
            self.reset_flag = False

        return image, self.score, self.reward, self.reset_flag

    def show(self):
        self.screen.fill(Settings.SCREEN_COLOR)
        # 1、设置刷新帧率
        self.clock.tick(Settings.FPS)
        # 2、事件监听
        self.__event_handler()
        # 3、碰撞监测
        self.__check_collide()
        # 4、更新/绘制精灵/经理组
        self.__update_sprites()
        # 5、更新显示
        self.__check_over()
        pygame.display.update()



    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        time = 0
        while True and self.hero.is_alive and self.game_still:
            self.screen.fill(Settings.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Settings.FPS)
            # 2、事件监听
            self.__event_handler()

            time = random.randint(0, 100)
            if time < 10:
                action = random.randint(0, 5)
                print('action:', action)
                self.decode_action(action)
                print('score:{} reward:{} alive:{}'.format(self.score,  self.score, self.hero.is_alive))
            # 3、碰撞监测
            self.__check_collide()
            # 4、更新/绘制精灵/经理组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
            # 6、判断是否结束
            self.__check_over()

        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()



if __name__ == '__main__':

    game = AI_tank_war()
    game.run_game()