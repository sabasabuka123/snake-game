import turtle
import random


score=0
live=3
# screen est up
wn=turtle.Screen()
wn.title('Snake')
wn.bgcolor('green')
wn.bgpic('background.png')
wn.setup(width=800,height=600)
wn.tracer(0)


wn.register_shape('snake_left.gif')
wn.register_shape('snake_down.gif')
wn.register_shape('snake_right.gif')
wn.register_shape('snake_up.gif')
wn.register_shape('bomb.gif')
wn.register_shape('applee.gif')

# add player

player = turtle.Turtle()
player.speed(0)
player.shape('snake_left.gif')
player.color('white')
player.penup()
player.goto(0,-250)
player.direction = 'stop'
# apples
apple = turtle.Turtle()
apple.speed(0)
apple.shape('applee.gif')
apple.color('red')
apple.penup()
apple.goto((0,250))
# bad guy
bad = turtle.Turtle()
bad.speed(0)
bad.shape('bomb.gif')
bad.color('black')
bad.penup()
bad.goto((10,200))

# pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
s=('curier', 24, 'normal')
pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)


# function
def go_left():
    player.direction ="left"
    player.shape('snake_left.gif')
def go_right():
    player.direction ="right"
    player.shape('snake_right.gif')
def go_up():
    player.direction ="up"
    player.shape('snake_up.gif')
def go_down():
    player.direction ="down"
    player.shape('snake_down.gif')
# keyboard
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
# main game loop
while True:
    wn.update()
    # player move
    if player.direction =="left":
        x = player.xcor()
        x-=1
        player.setx(x)
    if player.direction =="right":
        x = player.xcor()
        x+=1
        player.setx(x)
    if player.direction =="up":
        y = player.ycor()
        y+=1
        player.sety(y)
    if player.direction =="down":
        y = player.ycor()
        y-=1
        player.sety(y)
        
    
    elif player.xcor==(400):
        player.goto(-400)
    #check a touch
    if apple.distance(player)<20:
        x=random.randint(-200,300)
        y=random.randint(-200,200)
        apple.goto(x,y)
        score+=10
        pen.clear()
        pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)
        print('score: {}'.format(score))
    elif bad.distance(player)<20:
        x=random.randint(-200,300)
        y=random.randint(-200,200)
        bad.goto(x,y)
        score-=10
        live-=1
        pen.clear()
        pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)
        print('score: {}'.format(score))
    # if score==100:
    #     live+=1
    elif live<0:
        pen.goto(0,0)
        z=('curier', 24, 'normal')
        pen.write('game over',align='center',font=z)

    



wn.mainloop()