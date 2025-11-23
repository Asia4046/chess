import position as p

# rook logic
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

        if move_right == True:                                                                                                                                                                                                                                            
            for i in range(c_rk+1, m_c):
               if board[r_rk][i] != "__" : 
                    print("illegal move")                
                    break
            else:
                if p.get_piece(board, pos)[0] == "W" and p.get_piece(board, move_pos)[0] == "W":
                    print("cannot cut own  piece")
                elif p.get_piece(board, pos)[0] == "B" and p.get_piece(board, move_pos)[0] == "B":
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)        
        elif move_left == True:                                                                                                                                                                                                                                            
            for i in range(m_c+1, c_rk):                            
               if board[r_rk][i] != "__" : 
                    print("illegal move")
                    break
            else:
                if p.get_piece(board, pos)[0] == "W" and p.get_piece(board, move_pos)[0] == "W":
                    print("cannot cut own  piece")
                elif p.get_piece(board, pos)[0] == "B" and p.get_piece(board, move_pos)[0] == "B":
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)  
        elif move_down == True:                                                                                                                                                                                                                                            
            for i in range(r_rk+1, m_r):                            
               if board[i][c_rk] != "__" : 
                    print("illegal move")
                    break
            else:
                if p.get_piece(board, pos)[0] == "W" and p.get_piece(board, move_pos)[0] == "W":
                    print("cannot cut own  piece")
                elif p.get_piece(board, pos)[0] == "B" and p.get_piece(board, move_pos)[0] == "B":
                    print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos) 
        elif move_up == True:                                                                                                                                                                                                                                            
            for i in range(m_r+1, r_rk):                            
               if board[i][c_rk] != "__" : 
                    print("illegal move")
                    break
            else:
                if p.get_piece(board, pos)[0] == "W" and p.get_piece(board, move_pos)[0] == "W":
                    print("cannot cut own  piece")
                elif p.get_piece(board, pos)[0] == "B" and p.get_piece(board, move_pos)[0] == "B":
                      print("cannot cut own  piece")
                else:
                    cut_piece(board, pos, move_pos)
        else:
            print("Cannot move diagonally")
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
