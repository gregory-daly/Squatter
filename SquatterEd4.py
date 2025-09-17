### Basic Squatter Game
### Author: Greg Daly
### Date Created: 30/09/22
### Edition 1.1 - With Drought W.I.P.
### Edition 2.0 - Graphics Added
### Edition 2.1 - Full two/one game feature with graphics (14/10/22)
### Edition 3.0 - Sounds added including intro, quit, drought, birthday and tick.
### Edition 4.0 - Full two/one game feature with graphics. Sound removed. Bugs fixed (Cant stock with bonus Stock sale while in drought) (5/7/24)
"""
This is a basic squatter game, with a small rectangular board of 20 squares.
Stockyard has 10 sale and 10 buy options
Tucker bag has 10 cards.
There are NO Paddocks, only sheep.
OBJECTIVE: Amass 50 sheep.
START UP: You have $100, and 5 sheep. You must buy and sell sheep and collect "WOOL SALE" to earn
income and eventually accumulate 50 sheep.
"""

from graphics import *
from graph_demo import *


def roll_dice():
    import random
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2)


rolls = []
roll = int()
sum = int()

### Player information
player1_sheep = int(5)
player1_money = float(100)
player1_position = int(0)

### Player Figure

head = Circle(Point(650, 625), 10)
head2 = head.clone()
neck = Rectangle(Point(645, 635), Point(655, 640))
neck2 = neck.clone()
torso = Rectangle(Point(638, 640), Point(662, 665))
torso2 = torso.clone()
legL = Polygon(Point(642, 665), Point(636, 685), Point(644, 685), Point(650, 665))
legL2 = legL.clone()
legR = Polygon(Point(650, 665), Point(656, 685), Point(664, 685), Point(658, 665))
legR2 = legR.clone()
armL = Polygon(Point(638, 648), Point(622, 640), Point(622, 648), Point(638, 656))
armL2 = armL.clone()
armR = Polygon(Point(662, 648), Point(678, 640), Point(678, 648), Point(662, 656))
armR2 = armR.clone()
torso.setFill("blue")
torso2.setFill("black")
head2.setFill("pink")
head.setFill("pink")
legR.setFill("brown")
legR2.setFill("brown")
legL.setFill("brown")
legL2.setFill("brown")
armR.setFill("yellow")
armR2.setFill("yellow")
armL.setFill("yellow")
armL2.setFill("yellow")
limbs = [head, neck, torso, legL, legR, armL, armR]
limbs2 = [head2, neck2, torso2, legL2, legR2, armL2, armR2]

movement = [(0, 0), (-100, 0), (-200, 0), (-300, 0), (-400, 0), (-500, 0), (-500, -100), (-500, -200), (-500, -300),
            (-500, -400), (-500, -500), (-400, -500), (-300, -500), (-200, -500), (-100, -500), (0, -500), (0, -400),
            (0, -300), (0, -200), (0, -100)]

# Stock sale cards

stock_buys = (30, 35, 40, 45, 50, 55, 60, 65, 70, 75)
stock_sells = (50, 55, 60, 65, 70, 75, 80, 85, 90, 95)

# Board functions

def woolsale(money, sheep):
    """calculate woolsale
    """
    woolsale = int()
    if sheep == 0:
        woolsale = 0
    else:
        woolsale = 50 + sheep * 5
    woolWin = GraphWin("WoolSale", 250, 250)
    woolWin.setBackground(color_rgb(250, 250, 0))
    woolText = Text(Point(125, 75), "IT'S WOOLSALE!!")
    woolInfo = Text(Point(125, 125), " You earned $ %g " % woolsale)
    woolText.setStyle("bold")
    woolText.setTextColor("green")
    woolInfo.setStyle("bold")
    woolInfo.setTextColor("blue")
    woolInfo.setSize(20)
    woolText.setSize(18)
    woolText.draw(woolWin)
    woolInfo.draw(woolWin)
    Text(Point(125, 180), "Click to close").draw(woolWin)
    woolWin.getMouse()
    woolWin.close()
    money = money + woolsale
    return (money, sheep)


