from graphics import*

def mouseClick(window,Roll_dice=False):
    while True:
        click=window.getMouse()
        xValue=click.getX()
        yValue=click.getY()
        option=str("")
        ###case: (xValue)>300 and (xValue)<500 and (yValue)>250 and (yValue)<350:
        if (xValue)>10 and (xValue)<90 and (yValue)>310 and (yValue)<390:
            option="play"
            return(option)
        #elif (xValue)>300 and (xValue)<500 and (yValue)>250 and (yValue)<350:
         #   print("This is TuckerBag")
         #   continue
        #elif (xValue)>300 and (xValue)<500 and (yValue)>450 and (yValue)<550:
        #    print("This is Stock Sale")
        #    continue
        #elif    (xValue)>610 and (xValue)<690 and (yValue)>610 and (yValue)<690:
        #    print("This is WoolSale")
        elif  (xValue)>10 and (xValue)<90 and (yValue)>510 and (yValue)<590:
            option="help"
            return(option)
        elif    (xValue)>10 and (xValue)<90 and (yValue)>410 and (yValue)<490:
            option="quit"
            return(option)
        else:
            if Roll_dice==True:
                if (xValue)>250 and (xValue)<340 and (yValue)>410 and (yValue)<450:
                    option=" "
                    return(option)
                elif (xValue)>460 and (xValue)<550  and (yValue)>410 and (yValue)<450:
                    option="i"
                    return(option)
                
            continue

def home_screen():
    win=GraphWin("SQUATTER",800,800)
    win.setBackground(color_rgb(0,255,0))
    message = Text(Point(400,50), "Welcome to Greg's SQUATTER")
    message.setSize(26)
    message.setStyle("bold italic")
    ##owl=Image(Point(50,50),"owl.gif")
    ##owl.draw(win)
    message.setTextColor("blue")
    message.draw(win)
    draw_rectangle(win)
    tucker_bag(win)
    board_spaces(win)
    woolsale(win)
    woman(win,"pink")
    option=mouseClick(win)
    return (option,win)

def entry(window):
    inputBox=Entry(Point(500,300),10)
    inputBox.setTextColor("green")
    inputStr=inputBox.getText()
    while True:
        if inputStr=="okay":
            window.close()
            break
        continue
    return

def playgame():
    print("Okay lets play")
    return

def draw_rectangle(window):
    clickArea=Rectangle(Point(100,100),Point(700,700))
    clickArea.setWidth(6)
    clickArea.draw(window)
    Line(Point(200,100),Point(200,700)).draw(window)
    Line(Point(100,200),Point(700,200)).draw(window)
    Line(Point(600,100),Point(600,700)).draw(window)
    Line(Point(100,600),Point(700,600)).draw(window)
    for x in (200,300,400,500):
        Line(Point(100,x),Point(200,x)).draw(window)
        Line(Point(600,x),Point(700,x)).draw(window)
        Line(Point(x,600),Point(x,700)).draw(window)
        Line(Point(x,100),Point(x,200)).draw(window)
    
def tucker_bag(window):
    tucker=Oval(Point(300,250),Point(500,350))
    stock=Oval(Point(300,450),Point(500,550))
    tucker.setFill("pink")
    stock.setFill("yellow")
    tucker.setOutline("blue")
    tucker.setWidth(3)
    stock.setOutline("blue")
    stock.setWidth(3)
    stock.draw(window)
    tucker.draw(window)
    tuckerText = Text(Point(400,300), "TUCKER BAG")
    tuckerText.setSize(22)
    tuckerText.setStyle("bold italic")
    tuckerText.setTextColor("blue")
    tuckerText.setFace("courier")
    tuckerText.draw(window)
    stockText = Text(Point(400,500), "STOCK SALE")
    stockText.setSize(22)
    stockText.setStyle("bold italic")
    stockText.setTextColor("blue")
    stockText.draw(window)

def woolsale(window):
    symbol=Circle(Point(650,650),40)
    symbol.draw(window)
    symbol.setFill("white")
    woolText=Text(Point(650,640),"WOOL")
    saleText=Text(Point(650,660),"SALE")
    woolText.draw(window)
    saleText.draw(window)
    playGame = symbol.clone()
    playGame.draw(window)
    playGame.move(-600,-300)
    playGame.setFill("green")
    playGame.setOutline(color_rgb(0,255,50))
    playGame.setWidth(2)
    playText=Text(Point(50,340),"PLAY")
    gameText=Text(Point(50,360),"GAME")
    gameText.draw(window)
    gameText.setStyle("bold")
    playText.draw(window)
    playText.setStyle("bold")
    quitGame= symbol.clone()
    quitGame.move(-600,-200)
    quitGame.draw(window)
    quitGame.setOutline(color_rgb(255,0,125))
    quitGame.setWidth(2)
    quitText = Text(Point(50,440),"QUIT")
    qgameText = Text(Point(50,460),"GAME")
    quitText.draw(window)
    qgameText.draw(window)
    quitText.setStyle("bold")
    qgameText.setStyle("bold")
    quitGame.setFill("red")
    instruction=symbol.clone()
    instruction.move(-600,-100)
    instruction.draw(window)
    helpText = Text(Point(50,550),"HELP")
    helpText.draw(window)
    helpText.setStyle("bold")
    instruction.setFill("orange")

