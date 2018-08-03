import turtle
import time
import pygame
'''
turtle.forward(30)
turtle.backward(30)
turtle.left(90)
turtle.speed(9)
'''
def draw_circle(angie): #形参：海龟
    angie.circle(150)



def draw_triangle(angie):
    for i in range(3):   #画三条边
        angie.forward(200)   #边长
        angie.right(120)

def draw_square(angie):
    for i in range(4):
        angie.forward(200)
        angie.right(90)


#定义函数来初始化
def init_turtle():  #初始化图像库
    #构造窗口对象
    window = turtle.Screen()
    window.bgcolor('green')
    brad=turtle.Turtle()    #class Turtle 类--实例对象
    brad.shape('turtle')  #阴影和图案,画笔在画布上的图形，小黑点
    brad.shapesize(28)
    #画笔的粗细
    brad.pensize(30)
    #移动速度
    brad.speed(8)
    return window,brad
#画复杂图案
def draw_art():
    #拿到窗体对象
    window,brad=init_turtle()
    for i in range(36):
        brad.color('yellow')
        draw_triangle(brad)
        #改颜色
        brad.color('red')
        draw_circle(brad)
        #海龟包含画布和画笔
        brad.color('blue')
        draw_square(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(800)
    time.sleep(3)
   # brad.done()

#初始化播放器
def init_player():
    pygame.init()  #初始化
    play = pygame.mixer.music  #音乐播放器
    return play
def play_draw(filename):
    play = init_player()
    play.load(filename)
    print('play the music')
    play.play(loops=0,start=1)
    draw_art()
    play.stop()
    print('stop the music')


if __name__=='__main__':
    #draw_art()
    try:
        play_draw('Sleep Away.mp3')
    except Exception as e:
        pass