def stock_sale(money, sheep, drought):
    """random list from stock sale/buy
    """
    import random
    buy_value = stock_buys[random.randint(0, 7)]
    sell_value = stock_sells[random.randint(0, 7)]
    stockWin = GraphWin("StockSale", 400, 400)
    stockWin.setBackground(color_rgb(0, 255, 100))
    stockText = Text(Point(200, 75), "It's STOCK SALE TIME! \n \nYou have $%d and %g sheep" % (money, sheep))
    stockText.setStyle("bold")
    stockText.setTextColor("white")
    stockText.setSize(18)
    stockText.draw(stockWin)
    Text(Point(200, 350), "Click to close").draw(stockWin)
    if drought == True:
        droughtText = Text(Point(200, 200), "Sorry, you're in DROUGHT. \nYou can not buy/sell stock")
        droughtText.setStyle("bold")
        droughtText.setTextColor("red")
        droughtText.draw(stockWin)
        stockWin.getMouse()
        stockWin.close()
        return (money, sheep)

    priceText = Text(Point(200, 170),
                     "You can BUY sheep at $%g \n\nYou can SELL sheep at $%g" % (buy_value, sell_value))
    priceText.setStyle("bold italic")
    priceText.setTextColor("blue")
    priceText.setSize(20)
    priceText.draw(stockWin)
    buyText = Text(Point(100, 300), "BUY")
    sellText = Text(Point(300, 300), "SELL")
    buyText.setStyle("bold")
    sellText.setStyle("bold")
    buyText.setSize(22)
    sellText.setSize(22)

    buyOval = Oval(Point(60, 280), Point(140, 320))
    buyOval.setOutline("yellow")
    buyOval.setFill("green")
    buyOval.draw(stockWin)
    sellOval = Oval(Point(260, 280), Point(340, 320))
    sellOval.setFill("pink")
    sellOval.setOutline("yellow")
    sellOval.draw(stockWin)
    buyText.draw(stockWin)
    sellText.draw(stockWin)

    while True:
        click = stockWin.getMouse()
        xValue = click.getX()
        yValue = click.getY()
        if (xValue) > 60 and (xValue) < 140 and (yValue) > 280 and (yValue) < 320:
            (money, sheep) = stock_buy(buy_value, money, sheep)
            stockWin.close()
            return (money, sheep)
        elif (xValue) > 260 and (xValue) < 340 and (yValue) > 280 and (yValue) < 320:
            (money, sheep) = stock_sell(sell_value, money, sheep)
            stockWin.close()
            return (money, sheep)
        else:
            stockWin.close()
            return (money, sheep)


def stock_buy(buy, money, sheep):
    buyWin = GraphWin("BUY", 300, 300)
    buyWin.setBackground(color_rgb(0, 100, 200))
    buyText = Text(Point(150, 75), "How many sheep \n would you like to buy?")
    buyText.setStyle("bold")
    buyText.setTextColor("white")
    buyText.setSize(18)
    buyText.draw(buyWin)
    Text(Point(200, 350), "Click to close").draw(buyWin)
    inputBox = Entry(Point(150, 150), 3)
    inputBox.setTextColor("orange")
    inputBox.draw(buyWin)

    while True:
        buyWin.getMouse()
        no_sheep = inputBox.getText()
        if no_sheep == "":
            continue
        try:
            no_sheep = int(no_sheep)
            cost = no_sheep * buy
            if (money - cost) < 0:
                afford = Text(Point(150, 200), "YOU CAN'T AFFORD THAT!")
                afford.draw(buyWin)
                for time in range(100000000):
                    time = time + 1
                    continue
                afford.undraw()
                continue
        except:
            integer = Text(Point(150, 200), "MUST BE AN INTEGER")
            integer.draw(buyWin)
            for time in range(100000000):
                time = time + 1
                continue
            integer.undraw()
            continue

        bought = Text(Point(150, 200), "You are buying %g \n Which cost $%g" % (no_sheep, cost))
        bought.setSize(18)
        bought.draw(buyWin)
        confirmbox = Rectangle(Point(40, 240), Point(120, 270))
        confirmbox.setFill("yellow")
        confirmbox.draw(buyWin)
        cancelbox = Rectangle(Point(180, 240), Point(260, 270))
        cancelbox.setFill("pink")
        cancelbox.draw(buyWin)
        Text(Point(80, 250), "CONFIRM").draw(buyWin)
        Text(Point(220, 250), "CANCEL").draw(buyWin)

        while True:
            click = buyWin.getMouse()
            yValue = click.getY()
            xValue = click.getX()
            if (xValue) > 40 and (xValue) < 120 and (yValue) > 240 and (yValue) < 270:
                money = money - cost
                sheep = sheep + no_sheep
                buyWin.close()
                return (money, sheep)
            if (xValue) > 180 and (xValue) < 260 and (yValue) > 240 and (yValue) < 270:
                buyWin.close()
                return (money, sheep)
            else:
                continue


