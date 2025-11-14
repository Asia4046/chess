import position as p

def move_rook(board, pos, move_pos):
    if p.get_piece(board, pos) == "BR" or p.get_piece(board, pos) == "WR":
        r_rk, c_rk = p.get_pos(pos)
        m_r, m_c = p.get_pos(move_pos)

        move_up = False
        move_down = False
        move_left  = False
        move_right = False

        if r_rk - m_r == 0 and  m_c - c_rk < 0:
            move_left = True
        elif r_rk - m_r == 0 and  m_c - c_rk > 0:
            move_right = True
        elif c_rk - m_c == 0 and  m_r - r_rk < 0:
            move_up = True
        elif c_rk - m_c == 0 and  m_r - r_rk > 0:
            move_down = True

        if m_r == r_rk or m_c == c_rk:
            if board[m_r][m_c] != "__":
                print("Error:  No place to move  rook")
            else:
                p.change_position(board, pos, move_pos)
        elif m_r == r_rk and m_c == c_rk:
            print("Cannot move to the same place")
        else:
            print("Cannot move diagonally!!")
    else:
        print(p.get_piece(board, pos))
        print("Error: Selected postion does not  contain a rook!!")

def get_color(board, pos):
    color = ""
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
