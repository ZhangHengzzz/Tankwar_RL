import pygame
from sprites import *

class Test_TankWar:

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

    def __check_keydown(self, event):
        """检查按下按钮的事件"""
        if event == 0:
            # 按下左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
            return self.hero.direction,self.hero.is_moving,self.hero.is_hit_wall
        elif event == 1:
            # 按下右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
            return self.hero.direction, self.hero.is_moving, self.hero.is_hit_wall
        elif event == 2:
            # 按下上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
            return self.hero.direction, self.hero.is_moving, self.hero.is_hit_wall
        elif event== 3:
            # 按下下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
            return self.hero.direction, self.hero.is_moving, self.hero.is_hit_wall
        elif event == 4:
            # 坦克发子弹
            self.hero.shot()
            return self.hero.shot()

    def __check_keyup(self, event):
        """检查松开按钮的事件"""
        if event == 0:
            # 松开左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
            return self.hero.direction,self.hero.is_moving
        elif event == 1:
            # 松开右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
            return self.hero.direction, self.hero.is_moving
        elif event == 2:
            # 松开上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
            return self.hero.direction, self.hero.is_moving
        elif event == 3:
            # 松开下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False
            return self.hero.direction, self.hero.is_moving


    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                Test_TankWar.__game_over()
            elif event.type == pygame.KEYDOWN:
                Test_TankWar.__check_keydown(self, event)
            elif event.type == pygame.KEYUP:
                Test_TankWar.__check_keyup(self, event)

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
                    elif wall.type == Settings.BOSS_WALL:
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
                            self.game_still = False
                        elif wall.type == Settings.IRON_WALL:
                            bullet.kill()

            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # 移出墙内
                    self.hero.move_out_wall(wall)

            # 敌方坦克撞墙
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # 子弹击中、敌方坦克碰撞、敌我坦克碰撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        # 敌方子弹击中我方
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(bullet, self.hero):
                    bullet.kill()
                    self.hero.kill()

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

    def __game_begin(self):
        start_screen = pygame.Surface(Settings.SCREEN_RECT.size)  # 充当开始界面的画布
        start_screen = start_screen.convert()
        start_screen.fill((255, 255, 255))  # 白色画布1（开始界面用的）
        i1 = pygame.image.load("./resources/images/begin/s1.png")
        i1.convert()
        i11 = pygame.image.load("./resources/images/begin/s2.png")
        i11.convert()

        i2 = pygame.image.load("./resources/images/begin/n1.png")
        i2.convert()
        i21 = pygame.image.load("./resources/images/begin/n2.png")
        i21.convert()
        n1 = True
        while n1:
            self.clock.tick(Settings.FPS)
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1 >= 327 and x1 <= 655 and y1 >= 221 and y1 <= 287:
                start_screen.blit(i11, (300, 200))
                if buttons[0]:
                    n1 = False

            elif x1 >= 327 and x1 <= 655 and y1 >= 341 and y1 <= 407:
                start_screen.blit(i21, (300, 320))
                if buttons[0]:
                    pygame.quit()
                    exit()

            else:
                start_screen.blit(i1, (300, 200))
                start_screen.blit(i2, (300, 320))

            self.screen.blit(start_screen, (0, 0))
            pygame.display.update()
            # 下面是监听退出动作

            # 监听事件
            for event in pygame.event.get():

                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    print("游戏退出...")

                    # quit 卸载所有的模块
                    pygame.quit()

                    # exit() 直接终止当前正在执行的程序
                    exit()

    def run_game(self):
        self.__init_game()
        self.__game_begin()
        self.__create_sprite()
        while True and self.hero.is_alive and self.game_still:
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
            pygame.display.update()
        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

    def test_aa(self):
        self.screen = pygame.display.set_mode(Settings.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None
        self.__init_game()
        self.__create_sprite()
        # 自动化测试----上下左右是否按下
        assert self.__check_keydown(0) == (0, True, False)
        assert self.__check_keydown(1) == (1, True, False)
        assert self.__check_keydown(2) == (2, True, False)
        assert self.__check_keydown(3) == (3, True, False)
        assert self.__check_keydown(4) == (True)
        # 自动化测试----上下左右是否松开
        assert self.__check_keyup(0) == (0, False)
        assert self.__check_keyup(1) == (1, False)
        assert self.__check_keyup(2) == (2, False)
        assert self.__check_keyup(3) == (3, False)
        # 自动化测试----






