def stock_sell(sell, money, sheep):
    sellWin = GraphWin("BUY", 300, 300)
    sellWin.setBackground(color_rgb(255, 100, 200))
    sellText = Text(Point(150, 75), "How many sheep \n would you like to sell?")
    sellText.setStyle("bold")
    sellText.setTextColor("white")
    sellText.setSize(18)
    sellText.draw(sellWin)
    Text(Point(200, 350), "Click to close").draw(sellWin)
    inputBox = Entry(Point(150, 150), 3)
    inputBox.setTextColor("orange")
    inputBox.draw(sellWin)

    while True:
        sellWin.getMouse()
        no_sheep = inputBox.getText()
        if no_sheep == "":
            continue
        try:
            no_sheep = int(no_sheep)
            profit = no_sheep * sell
            if (sheep - no_sheep) < 0:
                afford = Text(Point(150, 200), "YOU DON'T HAVE THAT MANY SHEEP!")
                afford.draw(sellWin)
                for time in range(100000000):
                    time = time + 1
                    continue
                afford.undraw()
                continue
        except:
            integer = Text(Point(150, 200), "MUST BE AN INTEGER")
            integer.draw(sellWin)
            for time in range(100000000):
                time = time + 1
                continue
            integer.undraw()
            continue

        bought = Text(Point(150, 200), "You are selling %g \n Which makes $%g" % (no_sheep, profit))
        bought.setSize(18)
        bought.draw(sellWin)
        confirmbox = Rectangle(Point(40, 240), Point(120, 270))
        confirmbox.setFill("yellow")
        confirmbox.draw(sellWin)
        cancelbox = Rectangle(Point(180, 240), Point(260, 270))
        cancelbox.setFill("pink")
        cancelbox.draw(sellWin)
        Text(Point(80, 250), "CONFIRM").draw(sellWin)
        Text(Point(220, 250), "CANCEL").draw(sellWin)

        while True:
            click = sellWin.getMouse()
            yValue = click.getY()
            xValue = click.getX()
            if (xValue) > 40 and (xValue) < 120 and (yValue) > 240 and (yValue) < 270:
                money = money + profit
                sheep = sheep - no_sheep
                sellWin.close()
                return (money, sheep)
            if (xValue) > 180 and (xValue) < 260 and (yValue) > 240 and (yValue) < 270:
                sellWin.close()
                return (money, sheep)
            else:
                continue


def miss_turn(miss, player):
    """ player misses one or 2 turns\
    """
    missWin = GraphWin("Miss Turn", 300, 300)
    missWin.setBackground(color_rgb(255, 0, 100))
    missText = Text(Point(150, 150), "You miss a turn")
    missText.setStyle("bold")
    missText.setTextColor("white")
    missText.setSize(18)
    missText.draw(missWin)
    missWin.getMouse()
    miss = True
    missWin.close()
    return (miss)


def drought(money, sheep):
    """ player is on drought for 1 rotations of board. Sell half of stock at $40 per pen
    """
    droughtWin = GraphWin("Drought", 300, 300)
    droughtWin.setBackground(color_rgb(255, 255, 0))
    droughtText = Text(Point(150, 75), "*** You're in DROUGHT***")
    droughtText.setStyle("bold")
    droughtText.setTextColor("red")
    droughtText.setSize(18)
    info = Text(Point(150, 150),
                "You must sell half your stock @ $40/pen.\n And you cannot restock until you complete\n on full turn of the board,\n unless you land on 'local rain'")
    info.draw(droughtWin)
    droughtText.draw(droughtWin)
    money = int(money + (sheep * 0.5 * 40))
    sheep = int(sheep * 0.5)
    # print("You now have $",money," and ",sheep,"sheep.")
    drought = True
    drought_position = 0
    droughtWin.getMouse()
    droughtWin.close()
    return (money, sheep, drought, drought_position)


def footrot(money, sheep):
    Win = GraphWin("Footrot", 300, 300)
    Win.setBackground(color_rgb(255, 255, 0))
    footText = Text(Point(150, 75), "*** You're have footrot\n You must by $50 in fees***")
    footText.setStyle("bold")
    footText.setTextColor("red")
    footText.setSize(18)
    footText.draw(Win)
    if money > 50:
        money = money - 50
    else:
        money = money * 0.5
    Win.getMouse()
    Win.close()
    return (money, sheep)


def rainScreen():
    droughtWin = GraphWin("Rain ends drought", 300, 300)
    droughtWin.setBackground(color_rgb(0, 150, 150))
    droughtText = Text(Point(150, 75), "Your drought has Ended.\n HURRAH!")
    droughtText.setStyle("bold")
    droughtText.setTextColor("white")
    droughtText.setSize(18)
    droughtText.draw(droughtWin)
    Text(Point(125, 180), "Click to close").draw(droughtWin)
    droughtWin.getMouse()
    droughtWin.close()
    return


