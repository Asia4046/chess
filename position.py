row = 0 
col = 0

def get_pos(pos):

    if len(pos) > 2 and len(pos) < 2:
        print("Invalid")
        print("\n")
        row = None
        col = None

    if pos[0] == 'a':
        col = 1
    elif pos[0] == 'b':
        col = 2
    elif pos[0] == 'c':
        col = 3
    elif pos[0] == 'd':
        col = 4
    elif pos[0] == 'e':
        col = 5
    elif pos[0] == 'f':
        col = 6
    elif pos[0] == 'g':
        col = 7
    elif pos[0] == 'h':
        col = 8
    else:
        print ("Invalid")


    if pos[1] == '1':
        row = 1
    elif pos[1] == '2':
        row = 2
    elif pos[1] == '3':
        row = 3
    elif pos[1] == '4':
        row = 4
    elif pos[1] == '5':
        row = 5
    elif pos[1] == '6':
        row = 6
    elif pos[1] == '7':
        row = 7
    elif pos[1] == '8':
        row = 8
    else:
        print ("Invalid")

    return row, col

def change_position(board, initial_pos, final_pos):
    ri, ci = get_pos(initial_pos)
    rf, cf = get_pos(final_pos)

    board[rf][cf] = board[ri][ci]
    board[ri][ci] = '__'
 
def get_piece(board, pos):
    r,c = get_pos(pos)

    piece = board[r][c]
    return piece