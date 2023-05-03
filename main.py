import pygame
import random
import math

pygame.init()#游戏初始化

i=0
clock=pygame.time.Clock()

#创建游戏窗口
scr=pygame.display.set_mode((1024,617))#返回一个屏幕对象
pygame.display.set_caption('坤坤大作战：黑子的篮球')#游戏名字
icon=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\13，游戏图标.jpg')
pygame.display.set_icon(icon)#设置游戏图标

#导入坤坤背景图
kunkun1=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\17，kunkun背景图.jpg')

#导入ikun图标
ikun=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\20，ikun.jpg')

#导入开始界面
start=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\23，开始界面（一分钟）.jpg')

#导入射中音效
kun_sound=pygame.mixer.Sound(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\26，你干嘛（剪辑的副本.mp3')

#定义分数：
score= 0
font= pygame.font.Font('freesansbold.ttf',32)
def show_score():
    text=f'Little Haters:{score}'
    score_render=font.render(text,True,(0,255,0))
    scr.blit(score_render,(10,10))


def show_haters():#显示剩余时间
    text=f'you need to knock down 60 haters'
    score_render=font.render(text,True,(255,0,0))
    scr.blit(score_render,(10,500))

#设置结局
a1=0#结局1
b1=0#结局2
c1=0#结局3

#导入结局
end1=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\48，结局1.jpg')
end2=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\49，结局2.jpg')
end3=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\50，结局3 2的副本.jpg')
end4=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\51，结局4的副本.jpg')

ikunX=512
ikunY=500
ikunStep=0#ikun移动的速度

kunkun=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\57，kunkun.png')

#控制KUNKUN的位置
kunkunX=512
kunkunY=550
kunkunStep=5

#黑子的篮球数目的导入
num_of_bas=4


#篮球类
class bas():
    def __init__(self):
        self.bas=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\71，ikun的篮球 2.png')
        self.x=random.randint(200,800)
        self.y=random.randint(50,100)
        self.step=random.randint(2,5)
    def reset(self):
        self.x = random.randint(200, 800)
        self.y = random.randint(50, 100)

bas1=[]
for i in range(num_of_bas):
    bas1.append(bas())

def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+b*b)


#爱心类
class luv():

    def __init__(self):
        self.luv=pygame.image.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\93，ikun发射爱心的副本.jpg')
        self.x=ikunX+8
        self.y=ikunY-10
        self.step=5
    def hit(self):
        global a1,b1,score
        for l in bas1:
            if distance(self.x,self.y,l.x,l.y)<75:#表示爱心打到篮球
                try:
                    luvs.remove(self)
                    kun_sound.play()
                except ValueError:
                    break
                #luvs.remove(self)
                l.reset()
                score+=1
            if distance(self.x,self.y,kunkunX,kunkunY)<40:
                a1=1#结局1
                #running=False
            if distance(l.x,l.y,kunkunX,kunkunY)<50:
                b1=1#结局2


luvs=[]#保存现有的爱心

#显示爱心，并移动爱心💗
def show_luvs():
    for b in luvs:
        scr.blit(b.luv,(b.x,b.y))
        b.hit()#检测是否击中
        b.y-=b.step
        if b.y<0  :#or b.y>617:
            b.step*=-1
            #luvs.remove(b)



#显示篮球，并且篮球的移动和下沉
def show_bas():
    for e in bas1:
        scr.blit(e.bas,(e.x,e.y))
        e.x+=e.step
        if e.x>874 or e.x<0:
            e.step*=-1
            e.y+=150

def process_event():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            #按下键，就可以移动
            if event.key==pygame.K_RIGHT:
                ikunStep=7.5
            elif event.key==pygame.K_LEFT:
                ikunStep=-7.5
        if event.type==pygame.KEYUP:
            ikunStep=0

def move_ikun():
    global ikunX
    if ikunX>974:
        ikunX=974
    if ikunX<0:
        ikunX=0

def move_kunkun():
    global  kunkunX,kunkunStep
    if kunkunX>974 or kunkunX<0:
        kunkunStep*=-1


starts=True
running=True
while starts:
    scr.blit(start,(0,0))
    show_haters()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            starts=False
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                starts=False
    pygame.display.update()


#running=True
while running:
    clock.tick(60)
    scr.blit(kunkun1,(0,0))
    show_score()#显示分数
    #show_Time()#显示剩余坚持时间

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            #按下键，就可以移动
            if event.key==pygame.K_RIGHT:
                ikunStep=7.5
            elif event.key==pygame.K_LEFT:
                ikunStep=-7.5
            elif event.key==pygame.K_SPACE:
                #创建一颗爱心
                b=luv()
                luvs.append(b)


        if event.type==pygame.KEYUP:
            ikunStep=0

    for l in bas1:
        if distance(l.x,l.y,kunkunX,kunkunY)<50:
            b1=1



    scr.blit(ikun,(ikunX,ikunY))#把东西画在画布上，又再次重新更新位置
    ikunX+=ikunStep             #控制ikun的运动
    #防止ikun跑出界面
    scr.blit(kunkun,(kunkunX,kunkunY))
    kunkunX+=kunkunStep
    move_kunkun()

    move_ikun()

    show_bas()

    show_luvs()#显示爱心

    pygame.display.update()#类似于展示画布画布

    i+=1
    #print(i)
    d=i//60
    if i == 60:
        print('1')
    elif d*60==i:
        print(d)#显示坚持秒数



    if i==3600:#坚持时间
        c1=1#结局3
        break

    if a1==1:
        break
    elif b1==1:
        break

a2=True
b2=True
c2=True

if a1==1:
    starts = True
    running = True
    while a2:
        scr.blit(end1,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a2 = False
            '''if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE :
                    a1 = 0
                    b1 = 0
                    c1 = 0
                    break'''

if b1==1:
    starts = True
    running = True
    pygame.mixer.music.load(r'C:\Users\NR\PycharmProjects\pythonProjectNR1\268，鸡你太美剪辑的副本.mp3')
    pygame.mixer.music.play(-1)
    while b2:
        scr.blit(end2,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b2 = False
            '''if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE :
                    a1 = 0
                    b1 = 0
                    c1 = 0
                    break'''

if c1==1 and score>60:
    starts = True
    running = True
    while c2:
        scr.blit(end3,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c2 = False
            '''if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE :
                    a1 = 0
                    b1 = 0
                    c1 = 0
                    break'''

if c1==1 and score<=60:
    starts = True
    running = True
    while c2:
        scr.blit(end4,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c2 = False
pygame.quit()