def tucker_bag(miss, player, money, sheep, drought, drought_position):
    """Player picks up from a random list of tucker bag"""
    import random
    tucker_rand = random.randint(0, 9)
    # tucker_rand=3  # Fix Tucker bag category if required to fix bugs
    if tucker_rand == 0:
        miss = tucker_bags[0](miss, player)
        return (miss, player, money, sheep, drought, drought_position)
    if tucker_rand == 1:
        (money, sheep, drought, drought_position) = tucker_bags[1](money, sheep)
        return (miss, player, money, sheep, drought, drought_position)
    if tucker_rand == 4:
        drought = tucker_bags[4](drought)
        return (miss, player, money, sheep, drought, drought_position)
    if tucker_rand == 3:
        (money, sheep, drought) = tucker_bags[3](money, sheep, drought)
        return (miss, player, money, sheep, drought, drought_position)
    (money, sheep) = tucker_bags[tucker_rand](money, sheep)
    return (miss, player, money, sheep, drought, drought_position)


# Tucker Bag additional functions.

def rain(drought):
    """Player ends drought"""
    if drought == True:
        rainScreen()
        drought = False
    else:
        rainWin = GraphWin("Rain", 300, 300)
        rainWin.setBackground(color_rgb(0, 150, 150))
        rainText = Text(Point(150, 75), "Its Raining Time")
        rainText.setStyle("bold")
        rainText.setTextColor("white")
        rainText.setSize(18)
        rainText.draw(rainWin)
        Text(Point(125, 180), "Click to close").draw(rainWin)
        rainWin.getMouse()
        rainWin.close()
    return (drought)


def dog_kills_sheep(money, sheep):
    """Player loses 3 sheep"""
    dogWin = GraphWin("Wild dogs", 300, 300)
    dogWin.setBackground("orange")
    dogText = Text(Point(150, 75), "### Wild dogs kill 3 sheep ###")
    dogText.setStyle("bold")
    dogText.setTextColor("black")
    dogText.setSize(18)
    dogText.draw(dogWin)
    sheep = sheep - 3
    if sheep < 0:
        sheep = 0
    # print("You now have ",sheep," sheep")
    dogWin.getMouse()
    dogWin.close()
    return (money, sheep)


def bonus_stockyard(money, sheep, drought):
    """Player gets 20% increase in buy/sell stock"""
    stockWin = GraphWin("Bonus StockSale", 400, 400)
    stockWin.setBackground(color_rgb(0, 255, 100))
    stockText = Text(Point(200, 75), "It's BONUS STOCKYARD! \nYou have $%d and %g sheep" % (money, sheep))
    infoText = Text(Point(200, 120), "Your buying or selling price\nis increased by 20%")
    infoText.draw(stockWin)
    stockText.setStyle("bold")
    stockText.setTextColor("white")
    stockText.setSize(18)
    stockText.draw(stockWin)
    Text(Point(200, 350), "Click to close").draw(stockWin)
    if drought == True:
        droughtText = Text(Point(200, 200), "Sorry, you're in DROUGHT. \nYou can not buy/sell stock")
        droughtText.setStyle("bold")
        droughtText.setTextColor("red")
        droughtText.draw(stockWin)
        stockWin.getMouse()
        stockWin.close()
        return (money, sheep, drought)
    import random
    buy_value = stock_buys[random.randint(0, 7)]
    sell_value = stock_sells[random.randint(0, 7)]
    buy_per = int(buy_value * 0.2)
    sell_per = int(sell_value * 0.2)
    buy_price = buy_value + buy_per
    sell_price = sell_value + sell_per
    priceText = Text(Point(200, 200),
                     "You can BUY sheep at $%g\nPlus 20 per = $%d\nYou can SELL sheep at $%g\nPlus 20 per = $%d" % (
                     buy_value, buy_per, sell_value, sell_per))
    priceText.setStyle("bold italic")
    priceText.setTextColor("blue")
    priceText.setSize(20)
    priceText.draw(stockWin)

    buyText = Text(Point(100, 300), "BUY")
    sellText = Text(Point(300, 300), "SELL")
    buyText.setStyle("bold")
    sellText.setStyle("bold")
    buyText.setSize(22)
    sellText.setSize(22)

    buyOval = Oval(Point(60, 280), Point(140, 320))
    buyOval.setOutline("yellow")
    buyOval.setFill("green")
    buyOval.draw(stockWin)
    sellOval = Oval(Point(260, 280), Point(340, 320))
    sellOval.setFill("pink")
    sellOval.setOutline("yellow")
    sellOval.draw(stockWin)
    buyText.draw(stockWin)
    sellText.draw(stockWin)

    while True:
        click = stockWin.getMouse()
        xValue = click.getX()
        yValue = click.getY()
        if (xValue) > 60 and (xValue) < 140 and (yValue) > 280 and (yValue) < 320:
            (money, sheep) = stock_buy(buy_price, money, sheep)
            stockWin.close()
            return (money, sheep, drought)
        elif (xValue) > 260 and (xValue) < 340 and (yValue) > 280 and (yValue) < 320:
            (money, sheep) = stock_sell(sell_price, money, sheep)
            stockWin.close()
            return (money, sheep, drought)
        else:
            stockWin.close()
            return (money, sheep, drought)


