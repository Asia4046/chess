import position as p

# rook logic
def move_rook(board, pos, move_pos):
    init_piece_color = get_color(board, pos)
    final_color = get_color(board, move_pos)

    if p.get_piece(board, pos) == "BR" or p.get_piece(board, pos) == "WR":
        initial_rook_row, initial_rook_column = p.get_pos(pos)
        rook_move_row, rook_move_column = p.get_pos(move_pos)

        move_up, move_down, move_left, move_right = False

        if initial_rook_row - rook_move_row == 0 and  rook_move_column - initial_rook_column < 0:
            move_left = True
        elif initial_rook_row - rook_move_row == 0 and  rook_move_column - initial_rook_column > 0:
            move_right = True
        elif initial_rook_column - rook_move_column == 0 and  rook_move_row - initial_rook_row < 0:
            move_up = True
        elif initial_rook_column - rook_move_column == 0 and  rook_move_row - initial_rook_row > 0:
            move_down = True

        if move_right:
            for i in range(initial_rook_column + 1, rook_move_column):
               if board[initial_rook_row][i] != "__" :
                    print("illegal move")                
                    break
            else:
                if init_piece_color == final_color:
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)        
        elif move_left:
            for i in range(rook_move_column + 1, initial_rook_column):
               if board[initial_rook_row][i] != "__" :
                    print("illegal move")
                    break
            else:
                if init_piece_color == final_color:
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)
        elif move_down:
            for i in range(initial_rook_row + 1, rook_move_row):
               if board[i][initial_rook_column] != "__" :
                    print("illegal move")
                    break
            else:
                if init_piece_color == final_color:
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)
        elif move_up:
            for i in range(rook_move_row + 1, initial_rook_row):
               if board[i][initial_rook_column] != "__" :
                    print("illegal move")
                    break
            else:
                if init_piece_color == final_color:
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)
        else:
            print("Cannot move diagonally")
    else:
        print(p.get_piece(board, pos))
        print("Error: Selected position does not  contain a rook!!")

def get_color(board, pos):
    piece  = p.get_piece(board, pos)
    if "W" in piece:
        color = "White"
    else:
        color = "Black"

    return  color

def cut_piece(board, pos, mov_pos):
    ri, ci = p.get_pos(pos)
    rf, cf  = p.get_pos(mov_pos)

    if board[rf][cf] !=  "__":
        board[rf][cf] = board[ri][ci]
        board[ri][ci] = "__"
    else:
        p.change_position(board, pos, mov_pos)
