import turtle
#------génération du L-système------
li=[0]
for i in range(6):
    gen = []
    for symbol in li:
        if symbol == 0:
            gen.extend([1,'push','left','div',0,'pop',1,"+",'right',0,"-",'restore',0])
        elif symbol == 1:
            gen.extend([1, 1])
        elif symbol == 'div':
            gen.extend(['div', 'add'])
        else:
            gen.append(symbol)
    li = gen
print(li)
#------dessin---------
#positionement initiale
turtle.speed(0)
turtle.lt(90)
turtle.pu()
turtle.sety(-270)
turtle.pd()

#piles
pos_stack=list()
head_stack=list()
main_pos_stack=list()
main_head_stack=list()
fd_stack=[5]

for symbol in li:
    if symbol == 0:
        turtle.pd()
        turtle.fd(fd_stack[0])
    elif symbol == 1:
        turtle.pd()
        turtle.fd(fd_stack[0]/1.3)
    elif symbol == "+":
        main_pos_stack.insert(0,turtle.pos())
        main_head_stack.insert(0,turtle.heading())
    elif symbol == "-":
        turtle.pu()
        turtle.goto(main_pos_stack.pop(0))
        turtle.seth(main_head_stack.pop(0))
    elif symbol == 'push':
        pos_stack.insert(0,turtle.pos())
        head_stack.insert(0,turtle.heading())
    elif symbol == 'left':
        turtle.lt(90)
    elif symbol == 'div':
        fd_stack.insert(0,fd_stack[0]/1.00001)
    elif symbol == 'add':
        fd_stack[0] =+ (fd_stack[0]/1.1)
    elif symbol == 'restore':
        del fd_stack[0]
    elif symbol == 'pop':
        turtle.pu()
        turtle.goto(pos_stack.pop(0))
        turtle.seth(head_stack.pop(0))
    else :
        turtle.rt(90)