def stud(money, sheep):
    """Stud farm produces 3 sheep"""
    studWin = GraphWin("Stud Farm", 300, 300)
    studWin.setBackground("orange")
    studText = Text(Point(150, 150), "You get bonus stud work\nReceive 3 extra sheep!")
    studText.setStyle("bold")
    studText.setTextColor("black")
    studText.setSize(18)
    studText.draw(studWin)
    sheep = sheep + 3
    # print("You now have ",sheep, "sheep")
    studWin.getMouse()
    studWin.close()
    return (money, sheep)


def income_tax(money, sheep):
    """Player pays income tax!"""
    taxWin = GraphWin("Income Tax", 300, 300)
    taxWin.setBackground("red")
    taxText = Text(Point(150, 75), "You must pay income tax! \n10% of cash + \n $5 per head of stock")
    taxText.setStyle("bold")
    taxText.setTextColor("black")
    taxText.setSize(18)
    taxText.draw(taxWin)
    tax = int(money * 0.1 + sheep * 5)
    money = money - tax
    if money < 0:
        money = 0
    Text(Point(150, 200), "You pay $%g. You now have $%d" % (tax, money)).draw(taxWin)
    taxWin.getMouse()
    taxWin.close()
    return (money, sheep)


def birthday(money, sheep):
    """Players birthday, get an extra go"""
    birthWin = GraphWin("Birthday", 300, 300)
    birthWin.setBackground("yellow")
    birthText = Text(Point(150, 75), "###Its your birthday!###\n\n\nReceive a $100 gift\n from the Alan's Centrelink")
    birthText.setStyle("bold")
    birthText.setTextColor("pink")
    birthText.setSize(18)
    birthText.draw(birthWin)
    # happy() - Command commented out due to bugs with playsound module. G.D. 4/7/24
    Text(Point(200, 200), "Click to close").draw(birthWin)
    money = money + 100
    birthWin.getMouse()
    birthWin.close()
    return money, sheep


def tractor_repairs(money, sheep):
    """Player must repair tractor"""
    tractorWin = GraphWin("Tractor", 300, 300)
    tractorWin.setBackground("brown")
    header = Text(Point(150, 75), "TRACTOR REPAIRS")
    header.setSize(20)
    header.setTextColor("yellow")
    header.draw(tractorWin)
    tractorText = Text(Point(150, 150),
                       "Your tractor needs repairing\nYou must Pay $150\nor your total cash\n(if less than $150")
    tractorText.setStyle("bold")
    tractorText.setTextColor("pink")
    tractorText.setSize(14)
    tractorText.draw(tractorWin)
    money = money - 150
    if money < 0:
        money = 0
    tractorWin.getMouse()
    tractorWin.close()
    return (money, sheep)


def adjistment_fees(money, sheep):
    """player has adjistment fees"""
    feesWin = GraphWin("Fees", 400, 300)
    feesWin.setBackground("yellow")
    feesText = Text(Point(200, 75), "###You must pay agistment fees###\n")
    infoText = Text(Point(200, 150),
                    "Due to mismanagement, \nyou must pay $100 to Christie's Centrelink.\nIf you have less than $100, you pay half your cash total")
    infoText.draw(feesWin)
    feesText.setStyle("bold")
    feesText.setTextColor("pink")
    feesText.setSize(18)
    feesText.draw(feesWin)
    if money > 100:
        money = money - 100
    else:
        money = money * 0.5
    feesWin.getMouse()
    feesWin.close()
    return (money, sheep)


### Board and tucker bag lists

board_spaces = [woolsale, income_tax, drought, stock_sale, miss_turn, tucker_bag, rain, footrot, stock_sale, drought,
                tucker_bag, miss_turn, stud, stock_sale, tucker_bag, income_tax, rain, stock_sale, footrot, rain]
tucker_bags = [miss_turn, drought, dog_kills_sheep, bonus_stockyard, rain, stud, income_tax, birthday, tractor_repairs,
               adjistment_fees]


