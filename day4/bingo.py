
def to_int(board):
    for i, e in enumerate(board):
        board[i] = int(e)
    return board

def load_data():
    file1 = open('inp.txt', 'r')
    line_nr = 0
    numbers = []
    boards = []

    while True:
        line_nr += 1

        if line_nr == 1:
            line = file1.readline().strip().split(",")
            for i, e in enumerate(line):
                line[i] = int(e)
            numbers = line 
        

        else:
            # Get empty line
            line = file1.readline()
            # if line is empty
            # end of file is reached
            if not line:
                break

            row1 = to_int(file1.readline().strip().split())
            row2 = to_int(file1.readline().strip().split())
            row3 = to_int(file1.readline().strip().split())
            row4 = to_int(file1.readline().strip().split())
            row5 = to_int(file1.readline().strip().split())

            board = []
            board.extend(row1)
            board.extend(row2)
            board.extend(row3)
            board.extend(row4)
            board.extend(row5)

            boards.append(board)
    
            #print("Line{}: {}".format(count, line.strip()))
 
    file1.close()
    return numbers, boards


def check_winner(board, numbers):
    win_indexes = [ 
                    [0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],
                    [0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],
                  ]
    for indexes in win_indexes:
        winner = True
        for i in indexes:
            if board[i] not in numbers:
                winner = False
                break
            
        if winner:
            return True, indexes

    return False, []

def calculations(board, numbers):
    a_sum = 0

    for i in range(len(board)):
        if board[i] not in numbers:
            a_sum += board[i]
    
    return a_sum * numbers[-1]
    

def find_board(win_index, boards):
    for i, e in enumerate(boards):
        if i not in win_index:
            return e



# load data to numbers (list) and boards (list[list])
numbers, boards = load_data()
print(numbers)
print(boards)

# (part 1) for each number sequence(first 5 and larger) check if there is a winner board
# go = False
# for i in range(6, len(numbers)):
#     if go:
#         break

#     for board in boards:
        
#         winner, indexes = check_winner(board, numbers[:i])
#         # if there is a winner board, do calculations
#         if winner:
#             print(calculations(board, numbers[:i]))
#             go = True


# (part 2) check for winner if it is a winner, save its index
go = False
winner_index = set()
for i in range(6, len(numbers)):
    if go:
        break

    for j, board in enumerate(boards):
        
        if j not in winner_index:
            winner, indexes = check_winner(board, numbers[:i])
        else:
            winner = False

        if winner:
            winner_index.add(j)

            # when index list is equal to len(boards)- 1 there is only one board left
            if len(winner_index) == (len(boards) - 1):
                # save that board
                last_board = find_board(winner_index, boards)
            
            elif len(winner_index) == len(boards):
                # now the last board has won and we can use the called number
                print(calculations(last_board, numbers[:i]))
                go = True
                break