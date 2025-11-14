import position as p
import pieces as pie


current_piece = ""

board = [['  ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ' ],
         ['1 ', 'WR', 'WH', 'WB', 'WQ', 'WK', 'WB', 'WH', 'WR' ],
         ['2 ', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP' ],
         ['3 ', '__', '__', '__', '__', '__', '__', '__', '__' ],
         ['4 ', '__', '__', '__', '__', '__', '__', '__', '__' ],
         ['5 ', '__', '__', '__', '__', '__', '__', '__', '__' ], 
         ['6 ', '__', '__', '__', '__', '__', '__', '__', '__' ], 
         ['7 ', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP' ],
         ['8 ', 'BR', 'BH', 'BB', 'BQ', 'BK', 'BB', 'BH', 'BR' ]]

def print_board(board):
    for i in board:
        for j in i:
            print(j, end = "   ")
        print("\n")
    print("\n")

def  user_change_pos(board, pi, pf):   
    
    r, c = p.get_pos(pf)
    if board[r][c] != '__':
        print("Position not empty!!")
    else:
      p.change_position(board, pi, pf)      
      print_board(board)

'''
# Main cmd-line
print("\n"*100)
print("-"*50)
print("WELCOME TO CMD-LINE CHESS")
print("-"*50)
print("\n")
print("1. PLAYER VS PLAYER  ")
print("2. PLAYER VS COMPUTER")
print("\n")

choice = input("Enter your choice: ")

while True:
   exit()
'''

print_board(board)