def play(window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position, player=1,
         end=False):
    if end == False:
        while True:
            if player_sheep >= 50:
                winGame(window, player_name)
                window.close()
                quit_game(player_position, player)
                end = True
                return (
                window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                player, end)
            name = Text(Point(400, 380), ("OK", player_name))
            name.draw(window)
            Text(Point(400, 400), "YOUR TURN").draw(window)
            info(window)
            space_bar = mouseClick(window, True)
            name.undraw()
            if space_bar == "quit":
                window.close()
                quit_game(player_position, player)
                end = True
                return (
                window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                player, end)
            elif space_bar == "help":
                help()
            elif space_bar == ("i"):
                info_win(player_money, player_sheep, drought)
                continue
            elif space_bar == (" "):
                (roll1, roll2) = roll_dice()
                roll = roll1 + roll2
                dice(window, dice1=roll1, dice2=roll2)
                if player == 1 or player == 3:
                    for limb in limbs:
                        limb.move(-(movement[player_position][0]), -(movement[player_position][1]))
                else:
                    for limb in limbs2:
                        limb.move(-(movement[player_position][0]), -(movement[player_position][1]))
                player_position = (player_position + roll)
                if drought == True:
                    drought_position = drought_position + roll
                    if drought_position > 20:
                        rainScreen()
                        # print("\n Your drought has ended, Hurrah")
                        drought = False
                if player_position >= 20:
                    (player_money, player_sheep) = board_spaces[0](player_money, player_sheep)
                    if player_sheep >= 50:
                        print("You now have 50 or more sheep")
                        print("You won!")
                        quit_game(player_position, player)
                    player_position = (player_position) % 20
                if player == 1 or player == 3:
                    for limb in limbs:
                        limb.move(movement[player_position][0], movement[player_position][1])
                        update(20)
                else:
                    for limb in limbs2:
                        limb.move(movement[player_position][0], movement[player_position][1])
                        update(20)

                if player_position == 0:
                    return (
                    window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                    player, end)
                elif player_position == 4 or player_position == 11:
                    miss = board_spaces[4](miss, player_name)
                    return (
                    window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                    player, end)
                elif player_position == 5 or player_position == 10 or player_position == 14:
                    while True:
                        helpText = Text(Point(400, 580), ("CLICK ON TUCKER BAG CARD"))
                        helpText.setTextColor("pink")
                        helpText.setStyle("bold")
                        helpText.draw(window)
                        click = window.getMouse()
                        xValue = click.getX()
                        yValue = click.getY()
                        if (xValue) > 300 and (xValue) < 500 and (yValue) > 250 and (yValue) < 350:
                            helpText.undraw()
                            (miss, player_name, player_money, player_sheep, drought, drought_position) = board_spaces[
                                5](miss, player_name, player_money, player_sheep, drought, drought_position)
                            return (window, miss, player_name, player_position, player_money, player_sheep, drought,
                                    drought_position, player, end)
                        else:
                            helpText.undraw()
                            continue

                elif player_position == 3 or player_position == 8 or player_position == 13 or player_position == 17:
                    while True:
                        helpText = Text(Point(400, 580), ("CLICK ON STOCK SALE CARD"))
                        helpText.setTextColor("yellow")
                        helpText.setStyle("bold")
                        helpText.draw(window)
                        click = window.getMouse()
                        xValue = click.getX()
                        yValue = click.getY()
                        if (xValue) > 300 and (xValue) < 500 and (yValue) > 450 and (yValue) < 550:
                            helpText.undraw()
                            # someObject.undraw()
                            (player_money, player_sheep) = board_spaces[3](player_money, player_sheep, drought)
                            if player_sheep >= 50:
                                winGame(window, player_name)
                                window.close()
                                quit_game(player_position, player)
                                end = True
                                return (window, miss, player_name, player_position, player_money, player_sheep, drought,
                                        drought_position, player, end)
                            return (window, miss, player_name, player_position, player_money, player_sheep, drought,
                                    drought_position, player, end)
                        else:
                            helpText.undraw()
                            continue
                elif player_position == 2 or player_position == 9:
                    (player_money, player_sheep, drought, drought_position) = board_spaces[2](player_money,
                                                                                              player_sheep)
                    return (
                    window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                    player, end)
                elif player_position == 6 or player_position == 16 or player_position == 19:
                    drought = board_spaces[6](drought)
                    return (
                    window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                    player, end)
                else:
                    (player_money, player_sheep) = board_spaces[player_position](player_money, player_sheep)

                    if player_sheep >= 50:
                        winGame(window, player_name)
                        window.close()
                        quit_game(player_position, player)
                        end = True
                        return (window, miss, player_name, player_position, player_money, player_sheep, drought,
                                drought_position, player, end)
                if player_sheep >= 50:
                    print("You now have 50 or more sheep")
                    winGame(window, player_name)
                    window.close()
                    quit_game(player_position, player)
                    end = True
                    return (
                    window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                    player, end)
                return (
                window, miss, player_name, player_position, player_money, player_sheep, drought, drought_position,
                player, end)
    else:
        quit_game(player_position, player)
        main()


