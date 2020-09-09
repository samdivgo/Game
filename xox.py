X="X"
O="O"
EMPTY=" "
TIE="Ничья"
NUM_SQUERS=9

def ask_yes_no(question):
    """Задаёт вопрос да или нет"""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

def ask_number(question,low,high):
    """Просит ввести число из диапозона"""
    respones=None
    while respones not in range(low,high):
        respones=int(input(question))
    return respones

def pieces():
    """Решает кто ходит 1"""
    go_first=ask_yes_no("Хочешь ходить первым?(y/n) ")
    if go_first=='y':
        human=X
        computer=O
    else:
        computer=X
        human=O
    return computer,human

def new_board():
    """создаёт игровую доску"""
    board=[]
    for square in range(NUM_SQUERS):
        board.append(EMPTY)
    return board

def display_board(board):
    """Выводит игровую доску"""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t","---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Определяем доступные ходы"""
    moves=[]
    for square in range(NUM_SQUERS):
        if board[square]==EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяем победителя"""
    WAYS_TO_WIN=((0,1,2),(3,4,5),(6,7,8)
                 ,(0,3,6)
                 ,(1,4,7)
                 ,(2,5,8)
                 ,(0,4,8)
                 ,(2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board,human):
    """Ход человека"""
    legal=legal_moves(board)
    move=None

    while move not in legal:
        move=ask_number("Твой ход. Выбери одно из полей(0-8):",0,NUM_SQUERS)
        if move not in legal:
            print("Ты ошибся.")
    return move

def computer_move(board,computer,human):
    """Делает ход компьютера"""
    board=board[:]

    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("Я выберу поле",end=" ")

    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move]=EMPTY

    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
        board[move]=EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Переход хода"""
    if turn==X:
        return O
    else:
        return X

def congrat_winner(the_winner,computer,human):
    if the_winner!=TIE:
        print("Три ",the_winner," в ряд\n")
    else:
        print("Ничья")

    if the_winner==computer:
        print("Компьютер выйграл\n")
    elif the_winner==human:
        print("Вы выйграли\n")

def game():
    computer,human=pieces()
    turn=X
    board=new_board()
    display_board(board)
    while not winner(board):
        if turn==human:
            move = human_move(board,human)
            board[move]=human
        else:
            move=computer_move(board, computer,human)
            board[move]=computer
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner,computer,human)

game()
input("\n\nНажмите enter")
