import random
import pygame

# (python开发中约定常量的命名方式为大写字母，各个单词间下划线链接)
#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,512,768)
#刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量,userevent用户事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
    """一个飞机大战游戏精灵的类"""
    def __init__(self,image_name,speed=1,speed_y=0):

        #在开发一个子类时，如果其父类不是Object这个基类时
        #必须主动调用父类的初始化方法,调用父类的方法使用super()函数
        #否则无法使用父类中已经封装好的初始化代码了
        super().__init__()

        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed_y = speed_y
    #重写update方法
    def update(self):

        #在屏幕的垂直方向上移动
        self.rect.y +=self.speed

class Backgroud(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./images/背景.jpg")

        #判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = - self.rect.height


    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移除屏幕，如果移除屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
        pass

class Enemy (GameSprite):
    """敌机类"""

    def __init__(self):

        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/feind.png")

        # 2. 指定低级的初始随机速度 1~3
        self.speed =random.randint(3,6)

        # 3. 指定敌机的初始随机位置
        self.rect.y = -self.rect.height
        max_width = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_width)

    def update(self):

        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height :
            #print("敌机飞出 %s" % self.rect)
            self.kill()

    def __del__(self):
         #print("敌机挂了 %s" % self.rect)
         pass

class Hero (GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法，设置image & speed
        super().__init__("./images/flugzeug.png",0)

        # 2. 设置英雄的初始位置
        self.rect.bottom = SCREEN_RECT.bottom -120
        self.rect.centerx =SCREEN_RECT.centerx
        #self.rect.y = SCREEN_RECT.height - 120
        #self.rect.x = SCREEN_RECT.width/2

        # 3.创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        #英雄在水平方向移动
        self.rect.x += self.speed
        self.rect.y += self.speed_y

        #控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x=0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y =0
        elif self.rect.bottom >SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
    def fire(self):
        print("发射")

        for i in (1,2,3):
            # 1. 创建子弹精灵
            bullet = Bullet()

            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            # 3. 添加精灵到精灵组
            self.bullet_group.add(bullet)

class Bullet (GameSprite):
    """子弹精灵"""

    def __init__(self):
        #调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet.png",-4)

    def update(self):
        #调用父类方法，让子弹沿垂直方向飞行
        super().update()


        #判断字段是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print("子弹销毁")