def player_turn(window, turn, player1, player2):
    first1_time = True
    first2_time = True
    players1 = player1
    players2 = player2
    end = False
    miss = False
    while True:
        if turn == 1:
            if first1_time == True:
                (window, miss, player1, position1, money1, sheep1, drought1, drought_position1, turn, end) = play(
                    window, False, players1, 0, 100, 5, False, 0, turn, end)
                turn = -1
                first1_time = False
            else:
                if miss == False:
                    (window, miss, player1, position1, money1, sheep1, drought1, drought_position1, turn, end) = play(
                        window, False, players1, position1, money1, sheep1, drought1, drought_position1, turn, end)
                    turn = -1
                else:
                    (window, miss, player1, position1, money1, sheep1, drought1, drought_position1, turn, end) = play(
                        window, False, players1, position1, money1, sheep1, drought1, drought_position1, turn, end)
                    if miss == True:
                        turn = -1
                        continue
                    miss = False
                continue
        else:
            if first2_time == True:
                (window, miss, players2, position2, money2, sheep2, drought2, drought_position2, turn, end) = play(
                    window, False, players2, 0, 100, 5, False, 0, turn, end)
                turn = 1
                first2_time = False
            else:
                if miss == False:
                    (window, miss, players2, position2, money2, sheep2, drought2, drought_position2, turn, end) = play(
                        window, False, player2, position2, money2, sheep2, drought2, drought_position2, turn, end)
                    turn = 1
                else:
                    (window, miss, players2, position2, money2, sheep2, drought2, drought_position2, turn, end) = play(
                        window, False, player2, position2, money2, sheep2, drought2, drought_position2, turn, end)
                    if miss == True:
                        turn = 1
                    miss = False
                continue


def help():
    helpScreen = GraphWin("SQUATTER", 400, 300)
    helpScreen.setBackground(color_rgb(0, 0, 250))
    message = Text(Point(200, 75),
                   "INSTRUCTIONS \n\nYou start with $100 and 5 head of sheep\n The object of the game is to gather 50 head of sheep\n by buying and selling sheep at a profit\n and collecting woolsale\nClick dice to roll.")
    message.setStyle("bold")
    message.draw(helpScreen)
    helpScreen.getMouse()
    helpScreen.close()


def info_win(money, sheep, drought):
    win = GraphWin("Player Info", 300, 300)
    win.setBackground(color_rgb(250, 250, 0))
    moneyText = Text(Point(150, 75), "You have $ %g " % money)
    moneyText.setStyle("bold")
    moneyText.setTextColor("green")
    moneyText.draw(win)
    info = str("You have %d sheep" % sheep)
    sheepText = Text(Point(150, 200), info)
    sheepText.setStyle("bold")
    sheepText.setTextColor("green")
    sheepText.draw(win)
    if drought == True:
        droughtText = Text(Point(150, 150), "YOU ARE IN DROUGHT")
        droughtText.setStyle("bold")
        droughtText.setTextColor("red")
        droughtText.draw(win)
    win.getMouse()
    win.close()


def play_2(window):
    name1 = GraphWin("Player1", 250, 250)
    name1.setBackground(color_rgb(250, 0, 250))
    message1 = Text(Point(125, 75), "Player 1\nWhat is your name?")
    Text(Point(125, 180), "Click to close").draw(name1)
    message1.setStyle("bold")
    message1.draw(name1)
    inputBox = Entry(Point(125, 125), 15)
    inputBox.setTextColor("yellow")
    inputBox.draw(name1)
    while True:
        name1.getMouse()
        player1 = inputBox.getText()
        name1.close()
        break
    name2 = GraphWin("Player2", 250, 250)
    name2.setBackground(color_rgb(0, 0, 250))
    message2 = Text(Point(125, 75), "Player 2\nWhat is your name?")
    Text(Point(125, 180), "Click to close").draw(name2)
    message2.setStyle("bold")
    message2.draw(name2)
    inputBox = Entry(Point(125, 125), 15)
    inputBox.setTextColor("yellow")
    inputBox.draw(name2)
    dice(window)
    while True:
        name2.getMouse()
        player2 = inputBox.getText()
        name2.close()
        break

    rollText = Text(Point(400, 230), ("Please Roll to see he goes first"))
    rollText.draw(window)
    Text1 = Text(Point(400, 370), "Okay " + player1 + " your turn to roll")
    Text1.draw(window)

    while True:
        while True:
            click = window.getMouse()
            xValue = click.getX()
            yValue = click.getY()
            if (xValue) > 250 and (xValue) < 340 and (yValue) > 410 and (yValue) < 450:
                (roll1, roll2) = roll_dice()
                roll_player1 = roll1 + roll2
                dice(window, dice1=roll1, dice2=roll2)
                break
        Text1.setText("Okay " + player2 + " your turn to roll")
        while True:
            click = window.getMouse()
            xValue = click.getX()
            yValue = click.getY()
            if (xValue) > 250 and (xValue) < 340 and (yValue) > 410 and (yValue) < 450:
                (roll1, roll2) = roll_dice()
                roll_player2 = roll1 + roll2
                dice(window, dice1=roll1, dice2=roll2)
                break

        if roll_player1 > roll_player2:
            rollText.setText("Okay " + player1 + ", you go first")
            for x in range(1000000):
                continue
            rollText.undraw()
            Text1.undraw()
            player_turn(window, 1, player1, player2)
        elif roll_player1 < roll_player2:
            rollText.setText("Okay " + player2 + ", you go first")
            for x in range(1000000):
                continue
            rollText.undraw()
            Text1.undraw()
            player_turn(window, 2, player1, player2)
        else:
            Text1.setText("Okay a Tie " + player1 + ",please roll again")
            continue


