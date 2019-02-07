import turtle as t
import random
def create_table():

    t.Pen()

    t.pd()

    t.bgcolor('blue')

    t.pencolor('red')

    t.pensize(10)

    t.speed('normal')

    t.fd(120)

    t.bk(240)

    t.fd(80)

    t.rt(90)

    t.fd(160)

    t.bk(240)

    t.fd(160)

    t.rt(90)

    t.fd(80)

    t.bk(240)

    t.fd(80)

    t.rt(90)

    t.fd(160)

    t.bk(240)

    t.up()

    t.home()

    t.goto(-160, 160)

    t.pencolor('red')

    t.pd()

    t.write(' TIC TAC TOE DELUX', font=('Segoe Print', 22, 'normal'))

    t.up()

    t.home()





# Game



def position(x):

    if x == 1:

        t.setx(-80)

        t.sety(10)

    elif x == 2:

        t.sety(10)

    elif x == 3:

        t.setx(80)

        t.sety(10)

    elif x == 4:

        t.setx(-80)

        t.sety(-70)

    elif x == 5:

        t.sety(-70)

    elif x == 6:

        t.setx(80)

        t.sety(-70)

    elif x == 7:

        t.setx(-80)

        t.sety(-150)

    elif x == 8:

        t.sety(-150)

    elif x == 9:

        t.setx(80)

        t.sety(-150)

    else:

        print 'wrong input'

    t.pd()

    t.color('black', 'green')

    t.begin_fill()

    t.circle(25)

    t.end_fill()

    t.up()

    t.home()

    t.ht





def cross(x):

    if x == 1:

        t.setx(-120)

        t.sety(10)

    elif x == 2:

        t.setx(-20)

        t.sety(10)

    elif x == 3:

        t.setx(60)

        t.sety(10)

    elif x == 4:

        t.setx(-120)

        t.sety(-70)

    elif x == 5:

        t.setx(-20)

        t.sety(-70)

    elif x == 6:

        t.setx(60)

        t.sety(-70)

    elif x == 7:

        t.setx(-120)

        t.sety(-150)

    elif x == 8:

        t.setx(-20)

        t.sety(-150)

    elif x == 9:

        t.setx(60)

        t.sety(-150)

    t.pd()

    t.pencolor('white')

    t.left(45)

    t.fd(70.71)

    t.right(135)

    t.color('white')

    t.up()

    t.fd(50)

    t.pd()

    t.color('white')

    t.left(225)

    t.fd(70.71)

    t.right(135)

    t.up()

    t.home()





def feed(x, col):

    if col == 'cross':

        cross(x)

    elif col == 'circle':

        position(x)





def display():

    create_table()

    grid = [1,2,3,4,5,6,7,8,9]

    winl = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7],]

    l1 = []

    l2 = []

    print ' TIC TAC TOE DELUX'

    print 'the board looks like this'

    print_board()

    x = input(' Game b/w 2 players=1 Game b/w computer &player=2:')

    if x == 1:

        y = input('''enter the shape for player 1\ncross=1\ncircle=2 :''')

        if y == 1:

            col1 = 'cross'

        else:

            col1 = 'circle'

        print 'For Player 1 shape is', col1

        if col1 == 'cross':

            col2 = 'circle'

        else:

            col2 = 'cross'

        print 'For Player 2 shape is', col2



            # start game



        i = 0

        while i < 10:

            if i == 9:

                print 'TIE'
                win('It is a  TIE....')

            elif i % 2 == 0:

                while 1:

                    p1 = input('enter position player 1:')

                    if p1 in grid:

                        l1.append(p1)

                        grid.remove(p1)

                        x = p1

                        col = col1

                        feed(x, col)

                        m = 'The winner is:PLAYER 1'

                        check8(l1, m)

                        break

                    else:

                        print 'Invalid input'

            else:

                while 1:

                    p2 = input('enter position player 2:')

                    if p2 in grid:

                        l2.append(p2)

                        grid.remove(p2)

                        x = p2

                        col = col2

                        feed(x, col)

                        m = 'The winner is: PLAYER 2'

                        check8(l2, m)

                        break

                    else:

                        print 'Invalid input'

            i += 1

    elif x == 2:

        y = input('enter the shape for player\ncross=1\ncircle=2:')

        if y == 1:

            col1 = 'cross'

        else:

            col1 = 'circle'

        print 'For Player  shape is', col1

        if col1 == 'cross':

            col2 = 'circle'

        else:

            col2 = 'cross'

        print 'For computer shape is', col2



            # start game



        i = 0

        while i < 10:

            if i == 9:

                print 'TIE'
                win('It is a  TIE.....')

            elif i % 2 == 0:

                while 1:

                    p1 = input('enter position player :')

                    if p1 in grid:

                        l1.append(p1)

                        grid.remove(p1)

                        x = p1

                        col = col1

                        feed(x, col)

                        m = 'The winner is:PLAYER'

                        check8(l1, m)

                        break

                    else:

                        print 'Invalid input'

            else:



                while 1:

                    m = AImove(winl, l1, l2, grid)

                    grid = m[1]

                    l2 = m[2]

                    x = m[0]

                    col = col2

                    feed(x, col)

                    m = 'The winner is:COMPUTER'

                    check8(l2, m)

                    break

            i += 1

    else:

        print 'Invalid choice'





