#!/usr/bin/env python

import Gameboard
import Rules as ReversiRules
import AI as ReversiAI

"""
The Reversi controls some basic mechanisms over the game as a whole.

For instance, it is charged with making the moves, determining who is
the winner, etc. Relies on the Rules class to determine the legality
of particular moves.
"""

class Reversi:

    def __init__(self):
        self.gameboard = Gameboard.Gameboard()
        self.rules = ReversiRules.Rules()
        self.rules.setGameboard(self.gameboard)
        self.ai = ReversiAI.AI()
        self.ai.setRules(self.rules)
        
    def makeMove(self, pos, player):
        """ Makes the move for a player to a given tile """
        for move in self.rules.moveTiles(pos, player):
            self.gameboard.setPiece(move, player)
        
        self.gameboard.setPiece(pos, player)

    def gameover(self):
        """ Returns true if the game is over (no more moves), false if not """
        # If we've run out of empty squares it's obviously game over
        if len(self.rules.emptySquares()) == 0:
            return True
            
        # If neither player can move its also gameover
        return self.canMove(Gameboard.WHITE) == False and self.canMove(Gameboard.BLACK) == False
        
    def canMove(self, player):
        """ Returns true if a player has any valid moves, false if not """
        return len(self.rules.validMoves(player)) > 0

    def winner(self):
        """ Returns a numeric representation of the winner of the current game """
        # If the game is still being played, there is no winner
        if self.gameover() == False:
            return -1
            
        # Retrieve the scores (retrieve once and store in local variable so we don't have to keep iterating)
        white = self.gameboard.score(Gameboard.WHITE)
        black = self.gameboard.score(Gameboard.BLACK)
        
        # If it's a tie
        if white == black:
            return 0
            
        # Game over, not a tie, who won?
        return Gameboard.WHITE if white > black else Gameboard.BLACK
        
    def whoWon(self):
        """ Returns the winner in a literal string format """
        winner = self.winner()
        
        # If the game is still being played, nobody has won
        if winner == -1:
            return "n/a"
            
        # If it was a tied game
        if winner == 0:
            return "Tied game"
        
        return self.gameboard.players[winner][0]