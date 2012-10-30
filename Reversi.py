#!/usr/bin/env python

import Gameboard
import Rules as ReversiRules

class Reversi:
	def __init__(self):
		self.gameboard = Gameboard.Gameboard()
		self.rules = ReversiRules.Rules()
		self.rules.setGameboard(self.gameboard)
		
	def makeMove(self, pos, player):
		for move in self.moveTiles(pos, player):
			self.gameboard.setPiece(move, player)
		
		self.gameboard.setPiece(pos, player)
		
	def moveTiles(self, pos, player):
		moves = []
		moves.extend(self.rules.getHoriSwap(pos, player))
		moves.extend(self.rules.getVertiSwap(pos, player))
		moves.extend(self.rules.getDiagSwap(pos, player))
		
		return moves
		
	# When is it gameover?
	def gameover(self):
		# If we've run out of empty squares it's obviously game over
		if len(self.rules.emptySquares()) == 0:
			return True
			
		# If neither player can move its also gameover
		return self.canMove(Gameboard.WHITE) == False and self.canMove(Gameboard.BLACK) == False
		
	# Can a player move?
	def canMove(self, player):
		return len(self.rules.validMoves(player)) > 0

	# Who is the winner?
	def winner(self):
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
		
	# Winner (string)
	def whoWon(self):
		winner = self.winner()
		
		# If the game is still being played, nobody has won
		if winner == -1:
			return "n/a"
			
		# If it was a tied game
		if winner == 0:
			return "Tied game"
		
		return self.gameboard.players[winner][0]