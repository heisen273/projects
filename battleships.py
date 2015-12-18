import random
import sys
print(chr(27) + "[2J")
board = []
ships=[]

for x in range(0, 10):
    board.append((["O"]) * 10)
for x in range(0, 10):
    ships.append(([0]) * 10)

def print_board(board):
	for row in board:
		print " ".join(row)

def print_ships(board):
	for row in board:
		print ' '.join(str(e) for e in row)
print_board(board)

def random_dot():
	l=random.sample(range(0,99),8)
	for item in l:
		if item < 10:
			ship_row=0
			ship_col=item
		else:
			ship_row=item//10
			ship_col=item%10
	return [ship_row,ship_col]	
dot=[]
for i in range(0,10):
	dot=random_dot()
	ships[dot[0]][dot[1]]=1
for turn in range(10):
	print "GUESS MUST BE BETWEEN 0 AND 9"
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))
	print "GUESS MUST BE BETWEEN 0 AND 9"
	sys.stderr.write("\x1b[2J\x1b[H")

        if ships[guess_row][guess_col]==1:
                print "Congratulations! You sank my battleship!"
                board[guess_row][guess_col]="\033[1;31mX\033[1;m"
                print_board(board)
#                break
        elif (guess_row>10 or guess_row<0) or (guess_col>10 or guess_col<0):
                print "WRONG NUMBER, FELLA"
        elif board[guess_row][guess_col]=="X":
                print "You've guessed this one already!"
        else:
                print "You missed my battleship!"
                board[guess_row][guess_col]="X"
                print_board(board)
                if turn==9:
                        print "GAME OVER, no more turns"
        print "Turn",turn+1
                                     
