#Thai Q Pham
#Tic Tac Toe project
#Draft version
from graphics import *
from random import *
def drawBoard():
    win = GraphWin("Tic-Tac-Toe", 300,300)
    button1 = Text(Point(100,100),"Single Player")
    button2 = Text(Point(200,100),"Two Players")
    button1.draw(win)
    button2.draw(win)

    R1= Rectangle(Point(50,50),Point(150,150))
    R1.draw(win)
    R2= Rectangle(Point(150,50),Point(250,150))
    R2.draw(win)
    

    choice = win.getMouse()
    Xc = choice.getX()
    Yc = choice.getY()
    result = ''
    while(result == ''):
        if( Xc >= 50 and Xc <= 150 and Yc >=50 and Yc <= 150):
            result = 'single'
            undrawChoice(button1,button2,R1,R2)
        elif (Xc >= 150 and Xc <= 250 and Yc >=50 and Yc <= 150):
            result = 'two'
            undrawChoice(button1,button2,R1,R2)
        else:
            choice = win.getMouse()
            Xc = choice.getX()
            Yc = choice.getY()
    button1 = Text(Point(100,100),"X")
    button2 = Text(Point(200,100),"O")
    button1.draw(win)
    button2.draw(win)

    R1= Rectangle(Point(50,50),Point(150,150))
    R1.draw(win)
    R2= Rectangle(Point(150,50),Point(250,150))
    R2.draw(win)
    
    choice = win.getMouse()
    Xc = choice.getX()
    Yc = choice.getY()
    letter =''
    while(letter == ''):
        if( Xc >= 50 and Xc <= 150 and Yc >=50 and Yc <= 150):
            letter = 'X'
            undrawChoice(button1,button2,R1,R2)
        elif (Xc >= 150 and Xc <= 250 and Yc >=50 and Yc <= 150):
            letter = 'O'
            undrawChoice(button1,button2,R1,R2)
        else:
            choice = win.getMouse()
            Xc = choice.getX()
            Yc = choice.getY()
    
    pt1 = Point(100,0)
    pt2 = Point(100,300)

    line1 = Line(pt1,pt2)
    line1.draw(win)

    pt3 = Point(200,0)
    pt4 = Point(200,300)

    line2 = Line(pt3,pt4)
    line2.draw(win)

    pt5 = Point(0,200)
    pt6 = Point(300,200)

    line3 = Line(pt5,pt6)
    line3.draw(win)

    pt7 = Point(0,100)
    pt8 = Point(300,100)

    line4 = Line(pt7,pt8)
    line4.draw(win)

    numClicks = 9
    #mouseClick = win.getMouse()
    return win,result,letter

def showMsg(win,msg):
    rec1=Rectangle(Point(0,1),Point(3,2))
    rec1.setFill('lightskyblue')
    rec1.draw(win)
    message1=Text(Point(150,150),msg)
    message1.setFill('blue')
    message1.setSize(20)
    message1.draw(win)
    time.sleep(1)

    message1.undraw()
    rec1.undraw()
def undrawChoice(B1,B2,r1,r2):
    B1.undraw()
    B2.undraw()
    r1.undraw()
    r2.undraw()
def drawX(win,centerX, centerY):
    centerPoint = Point(centerX, centerY)

    lineA = Line(centerPoint, Point(centerX+40, centerY+40))
    lineA.draw(win)

    lineB = Line(centerPoint, Point(centerX+40, centerY-40))
    lineB.draw(win)

    lineC = Line(centerPoint, Point(centerX-40, centerY+40))
    lineC.draw(win)

    lineD = Line(centerPoint, Point(centerX-40, centerY-40))
    lineD.draw(win)

def findCenter(point):
    x=point.getX()
    y=point.getY()
    newx=x//100*100+50
    newy=y//100*100+50
    #print(newx,newy)
    return Point(newx,newy)

def drawCross(win,xPoint):
#    xPoint = findCenter(xClick)
    drawX(win,xPoint.getX(),xPoint.getY())
    return convertPointToTheMove(xPoint.getX(),xPoint.getY())
def drawCircle(win,cPoint):
#    cPoint = findCenter(oClick)
    circle = Circle(cPoint,40)
    circle.draw(win)
    return convertPointToTheMove(cPoint.getX(),cPoint.getY())