def play_game(window):
    message = Text(Point(400, 400), "How many players?")
    message.setTextColor("purple")
    message.setSize(20)
    message.draw(window)
    oneSquare = Rectangle(Point(280, 420), Point(320, 450))
    twoSquare = Rectangle(Point(480, 420), Point(520, 450))
    oneSquare.draw(window)
    twoSquare.draw(window)
    oneSquare.setFill("yellow")
    twoSquare.setFill("yellow")
    onePlayer = Text(Point(300, 430), "ONE")
    twoPlayer = Text(Point(500, 430), "TWO")
    onePlayer.draw(window)
    twoPlayer.draw(window)
    while True:
        click = window.getMouse()
        xValue = click.getX()
        yValue = click.getY()
        players = str("")
        if (xValue) > 280 and (xValue) < 320 and (yValue) > 420 and (yValue) < 450:
            players = "1"
            break
        elif (xValue) > 480 and (xValue) < 520 and (yValue) > 420 and (yValue) < 450:
            players = "2"
            for limb in limbs2:
                limb.draw(window)
            break
        else:
            continue
    message.undraw()
    oneSquare.undraw()
    twoSquare.undraw()
    onePlayer.undraw()
    twoPlayer.undraw()
    if players == "1":
        first_time = True
        while True:
            if first_time == True:
                name1 = GraphWin("SQUATTER", 250, 250)
                name1.setBackground(color_rgb(0, 0, 250))
                message = Text(Point(125, 75), "What is your name?")
                Text(Point(125, 180), "Click to close").draw(name1)
                message.setStyle("bold")
                message.draw(name1)
                inputBox = Entry(Point(125, 125), 15)
                inputBox.setTextColor("yellow")
                inputBox.draw(name1)
                while True:
                    name1.getMouse()
                    player1 = inputBox.getText()
                    name1.close()
                    break
                dice(window)
                (window, miss, player1, position1, money1, sheep1, drought1, drought_position1, player, end) = play(
                    window, False, player1, 0, 100, 5, False, 0, 3, False)
                first_time = False
            else:
                (window, miss, player1, position1, money1, sheep1, drought1, drought_position1, player, end) = play(
                    window, miss, player1, position1, money1, sheep1, drought1, drought_position1, player, end)
                if end == True:
                    main()
    elif players == "2":
        play_2(window)
    else:
        return


def winGame(window, player):
    info = Text(Point(400, 300), "" + player + "\nis the \nW I N N E R ! ! !")
    colours = ("pink", "brown", "yellow", "green", "blue", "red", "white", "orange", "black")
    info.setTextColor("pink")
    info.setSize(34)
    info.setStyle("bold")
    while True:
        click = window.checkMouse()
        for colour in colours:
            info.setTextColor(colour)
            info.draw(window)
            for x in range(1000000):
                x = x + 1
            info.undraw()
        if click != None:
            break
        continue
    return


def quit_game(player_position, player):
    if player == 1 or player == 3:
        for limb in limbs:
            limb.move(-(movement[player_position][0]), -(movement[player_position][1]))
        for object in limbs:
            object.undraw()
        return ()
    else:
        for limb in limbs2:
            limb.move(-(movement[player_position][0]), -(movement[player_position][1]))
        for object in limbs2:
            object.undraw()
        return ()


def main():
    (option, window) = home_screen()

    for object in limbs:
        object.draw(window)
    while True:
        if option.lower() == "play":
            play_game(window)
        elif option.lower() == "help":
            help()
            option = mouseClick(window)
        elif option == "quit":
            window.close()
            quit()
        else:
            continue


main()
