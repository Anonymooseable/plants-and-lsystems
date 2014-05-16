#Ce fichier est un test des L-systemes sensitives au contexte, c'est-à-dire,
#dont les règles varient selon une caracteristique du contexte (dans ce cas, la
#règle pour le symbole "1" dépend du symbole qui précède et du symbole qui suit).

import turtle
#------génération du L-syteme------
li=[0]
for i in range(5):
    gen = []
    for i in range(len(li)):
        if li[i] == 0:
            gen.extend([1,'push','left','div',0,'pop',1,"+",'right',0,"-",'restore',0])
        elif li[i] == 1:
            if li[i-1] == 1 and li[i+1] == 1: #cela limite la grossissement des segments
                gen.append(li[i])
            else:
                gen.extend([1,1])
        elif li[i] == 'div':
            gen.extend(['div', 'add'])
        else:
            gen.append(li[i])
    li = gen
print(li)
#------dessin---------
#positionement initiale
turtle.speed(0)
turtle.lt(90)
turtle.pu()
turtle.sety(-270)
turtle.pd()

#stacks
pos_stack=list()
head_stack=list()
main_pos_stack=list()
main_head_stack=list()
fd_stack=[10]

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
