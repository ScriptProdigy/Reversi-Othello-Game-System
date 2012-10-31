#!/usr/bin/env python

import reversi.Reversi as Reversi

print "REVERSI AI ENGINE - 2 PLAYER MODE"
print "By Alex Berriman 2012\n"

reversi = Reversi.Reversi()

# Starting player is black
player = Reversi.Gameboard.BLACK

# Iterate forever (until we manually break out on game over)
while True:
    opponent = Reversi.Gameboard.BLACK if player == Reversi.Gameboard.WHITE else Reversi.Gameboard.WHITE
    print reversi.gameboard
    
    # Keep requesting a move until a valid one is entered
    while True:
        print "Valid moves: " + str(reversi.rules.validMoves(player)) + "\n" # This is only really hear to debug, so I can quickly see valid moves to play
        
        move = raw_input("Please make your move: (" + reversi.gameboard.players[player][1] + "): ")
        if not reversi.rules.isValid(move, player):
            print "\tThat is an invalid move!\n"
        else:
            break
    
    # Make the move
    reversi.makeMove(move, player)
    
    # Is it game over?
    if reversi.gameover() == True:
        print str(reversi.gameboard) + "\n"
        print "Gameover! Winner: " + reversi.whoWon()
        break
        
    # Should we swap? Only if the opponent has valid moves
    if reversi.canMove(opponent) == False:
        print "\t" + reversi.gameboard.players[opponent][0] + " can not make any moves! Skipping turn...\n"
    else:
        player = opponent
        
    print ""