def twoPlayers(win,playerLetter):
    board =[0,0,0,0,0,0,0,0,0]
    isGamePlaying = True
    turn = 'player1'
    if playerLetter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'
    while(isGamePlaying):
        if(turn == 'player1'):
            xClick = win.getMouse()
            xPoint = findCenter(xClick)
            if playerLetter == 'X':
                X = drawCross(win,xPoint)
            else:
                X = drawCircle(win,xPoint)
            board[X] = playerLetter
            print(board)
            if(isWinner(board,playerLetter)):
               showMsg(win,'player1 is a winner')
               print('player1 is a winner')
               break
            else:
               if(isBoardFull(board)):
                   isGamePlaying = False
                   showMsg(win,'Tie!!!')
                   print("tie Zzz..")
                   break
               else:               
                   turn = 'player2'
        else:
            oClick = win.getMouse()
            cPoint = findCenter(oClick)
            if computerLetter == 'X':
                X = drawCross(win,cPoint)
            else:
                X = drawCircle(win,cPoint)
  
            
            board[X] = computerLetter
            if(isWinner(board,computerLetter)):
               showMsg(win,'player2 is a winner')
               print('player2 is a winner')
               break
            else:
               if(isBoardFull(board)):
                   isGamePlaying = False
                   print("tie Zzz..")
                   showMsg(win,'Tie!!!')
                   break
               else:               
                   turn = 'player1'
        
def singlePlayer(win,playerLetter):
    
#User clicks, get mouse click point
#Find center of the click
#Alternate between drawing O and X
    if playerLetter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'
    board =[0,0,0,0,0,0,0,0,0]
    playerMoves = [0,0,0,0,0,0,0,0,0]
    comMoves = [0,0,0,0,0,0,0,0,0]
    isGamePlaying = True
    turn = 'player'
    while(isGamePlaying):
        if turn == 'player':
            xClick = win.getMouse()
            xPoint = findCenter(xClick)
            if playerLetter == 'X':
                X = drawCross(win,xPoint)
            else:
                X = drawCircle(win,xPoint)
            print("check",X,xPoint.getX(),xPoint.getY())
            board[X] = playerLetter
            playerMoves[X] = playerLetter
            print(board)
            if(isWinner(board,playerLetter)):
               print('you are a winner')
               showMsg(win,'You Win!!!')
               break
            else:
               if(isBoardFull(board)):
                   isGamePlaying = False
                   showMsg(win,'Tie!!!')
                   print("tie Zzz..")
                   break
               else:               
                   turn = 'com'
        else:
            move = getComputerMove(board,computerLetter,playerLetter)
            print("check the move",move)
            x,y = convertTheMoveToPoint(move)
            print("check the move",x,y)
            cPoint = findCenter(Point(x,y))
            if computerLetter == 'X':
                X = drawCross(win,cPoint)
            else:
                X = drawCircle(win,cPoint)
  
            
            board[move] = computerLetter
            comMoves[move] = computerLetter
            print(board)
            if(isWinner(board,computerLetter)):
               print('com is a winner')
               showMsg(win,'You Lost!!!')
               break
            else:
                if(isBoardFull(board)):
                   isGamePlaying = False
                   showMsg(win,'Tie!!!')
                   print("tie Zzz..")
                   break
                else:               
                   turn='player'

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
       dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
# Return true if the passed move is free on the passed board.
    return board[move] == 0
def isBoardFull(board):
# Return True if every space on the board has been taken. Otherwise return False.
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True
def getComputerMove(board, computerLetter,playerLetter):
    # First, check if we can win in the next move
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
        if isWinner(copy, computerLetter):
            return i
    # Check if the player could win on their next move, and block them.
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
        if isWinner(copy, playerLetter):
            return i
    move = chooseRandomMoveFromList(board,[0,2,4,8])
    if(move != None):
        return move
    if isSpaceFree(board,4):
        return 4
    return chooseRandomMoveFromList(board, [1, 3, 5, 7])
def makeMove(board, letter, move):
    board[move] = letter
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return choice(possibleMoves)
    return None
def convertPointToTheMove(X,Y):
    if X == 50 and Y == 50:
        return 0
    elif X == 150 and Y == 50:
        return 1
    elif X == 250 and Y == 50:
        return 2
    elif X == 50 and Y == 150:
        return 3
    elif X == 150 and Y == 150:
        return 4
    elif X == 250 and Y == 150:
        return 5
    elif X == 50 and Y == 250:
        return 6
    elif X==150 and Y == 250:
        return 7
    else:
        return 8

def convertTheMoveToPoint(position):
    if position == 0:
        return 50,50
    elif position == 1:
        return 150,50
    elif position == 2:
        return 250,50
    elif position == 3:
        return 50,150
    elif position == 4:
        return 150,150
    elif position == 5:
        return 250,150
    elif position == 6:
        return 50,250
    elif position == 7:
        return 150,250
    else:
        return 250,250
    

def isWinner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
    (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
    (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
    (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

def main():
    win,result,letter = drawBoard()
    if(result == 'single'):
        singlePlayer(win,letter)
    else:
        twoPlayers(win,letter)

main()          
