from turtle import *
from turtle import *
q = Turtle()
screen = Screen()
screen.bgcolor("skyblue")
screen.title("Turtle House")


# ================= MENU =================

title = Turtle()
title.hideturtle()
title.penup()
title.goto(0, 200)
title.write("PYTHON TURTLE SIMULATOR", align="center", font= ("Elephant", 20, "bold"))
title.goto(0, 150)
title.write("WAKE THE TURTLE TO START THE GAME",
            align="center",
            font=("Arial", 20, "bold"))

instructions = Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, 100)
instructions.write("Click the turtle to wake it up!",
                   align="center",
                   font=("Arial", 16, "normal"))

programmer = Turtle()
programmer.hideturtle()
programmer.penup()
programmer.goto(0, -180)
programmer.write("Programmed by Saiyao Yin",
                 align="center",
                 font=("Arial", 14, "normal"))

# YOU = the sleeping turtle

q.shape("turtle")
q.color("black")
q.shapesize(5)
q.penup()
q.goto(0, 0)

zzz = Turtle()
zzz.hideturtle()
zzz.penup()
zzz.goto(45, 45)
zzz.write("Z Z Z",
          font=("Arial", 20, "bold"))


# ================= START GAME =================

def wake_up(x, y):

    # Remove menu
    title.clear()
    instructions.clear()
    programmer.clear()
    zzz.clear()

    title.hideturtle()
    instructions.hideturtle()
    programmer.hideturtle()
    zzz.hideturtle()
    # Put ALL your house code below this line
    q.goto(150, 125)
    q.onclick(wake_up)
    # turtle bed
    l = Turtle()
    l.hideturtle()
    l.penup()
    l.goto(0, 250)
    l.pendown()
    l.write("You moved into a new home, wait until you finish drawing the furniture...", align= "center", font= ("Elephant", 15))
    q.shape("turtle")
    q.shapesize(1)
    q.speed("slow")
    bgcolor("tan")
    q.penup()
    q.goto(150, 125)
    q.pendown()
    q.begin_fill()
    q.fillcolor("lightgoldenrodyellow")
    q.forward(250)
    q.left(90)
    q.forward(70)
    q.left(90)
    q.forward(250)
    q.left(90)
    q.forward(70)
    q.left(90)
    q.forward(250)
    #q.circle(50, 180)
    #q.forward(150)
    #q.circle(50, 180)
    #q.forward(150)
    q.end_fill()
    q.penup()
    q.left(90)
    q.forward(10)
    q.left(90)
    q.forward(70)
    q.right(180)
    q.pendown()
    for i in range(4):
        q.forward(50)
        q.left(90)
    #q.left(90)
    #q.forward(90)
    q.right(180)
    # food bowl
    q.penup()
    q.goto(-50, 125)
    q.forward(100)
    q.right(90)
    q.pendown()
    q.begin_fill()
    q.fillcolor("white")
    for i in range(4):
        q.forward(50)
        q.left(90)
    q.end_fill()
    q.forward(10)
    q.left(90)
    q.penup()
    q.forward(10)
    q.pendown()
    q.begin_fill()
    q.fillcolor("darkkhaki")
    for i in range(4):
        q.forward(30)
        q.right(90)
    q.end_fill()
    q.penup()
    q.forward(80)
    q.left(90)
    q.forward(10)
    q.right(90)
    # water bowl
    q.pendown()
    q.begin_fill()
    q.fillcolor("white")
    for i in range(4):
        q.forward(50)
        q.right(90)
    q.end_fill()
    q.forward(10)
    q.right(90)
    q.penup()
    q.forward(10)
    q.pendown()
    q.begin_fill()
    q.fillcolor("lightskyblue")
    for i in range(4):
        q.forward(30)
        q.left(90)
    q.end_fill()
    q.penup()
    q.forward(90)
    q.left(90)
    q.forward(90)
    q.right(180)
    q.pendown()
    q.forward(200)
    # basking rock
    #first half
    q.begin_fill()
    q.fillcolor("slategray")
    q.left(110)
    q.forward(20)
    q.left(100)
    q.forward(10)
    q.right(90)
    q.forward(30)
    q.left(60)
    q.forward(40)
    q.right(45)
    q.forward(30)
    # second half
    q.left(45) 
    q.forward(20) 
    q.left(100) 
    q.forward(10) 
    q.right(90) 
    q.forward(30) 
    q.left(50) 
    q.forward(40) 
    q.right(45) 
    q.forward(40)
    q.end_fill()
    q.left(75)
    q.penup()
    q.forward(150)
    # carpet
    q.pendown()
    q.begin_fill()
    q.fillcolor("forestgreen")
    q.left(90)
    q.forward(600)
    q.right(90)
    q.forward(300)
    q.right(90)
    q.forward(600)
    q.right(90)
    q.forward(300)
    q.end_fill()
    q.penup()
    q.goto(300, -300)
    q.left(90)
    q.forward(20)
    q.right(90)
    q.forward(50)
    q.pendown()
    # litter box
    q.begin_fill()
    q.fillcolor("saddlebrown")
    q.right(90)
    q.forward(50)
    q.circle(10, 90)
    q.forward(100)
    q.circle(10, 90)
    q.forward(50)
    q.circle(10, 90)
    q.forward(100)
    q.end_fill()
    q.left(90)
    q.penup()
    q.forward(15)
    q.pendown()
    q.begin_fill()
    q.fillcolor("burlywood")
    q.forward(40)
    q.left(90)
    q.forward(90)
    q.left(90)
    q.forward(40)
    q.left(90)
    q.forward(90)
    q.end_fill()
    q.color("black")
    q.penup()
    l.clear()
w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False


def press_w():
    global w_pressed
    w_pressed = True

def release_w():
    global w_pressed
    w_pressed = False


def press_a():
    global a_pressed
    a_pressed = True

def release_a():
    global a_pressed
    a_pressed = False


def press_s():
    global s_pressed
    s_pressed = True

def release_s():
    global s_pressed
    s_pressed = False


def press_d():
    global d_pressed
    d_pressed = True

def release_d():
    global d_pressed
    d_pressed = False


def move():
    if w_pressed:
        q.setheading(90)
        q.forward(10)

    if a_pressed:
        q.setheading(180)
        q.forward(10)

    if s_pressed:
        q.setheading(270)
        q.forward(10)

    if d_pressed:
        q.setheading(0)
        q.forward(10)

    ontimer(move, 20)


listen()

onkeypress(press_w, "w")
onkeyrelease(release_w, "w")

onkeypress(press_a, "a")
onkeyrelease(release_a, "a")

onkeypress(press_s, "s")
onkeyrelease(release_s, "s")

onkeypress(press_d, "d")
onkeyrelease(release_d, "d")
move()
q.onclick(wake_up)
# mutingshan nilailema
# 你个沟是一赛要 我tm进去那死乌龟就睡觉 让我点他都不起然后程序就关了 你写啥呢
#你他妈逼写个done（）不就完事了吗（记得copy进你的死活idle里头, 查看issues（那个做level的） 用WASD动， 把输入法调成英文（要不然动不了））， 我草我今天吃火鸡面又放太多酱了，都快辣晕我了
# 台词翻译：唤醒乌龟及开始游戏 点击唤醒乌龟        
#2026/09/16 添
done()



    
