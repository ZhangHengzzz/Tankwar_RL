import pygame
from sprites import *

def __game_begin():
    start_screen = pygame.Surface(Settings.SCREEN_RECT.size)  # 充当开始界面的画布
    start_screen = start_screen.convert()
    start_screen.fill((255, 255, 255))  # 白色画布1（开始界面用的）
    i1 = pygame.image.load("./resources/images/begin/s11.png")
    i1.convert()
    i11 = pygame.image.load("./resources/images/begin/s21.png")
    i11.convert()

    i2 = pygame.image.load("./resources/images/begin/n11.png")
    i2.convert()
    i21 = pygame.image.load("./resources/images/begin/n21.png")
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


def choose_model(self):
    choose_screen = pygame.Surface(Settings.SCREEN_RECT.size)  # 充当选择界面的画布
    choose_screen = choose_screen.convert()
    choose_screen.fill((255, 255, 255))  # 白色画布1（选择界面用的）
    i1 = pygame.image.load("./resources/images/choose/p1.png")
    i1.convert()
    i11 = pygame.image.load("./resources/images/choose/p2.png")
    i11.convert()

    i2 = pygame.image.load("./resources/images/choose/a1.png")
    i2.convert()
    i21 = pygame.image.load("./resources/images/choose/a2.png")
    i21.convert()

    n1 = True
    while n1:
        self.clock.tick(Settings.FPS)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= 327 and x1 <= 655 and y1 >= 121 and y1 <= 187:
            choose_screen.blit(i11, (300, 100))
            if buttons[0]:
                n1 = False

        elif x1 >= 327 and x1 <= 655 and y1 >= 441 and y1 <= 507:
            choose_screen.blit(i21, (300, 420))
            if buttons[0]:
                pygame.quit()
                exit()

        else:
            choose_screen.blit(i1, (300, 100))
            choose_screen.blit(i2, (300, 420))

        self.screen.blit(choose_screen, (0, 0))
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


def end_screen(self):
    end_screen = pygame.Surface(Settings.SCREEN_RECT.size)  # 充当开始界面的画布
    end_screen = end_screen.convert()
    end_screen.fill((255, 255, 255))  # 白色画布1（开始界面用的）
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
            end_screen.blit(i11, (300, 200))
            if buttons[0]:
                self.__init_game()
                self.__create_sprite()
                self.winflag = False
                self.hero.is_alive = True
                self.game_still = True
                n1 = False


        elif x1 >= 327 and x1 <= 655 and y1 >= 341 and y1 <= 407:
            end_screen.blit(i21, (300, 320))
            if buttons[0]:
                pygame.quit()
                exit()

        else:
            end_screen.blit(i1, (300, 200))
            end_screen.blit(i2, (300, 320))

        self.screen.blit(end_screen, (0, 0))
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