#!/usr/bin/env python

import locale
import resource
import reversi.Reversi as Reversi

print "REVERSI AI ENGINE - 1 PLAYER MODE"
print "By Alex Berriman 2012\n"

locale.setlocale(locale.LC_ALL, 'en_US')
reversi = Reversi.Reversi()

# Starting player is black
player = Reversi.Gameboard.BLACK
ai_player = reversi.gameboard.opponent(player)
reversi.ai.setActivePlayer(player)

# Let's play the 1 player game
move_count = 1
while True:
    print "Memory usage: " + str(locale.format("%d", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, grouping=True)) + "\n"
    print reversi.gameboard
     
    # If we're the human player
    if move_count % 2 == 1:
        # Keep requesting a move until a valid one is entered
        while True:
            print "Valid moves: " + str(reversi.rules.validMoves(player)) + "\n"            
            move = raw_input("Please make your move: (" + reversi.gameboard.players[player][1] + "): ")
            if not reversi.rules.isValid(move, player):
                print "\tThat is an invalid move!\n"
            else:
                break
                
        # Make the move
        reversi.makeMove(move, player)
        opponent = Reversi.Gameboard.BLACK if player == Reversi.Gameboard.WHITE else Reversi.Gameboard.WHITE
        
    # If we're the AI player
    else:
        print "Your opponent is determining their move..."
        move = reversi.ai.run(reversi.gameboard, ai_player)
        reversi.flushAi()
        reversi.makeMove(move, ai_player)
        opponent = Reversi.Gameboard.BLACK if ai_player == Reversi.Gameboard.WHITE else Reversi.Gameboard.WHITE
        
    # Increment the move count
    move_count += 1
        
    # Is it game over?
    if reversi.gameover() == True:
        print str(reversi.gameboard) + "\n"
        print "Gameover! Winner: " + reversi.whoWon()
        break
        
    # Should we swap? Only if the opponent has valid moves
    if reversi.canMove(opponent) == False:
        print "\t" + reversi.gameboard.players[opponent][0] + " can not make any moves! Skipping turn...\n"
        move_count += 1
        
    print ""
    