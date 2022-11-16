#기초파이썬 7장 연습문제 터틀그래픽


#1. 눈사람을 그리는 함수를 작성하고 이 함수를 여러 번 호출하여서 랜덤한 위치에 눈사람을 그리는 프로그램을 작성하라.

import turtle                          #거북이 모듈 불러오기
import random                          #랜덤 값
t=turtle.Turtle()                      #거북이 생성
t.shape("turtle")
s=turtle.Screen()                      #스크린 생성
t.color('black','white')
s.bgcolor('skyblue')


def snowman_friend(x,y):               #snow_friend() 함수 정의
    t.up
    t.goto(x,y)
    t.down
    t.begin_fill()
    t.circle(20)
    t.end_fill()                       #눈사람 머리
    
    t.up
    t.goto(x,y-20)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()                       #눈사람 중간
    
    t.left(20)
    t.forward(40)
    t.forward(-40)
    t.left(120)
    t.forward(40)
    t.forward(-40)
    t.right(140)                       #눈사람 중반부
    
    t.up()
    t.goto(x,y-90)
    t.down()
    t.begin_fill()
    t.circle(37)
    t.end_fill()                       #눈사람 하단
    
for i in range(3):                     #3번 반복
    x=random.randint(-300,300)
    y=random.randint(-300,300)         #x좌표와 y좌표를 -300,300 범위 내에서 무작위로 생성
    snowman_friend(x,y)
t.screen.exitonclick()


#2. 6각형을 그리는 draw_hexa() 함수를 작성하고 이 함수를 호츌하여서 다음과 같은 벌집 모양을 화면에 그려보자.

import turtle
t=turtle.Turtle()
t.shape("turtle")

def draw_hexa():                       #draw_hexa() 함수 정의
    for i in range(6):                 #6번 반복
        t.forward(100)
        t.left(60)
        
for i in range(6):                     #6번 반복
    draw_hexa()
    t.forward(100)
    t.right(60)
t.screen.exitonclick()


#3. 함수 f(x)=x^2+1을 계산하는 함수를 작성하고 이 함수를 이용하여 화면에 f(x)를 그려보자.

import turtle
t=turtle.Turtle()
t.shape("turtle")

def f_draw():                     #f_draw() 함수 정의
    for i in range(150):          #150번 반복
        t.goto(i,0.01*(i**2+1))   #f(x)=x^2+1에 해당하는 값으로 이동

t.forward(200)
t.forward(-200)
t.left(90)
t.forward(200)
t.forward(-200)
t.right
f_draw()
t.screen.exitonclick()


#4. 터틀 그래픽에서 거북이를 움직이지 않고 선을 긋는 함수 draw_line()을 정의하고 이것을 이용하여 다음과 같은
#   거미줄과 같은 모양을 그려보자. 거북이는 항상 중앙에 위치한다.

import turtle
t=turtle.Turtle()
t.shape("turtle")

def draw_line():             #draw_line() 함수 정의
    for i in range(12):      #12번 반복
        t.forward(100)
        t.forward(-100)
        t.left(30)
        
draw_line()
t.screen.exitonclick()