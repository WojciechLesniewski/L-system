import turtle as t
import random as r

position = [-300, 50]
axiom = 'F++F++F'
rule = ['F', ' F-F(++F-F']
angle = 60
step = 5
iterations = 4

#pentadendryt
"""
position = [-500, -150]
axiom = 'F'
rule = ['F', 'F+(F-F--F+F+F']
angle = 72
step = 10
iterations = 4
"""

#sierpinski
"""
position = (-200, 100)
axiom = 'F+F+F'
rule = ['F', 'F+F(-F-F+F']
angle = 120
step = 25
iterations = 4
"""

# drzewo
"""
position = (-200, -300)
axiom = '---F'
rule = ['F', 'FF+[+F-F(-F]-[-F+F+F]']
angle = 22.5
step = 25
iterations = 3
"""


def gen(axiom, rule, num):
    sentence = axiom
    for i in range(num):
        sentence = sentence.replace(rule[0],rule[1])
    return sentence


def draw(s,  angle, step):
    sentence = s
    stack = []
    newposition = []

    for x in sentence:
        if x == 'F':
            t.forward(step)
        elif x == 'f':
            t.penup()
            t.forward(step)
            t.pendown()
        elif x == '+':
            t.right(angle)
        elif x == '-':
            t.left(angle)
        elif x == '[':
            stack.append(t.position())
        elif x == ']':
            newposition = stack.pop()
            t.penup()
            t.setx(newposition[0])
            t.sety(newposition[1])
            t.pendown()
        elif x == '(':
            t.pencolor((r.randrange(255), r.randrange(255), r.randrange(255)))

t.penup()
t.setx(position[0])
t.sety(position[1])
t.pendown()
t.speed(100)
t.colormode(255)
nsentence = gen(axiom,rule,iterations)
draw(nsentence, angle, step)

t.done()