def board_spaces(window):
    x=[150,250,350,450,550,650]
    y=[150,250,350,450,550,650]
    textbottom=["BAG","A TURN","SALE","DROUGHT","TAX","SALE","DROUGHT","SALE","TREATMENT","RAIN","BAG","A TURN","BONUS","SALE","BAG","TAX","RAIN","SALE","TREATMENT","TIME"]
    texttop=["TUCKER","MISS","STOCK","SEVERE","INCOME","WOOL","SEVERE","STOCK","FOOTROT","LOCAL","TUCKER","MISS","STUD","STOCK","TUCKER","INCOME","LOCAL","STOCK","FOOTROT","SPRING"]
    symbol=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    for coord in [0,1,2,3,4,5]:
        symbol[coord]=Circle(Point(x[coord],y[5]),40)
        symbol[coord].draw(window)
        symbol[coord].setFill("white")
        Text(Point(x[coord],640),texttop[coord]).draw(window)
        Text(Point(x[coord],660),textbottom[coord]).draw(window)
    for down in range(4):
        symbol[down+6]=Circle(Point(x[0],(y[down]+100)),40)
        symbol[down+6].draw(window)
        symbol[down+6].setFill("white")
        Text(Point(x[0],y[down]+90),texttop[down+6]).draw(window)
        Text(Point(x[0],y[down]+110),textbottom[down+6]).draw(window)
    for top in range(6):
        symbol[top+10]=Circle(Point(x[top],(y[0])),40)
        symbol[top+10].draw(window)
        symbol[top+10].setFill("white")
        Text(Point(x[top],y[0]-10),texttop[top+10]).draw(window)
        Text(Point(x[top],y[0]+10),textbottom[top+10]).draw(window)

    for opp in range(4):
        symbol[opp+16]=Circle(Point(x[5],y[opp+1]),40)
        symbol[opp+16].draw(window)
        symbol[opp+16].setFill("white")
        Text(Point(x[5],y[opp+1]-10),texttop[opp+16]).draw(window)
        Text(Point(x[5],y[opp+1]+10),textbottom[opp+16]).draw(window)

def draw_hexagon(window):
    vertices=[Point(150,77),Point(350,77),Point(450,250),Point(350,423),Point(150,423),Point(50,250)]
    aPolygon = Polygon(vertices)
    aPolygon.setWidth(5)
    aPolygon.draw(window)
    aPolygon.move(75,75)
    return(aPolygon)

def man(window,colour,xmove=0,ymove=0,undraw=False):
    head=Circle(Point(50,50),10)
    neck=Rectangle(Point(45,60),Point(55,65))
    torso=Rectangle(Point(38,65),Point(62,90))
    torso.draw(window)
    head.draw(window)
    neck.draw(window)
    legL=Polygon(Point(42,90),Point(36,110),Point(44,110),Point(50,90))
    legL.draw(window)
    legR=Polygon(Point(50,90),Point(56,110),Point(64,110),Point(58,90))
    legR.draw(window)
    armL=Polygon(Point(38,73),Point(22,65),Point(22,73),Point(38,81))
    armL.draw(window)
    armR=Polygon(Point(62,73),Point(78,65),Point(78,73),Point(62,81))
    armR.draw(window)
    torso.setFill(colour)
    head.setFill("pink")
    legR.setFill("brown")
    legL.setFill("brown")
    armR.setFill("yellow")
    armL.setFill("yellow")
    limbs=[head,neck,torso,legL,legR,armL,armR]
    for limb in limbs:
        limb.move(xmove,ymove)
        update(10)
    if undraw==True:
        head.undraw()
        neck.undraw()
        torso.undraw()
        legL.undraw()
        legR.undraw()
        armL.undraw()
        armR.undraw()

def woman(window,colour):
    head=Circle(Point(50,50),10)
    neck=Rectangle(Point(45,60),Point(55,65))
    torso=Polygon(Point(45,65),Point(38,90),Point(62,90),Point(55,65))
    torso.draw(window)
    head.draw(window)
    neck.draw(window)
    legL=Polygon(Point(42,90),Point(36,110),Point(44,110),Point(50,90))
    legL.draw(window)
    legR=Polygon(Point(50,90),Point(56,110),Point(64,110),Point(58,90))
    legR.draw(window)
    armL=Polygon(Point(42,73),Point(26,65),Point(26,73),Point(40,81))
    armL.draw(window)
    armR=Polygon(Point(58,73),Point(74,65),Point(74,73),Point(60,81))
    armR.draw(window)
    torso.setFill(colour)
    head.setFill("pink")
    legR.setFill("brown")
    legL.setFill("brown")
    armR.setFill("yellow")
    armL.setFill("yellow")
    limbs=[head,neck,torso,legL,legR,armL,armR]
    for limb in limbs:
        limb.move(700,0)
        update(10)

