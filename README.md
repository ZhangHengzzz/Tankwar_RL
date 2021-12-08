# Tankwar_RL智能对抗体  
一、前言  
关于智能对抗体这样的游戏，我们的第一想法就是坦克大战的这个游戏，与智能对抗体十分的类似，因此我们决定在坦克大战的基础上，完成智能对抗体的项目。  
二、开发环境  
开发工具：pycharm  
开发环境：python 3.9.6  
第三方模块：pygame、pytorch  
三、项目介绍  
3.1 项目截图
我们主程序入口在main.py文件，在安装好pygame模块后就能直接运行。下面是运行截图：

下面是子弹击中墙壁的爆炸效果：

下面是多个敌方坦克的效果图：

我们再来看看项目的各个文件。
3.2 项目文件
下面是项目目录：

（1）resources
其中resources是资源文件，音频、图片等都在resources目录。而tools中提供了两个小工具，因为只是供个人临时使用的，这里不过多解释了。
（2）main.py
而main.py则是项目的主入口，代码很短：
from tank_war import TankWarif __name__ == '__main__':    tankWar = TankWar()    tankWar.run_game()
我们直接创建了TankWar的实例，然后调用run_game方法运行游戏。
（3）tank_war.py
tank_war.py中写了我们坦克大战游戏主体的模块，里面的TankWar类定义了游戏主体的一切行为。包括初始化屏幕、初始化pygame模块、创建敌方坦克、绘制地图、检测碰撞、监听事件等。
（4）sprites.py
在pygame中提供了一个sprite类用于创建有图像的物体。而sprites中定义的都是sprite的子类，因此也都是有图片的类。其中包括坦克基类、英雄类（我方坦克）、敌人类（敌方坦克）、子弹类、墙类等。
而各个类中定义了各自的行为，例如：坦克类有发射子弹的行为、移动的行为、爆炸的行为等。
（5）settings.py
settings.py中定义了一些设置信息，包括子弹的数量、子弹的速度、坦克的速度、地图信息、图片信息等。我们可以通过修改settings.py来调整游戏的一些设置，因为还没有写设置相关的操作，所以需要修改源码。
