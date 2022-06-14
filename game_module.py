
import random
global maze
global taken_pos
global player
global computer
player = [0]
compute = [0]

maze = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]
taken_pos=[]

#easy level
def play(row,col):
    maze[row][col] = 'X'
    taken_pos.append([row, col])
    if (win_check('X', maze)):
        player[0] = player[0]+1
        return 'player'
    while True and len(taken_pos)<9:
        row = random.choice([0, 1, 2])
        col = random.choice([0, 1, 2])
        if (([row,col] not in taken_pos)):
            maze[row][col] = 'O'
            taken_pos.append([row, col])
            break
    if (win_check('O', maze)):
        compute[0] = compute[0]+1
        return 'computer'
    if '_' not in maze[0] and '_' not in maze[1] and '_' not in maze[2]:
        return 'ties'
    return None

#hard_level_imlementation
def play_hard(row,col):
    maze[row][col] = 'X'
    taken_pos.append([row, col])
    if (win_check('X', maze)):
        player[0] = player[0] + 1
        return 'player'
    row, col = computer()
    maze[row][col] = 'O'
    if (win_check('O', maze)):
        compute[0] = compute[0] + 1
        return 'computer'
    if '_' not in maze[0] and '_' not in maze[1] and '_' not in maze[2]:
        return 'ties'
    return None


#medium_level_implementation
def play_medium(row,col):
    maze[row][col] = 'X'
    taken_pos.append([row, col])
    if (win_check('X', maze)):
        player[0] = player[0] + 1
        return 'player'
    #random logic

    choice = random.choice([0, 1])
    if choice == 0:
        while True and len(taken_pos)<9:
            row = random.choice([0, 1, 2])
            col = random.choice([0, 1, 2])
            if (([row,col] not in taken_pos)):
                maze[row][col] = 'O'
                taken_pos.append([row, col])
                break
    else:
        row,col = computer()
        taken_pos.append([row, col])
        maze[row][col] = 'O'
    if (win_check('O', maze)):
        compute[0] = compute[0] + 1
        return 'computer'
    if '_' not in maze[0] and '_' not in maze[1] and '_' not in maze[2]:
        return 'ties'
    return None


def reset():
    for i in range(3):
        for j in range(3):
            maze[i][j] = '_'
    taken_pos.clear()
    return

#map with 1d to 2d
def mapper(num):
    if num == 0:
        return 0,0
    elif num == 1:
        return 0,1
    elif num == 2:
        return 0,2
    elif num == 3:
        return 1,0
    elif num == 4:
        return 1,1
    elif num == 5:
        return 1,2
    elif num == 6:
        return 2,0
    elif num == 7:
        return 2,1
    else:
        return 2,2


#win check
def win_check(sym,maze):
    #vertical check
    for i in range(3):
        win = True
        for j in range(3):
            if (maze[j][i]!=sym):
                win = False
                continue
        if (win == True):
            return win

    #horizontal check
    for i in range(3):
        win = True
        for j in range(3):
            if (maze[i][j]!=sym):
                win = False
                continue
        if (win == True):
            return win

    #cross section check LEFT TO RIGHT
    win = True
    for i in range(3):
        if (maze[i][i]!=sym):
            win = False
            break
    if(win == True):
        return win

    #cross section check RIGHT TO LEFT
    win = True
    j=2
    for i in range(3):
        if (maze[i][j] != sym):
            win = False
            break
        j-=1
    if (win == True):
        return win
    return False


#computer ai play with min max algorithm
def computer():
    bestscore = -100
    best_row=best_col=0
    for i in range(3):
        for j in range(3):
            if (maze[i][j]=='_'):
                maze[i][j] = 'O'
                score = minimax(maze,False)
                maze[i][j] = '_'
                if(score>bestscore):
                    bestscore = score
                    best_row = i
                    best_col = j

    return best_row,best_col


def minimax (maze,ismax):
    if(win_check('O',maze)):
        return 1
    elif (win_check('X',maze)):
        return -1
    elif checkdraw():
        return 0
    if(ismax):
        bestscore = -100

        for i in range(3):
            for j in range(3):
                if (maze[i][j] == '_'):
                    maze[i][j] = 'O'

                    score = minimax(maze, False)
                    maze[i][j] = '_'
                    if (score > bestscore):
                        bestscore = score
                    if bestscore == 1: #purning code alpha beta
                        return bestscore
        return bestscore
    else:
        bestscore = 100
        for i in range(3):
            for j in range(3):
                if (maze[i][j] == '_'):
                    maze[i][j] = 'X'
                    score = minimax(maze, True)
                    maze[i][j] = '_'
                    if (score < bestscore):
                        bestscore = score
                    if bestscore == -1: #purning code alpha beta
                        return bestscore
        return bestscore

#draw check
def checkdraw():
    for i in range(3):
        for j in range(3):
            if(maze[i][j]=='_'):
                return False
    return True
