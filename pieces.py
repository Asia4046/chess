import position as p

# rook logic
def move_rook(board, pos, move_pos):
    init_piece_color = get_color(board, pos)
    final_color = get_color(board, move_pos)

    if p.get_piece(board, pos) == "BR" or p.get_piece(board, pos) == "WR":
        initial_rook_row, initial_rook_column = p.get_pos(pos)
        rook_move_row, rook_move_column = p.get_pos(move_pos)

        move_up, move_down, move_left, move_right = False, False, False, False

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

def move_pawn(board, pos, move_pos):
    init_piece_color = get_color(board, pos)
    final_color = get_color(board, move_pos)

    if p.get_piece(board, pos) == "WP" or p.get_piece(board, pos) == "BP":
        initial_pawn_row, initial_pawn_column = p.get_pos(pos)
        pawn_move_row, pawn_move_column = p.get_pos(move_pos)

        move_up_pw, move_down_pw = False, False

        if initial_pawn_column - pawn_move_column == 0 and  pawn_move_row - initial_pawn_row < 0:
            move_up_pw = True
        elif initial_pawn_column - pawn_move_column == 0 and  pawn_move_row - initial_pawn_row > 0:
            move_down_pw = True

        if init_piece_color == "White":
            move_count = 0
            if move_down_pw:
                for i in range(initial_pawn_row + 1, pawn_move_row):
                    move_count += 1

                    if move_count > 2:
                        print("Cannot move more than 2 places!! ")
                        break 
                        move_count = 0
                    
                    if board[i][initial_pawn_column] != "__" :
                        print("illegal move")
                        break
                else:
                    if pawn_move_row == initial_pawn_row + 1 and pawn_move_column == initial_pawn_column + 1:
                        if init_piece_color == final_color:
                            print("Cannot Vut own piece")
                        else:
                            cut_piece(board, pos, move_pos)
   
            else:
                print("Illegal move!!")
        if init_piece_color == "Black":
            if move_up_pw:
                if initial_pawn_row - pawn_move_row < 3:
                    for i in range(pawn_move_row, initial_pawn_row):
                        if board[i][initial_pawn_column] != "__" :
                            print("illegal move")
                            break
                        else:
                            p.change_position(board, pos, move_pos)
                    else:
                        if pawn_move_row == initial_pawn_row - 1 and pawn_move_column == initial_pawn_column - 1:
                            if init_piece_color == final_color:
                                print("Cannot Cut own piece")
                            else:
                                cut_piece(board, pos, move_pos)
                else:
                    print("Cannot move more than 2 places")

            else:
                print("Illegal move!!")


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
