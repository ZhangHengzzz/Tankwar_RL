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
![image](https://user-images.githubusercontent.com/92613664/145184063-acaceb1a-93aa-42e1-8ca5-793e599cc169.png)  

下面是游戏中的画面：  
![image](https://user-images.githubusercontent.com/92613664/145184123-0e80a335-8ab6-489d-97eb-ec82e2c49961.png)  

我们再来看看项目的各个文件。  
3.2 项目文件  
下面是项目目录：  
![image](https://user-images.githubusercontent.com/92613664/145184213-c3a4ac9b-62cc-4de1-bca9-3dd983e771d8.png)  

（1）resources  
其中resources是资源文件，音频、图片等都在resources目录。而tools中提供了两个小工具，主要是为了绘制游戏地图。  
（2）main.py  
而main.py则是项目的主入口，代码很短：  
我们直接创建了TankWar的实例，然后调用run_game方法运行游戏，也就是进行用户手动操作。  
（3）tank_war.py  
tank_war.py中写了我们坦克大战游戏主体的模块，里面的TankWar类定义了游戏主体的一切行为。包括初始化屏幕、初始化pygame模块、创建敌方坦克、绘制地图、检测碰撞、监听事件等。  
（4）sprites.py  
在pygame中提供了一个sprite类用于创建有图像的物体。而sprites中定义的都是sprite的子类，因此也都是有图片的类。其中包括坦克基类、英雄类（我方坦克）、敌人类（敌方坦克）、子弹类、墙类等。
而各个类中定义了各自的行为，例如：坦克类有发射子弹的行为、移动的行为、爆炸的行为等。  
（5）settings.py  
settings.py中定义了一些设置信息，包括子弹的数量、子弹的速度、坦克的速度、地图信息、图片信息等。我们可以通过修改settings.py来调整游戏的一些设置，因为还没有写设置相关的操作，所以需要修改源码。  
（6）state.py  
这里是为了强化学习中的state和reward而编写，以前面的tank_war.py为基础，实现了自动控制角色运行的功能，并实时记录state和reward。  
（7）torch_RL.py  
采用pytorch框架，进行强化学习算法的描述，并且可以在该文件下对agent进行训练。  
（8）params3.pth  
记录了每训练一定轮次后的神经网络参数，并且可以在每次训练前调用，继续上次的训练。  
（9）test_Tankwar.py  
对程序基本操作功能的自动测试。