def AImove(winl,l1,l2,grid,):

    '''function to choose an ideal move for the computer

    :param1: win list of winning moves

    :param2: l1 list of moves by player 1

    :param3: l2 list of moves by computer

    :param4: grid list containing available spots on the grid

    :returns: tuple : (winning move index, final grid, list of moves by computer)

    '''



    #checks if a winning move is available

    for i in grid:

        gridcpy = list(grid)

        l1_cpy = list(l1)

        l2_cpy = list(l2)

        l2_cpy.append(i)

        gridcpy.remove(i)

        for move in winl:

            if set(move).issubset(set(l2_cpy)):

                return (i, gridcpy, l2_cpy)

    #checks if the player can win in the next move and blocks

    for i in grid:

        gridcpy = list(grid)

        l1_cpy = list(l1)

        l2_cpy = list(l2)

        l1_cpy.append(i)

        gridcpy.remove(i)

        for move in winl:

            if set(move).issubset(set(l1_cpy)):

                l2_cpy.append(i)

                return (i, gridcpy, l2_cpy)

    corners = [1,3,7,9]

    #makes a move in the corners

    for i in grid:

        gridcpy = list(grid)

        l1_cpy = list(l1)

        l2_cpy = list(l2)

        if i in corners:

            l2_cpy.append(i)

            gridcpy.remove(i)

            return i,gridcpy,l2_cpy

    #makes a move in the center if corners are unavailable

    if 5 in grid:

        gridcpy = list(grid)

        l1_cpy = list(l1)

        l2_cpy = list(l2)

        l2_cpy.append(5)

        gridcpy.remove(5)

        return 5,gridcpy,l2_cpy

    #chooses a random side move

    mv = random.choice(grid)

    gridcpy = list(grid)

    l2_cpy = list(l2)

    l2_cpy.append(mv)

    gridcpy.remove(mv)

    return mv,gridcpy,l2_cpy


def end(k, f):

    t.goto(k)

    t.pensize(5)

    t.color('black')

    t.pd()

    t.goto(f)

    t.ht()

def check8(t, m):

    if check(t, [1, 2, 3]):

        end((-120, 40), (120, 40))

        win(m)

    elif check(t, [4, 5, 6]):

        end((-120, -40), (120, -40))

        win(m)

    elif check(t, [7, 8, 9]):

        end((-120, -120), (120, -120))

        win(m)

    elif check(t, [1, 4, 7]):

        end((-80, 80), (-80, -160))

        win(m)

    elif check(t, [2, 5, 8]):

        end((0, 80), (0, -160))

        win(m)

    elif check(t, [3, 6, 9]):

        end((80, 80), (80, -160))

        win(m)

    elif check(t, [1, 5, 9]):

        end((-120, 80), (120, -160))

        win(m)

    elif check(t, [3, 5, 7]):

        end((120, 80), (-120, -160))

        win(m)





def win(m):

    print '****************************** \n ', m

    print '*' * 30

    t.up()

    t.goto(-160, -240)

    t.pencolor('red')

    t.pd()

    t.write(m, font=('Segoe Print', 22, 'normal'))

    playagain()





def check(t, q):

    j = 0

    for p in q:

        if p in t:

            j += 1

            if p not in t:

                return False



    if j != 3:

        return False

    if j == 3:

        return True





def playagain():

    print 'Press 1 to play again\nPress any number for EXIT'

    while True:

        x = input('enter:')

        if x == 1:

            t.home()

            t.clear()

            display()

        else:

            print 'EXIT'

            exit()





def print_board():

    print '   |      |'

    print 1, ' | ', 2, '  | ', 3

    print '   |      |'

    print '---------------'

    print '   |      |'

    print 4, ' | ', 5, '  | ', 6

    print '   |      |'

    print '---------------'

    print '   |      |'

    print 7, ' | ', 8, '  | ', 9

    print '   |      |'





def main():

    display()

    playagain()





main()



            

            