def dice(window,dice1=0,dice2=0):
    square1= Rectangle(Point(300,410),Point(340,450))
    square1.setFill("white")
    square2= square1.clone()
    square2.move(-50,0)
    dot1=Circle(square2.getCenter(),5)
    dot1.setFill("red")
    dot2=Circle(Point(310,420),5)
    dot2.setFill("red")
    dot3=Circle(Point(330,440),5)
    dot3.setFill("red")
    text=Text(Point(295,390),"ROLL DICE")
    if dice1==0:
        square1.draw(window)
        die1(window)
        square2.draw(window)
        dot1.draw(window)
        dot2.draw(window)
        dot3.draw(window)
        text.draw(window)
    else:
        square2.setFill("green")
        square1.draw(window)
        square1.setFill("blue")
        square2.draw(window)
        #print(dice1)
        #print(dice2)
    if dice2==1:
        die1(window)
    elif dice2==2:
        die2(window)
    elif dice2==3:
        die3(window)
    elif dice2==4:
        die4(window)
    elif dice2==5:
        die5(window)
    elif dice2==6:
        die6(window)
    if dice1==1:
        die1(window,2)
    elif dice1==2:
        die2(window,2)
    elif dice1==3:
        die3(window,2)
    elif dice1==4:
        die4(window,2)
    elif dice1==5:
        die5(window,2)
    elif dice1==6:
        die6(window,2)      

def die1(window,die=1):
    dot=Circle(Point(320,430),5)
    dot.setFill("red")
    if die==1:
        dot.draw(window)
    else:
        dot=dot.clone()
        dot.move(-50,0)
        dot.draw(window)

def die2(window,die=1):
    dot1=Circle(Point(310,420),5)
    dot1.setFill("red")
    dot2=Circle(Point(330,440),5)
    dot2.setFill("red")
    if die==1:
        dot1.draw(window)
        dot2.draw(window)
    else:
        dot1=dot1.clone()
        dot1.move(-50,0)
        dot1.draw(window)
        dot2=dot2.clone()
        dot2.move(-50,0)
        dot2.draw(window)

def die3(window,die=1):
    die2(window,die)
    die1(window,die)

def die4(window,die=1):
    die2(window,die)
    dot3=Circle(Point(310,440),5)
    dot3.setFill("red")
    dot4=Circle(Point(330,420),5)
    dot4.setFill("red")
    if die==1:
        dot3.draw(window)
        dot4.draw(window)
    else:
        dot3=dot3.clone()
        dot3.move(-50,0)
        dot3.draw(window)
        dot4=dot4.clone()
        dot4.move(-50,0)
        dot4.draw(window)

def die5(window,die=1):
    die4(window,die)
    die1(window,die)

def die6(window,die=1):
    die4(window,die)
    dot5=Circle(Point(310,430),5)
    dot5.setFill("red")
    dot6=Circle(Point(330,430),5)
    dot6.setFill("red")
    if die==1:
        dot5.draw(window)
        dot6.draw(window)
    else:
        dot5=dot5.clone()
        dot5.move(-50,0)
        dot5.draw(window)
        dot6=dot6.clone()
        dot6.move(-50,0)
        dot6.draw(window)

def info(window):
    box=Rectangle(Point(460,410),Point(550,450))
    box.setFill("orange")
    box.draw(window)
    text=Text(box.getCenter(),"INFO")
    text.setStyle("bold")
    text.setTextColor("purple")
    text.draw(window)
"""
window=GraphWin("SQUATTER",800,800)
window.setBackground(color_rgb(0,255,0))
head=Circle(Point(50,50),10)
neck=Rectangle(Point(45,60),Point(55,65))
torso=Rectangle(Point(38,65),Point(62,90))
legL=Polygon(Point(42,90),Point(36,110),Point(44,110),Point(50,90))
legR=Polygon(Point(50,90),Point(56,110),Point(64,110),Point(58,90))
armL=Polygon(Point(38,73),Point(22,65),Point(22,73),Point(38,81))
armR=Polygon(Point(62,73),Point(78,65),Point(78,73),Point(62,81))
torso.setFill("blue")
head.setFill("pink")
legR.setFill("brown")
legL.setFill("brown")
armR.setFill("yellow")
armL.setFill("yellow")

movement=[(0,0),(-100,0),(-200,0)]

#legL.draw(window)
#legR.draw(window)
#armR.draw(window)
#armL.draw(window)
#torso.draw(window)
#head.draw(window)
#neck.draw(window)
limbs=[head,neck,torso,legL,legR,armL,armR]

for object in limbs:
    object.draw(window)

for limb in limbs:
        limb.move(500,100)
        update(10)
for limb in limbs:
    limb.move(movement[1][0],movement[1][1])
    update(8)

for limb in limbs:
    limb.move(-movement[1][0],-movement[1][1])

def movingman(xmove,ymove,draw=True):
    for limb in limbs:
        limb.move(xmove,ymove)
        update(8)
        if draw==False:
            limb.undraw()

movingman(-50,-200)

movingman(300,200,False)

movingman(-200,50)
window.getMouse()
"""