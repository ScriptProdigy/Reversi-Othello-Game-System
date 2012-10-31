import Gameboard

"""
The Rules class contains the rules that govern our game of Reversi.

In order for our AI engine to properly function, it has to observe 
a series of rules that are outlined within this class. It contains
methods that primarily govern what moves are legal.

TODO:
    The horizontal, vertical and diagonal ordinates methods should
    be re-written. They can be combined in to one method with a 
    more simplistic algorithm.
"""

class Rules:
    
    # Set the gameboard data value
    def setGameboard(self, gameboard):
        self.gameboard = gameboard
        
    # Returns a list of empty squares on the board
    def emptySquares(self):
        empty = []
        
        for letter_ascii in range(Gameboard.LETTER_A, Gameboard.LETTER_H + 1):
            letter = chr(letter_ascii)
            for i in range(1, self.gameboard.size() + 1):
                pos = letter + str(i)
                if self.gameboard.getPiece(pos) == Gameboard.EMPTY:
                    empty.append(pos)
                    
        return empty
        
    # Whether or not a move is valid for a player
    def isValid(self, pos, player):
        if pos not in self.emptySquares(): # Moving in to a square that isn't empty is illegal
            return False
            
        return self.validHorizontal(pos, player) == True or self.validVertical(pos, player) == True or self.validDiagonal(pos, player) == True
        
    # Returns vertical tiles that can be swapped
    def getVertiSwap(self, pos, player):
        if pos not in self.emptySquares():
            return []

        (squares, tiles, ord, letter) = ([], [], int(pos[1:]), pos[0:1])
        
        # Go up
        for i in range(ord - 1, 0, -1):
            squares.append(letter + str(i))
        tiles.extend(self.swappedTiles(squares, player))

        # Go down
        squares = []
        for i in range(ord + 1, 9):
            squares.append(letter + str(i))
        tiles.extend(self.swappedTiles(squares, player))
    
        return tiles
        
    # Whether any horizontal options would constitute a valid move
    def validHorizontal(self, pos, player):
        return len(self.getHoriSwap(pos, player)) > 0
        
    # Whether any vertical options would constitute a valid move
    def validVertical(self, pos, player):
        return len(self.getVertiSwap(pos, player)) > 0
        
    # Whether any diagonal options would constitute a valid move
    def validDiagonal(self, pos, player):
        return len(self.getDiagSwap(pos, player)) > 0
        
    # Let's calculate the diagonal oordinates
    def getDiagSwap(self, pos, player):
        # We've got to go in 2 directions
        if pos not in self.emptySquares():
            return []

        (squares, tiles, cord, letter) = ([], [], int(pos[1:]), pos[0:1])
        (top_left, bottom_left, top_right, bottom_right) = ([], [], [], [])
        
        # Let's calculate the squares for the four directions
        for i in range(cord - 1, -self.gameboard.size(), -1):
            iter = cord - i
            
            # Do we need to break out?
            if (iter > self.gameboard.size()):
                break
            
            let = ord(letter) - (cord - i)
            if let >= Gameboard.LETTER_A and i >= 1:
                top_left.append(str(chr(let)) + str(i))

            if cord + iter <= self.gameboard.size() and let >= Gameboard.LETTER_A:
                bottom_left.append(str(chr(let)) + str(cord + iter))
                
            if i > 0 and (ord(letter) + iter) <= Gameboard.LETTER_H :
                top_right.append(str(chr(ord(letter) + iter)) + str(i))
            
            if (cord + iter) <= self.gameboard.size() and (ord(letter) + iter) <= Gameboard.LETTER_H:
                bottom_right.append(str(chr(ord(letter) + iter)) + str(cord + iter))

        # And now we can calculate what tiles can be swapped
        tiles.extend(self.swappedTiles(top_left, player))
        tiles.extend(self.swappedTiles(bottom_left, player))
        tiles.extend(self.swappedTiles(top_right, player))
        tiles.extend(self.swappedTiles(bottom_right, player))
                                        
        return tiles
    
    def getHoriSwap(self, pos, player):
        if pos not in self.emptySquares():
            return []

        (squares, tiles, cord, letter) = ([], [], int(pos[1:]), pos[0:1])
        
        # Go left
        letter_ord = ord(letter)
        for i in range(letter_ord, Gameboard.LETTER_A, -1):
            letter = chr(i - 1)
            squares.append(letter + str(cord))
        tiles.extend(self.swappedTiles(squares, player))
        
        # Go right
        squares = []
        for i in range(letter_ord, Gameboard.LETTER_H):
            letter = chr(i + 1)
            squares.append(letter + str(cord))
        tiles.extend(self.swappedTiles(squares, player))
        
        return tiles

    # Takes a list of piece positions and determines what pieces can be swapped
    def swappedTiles(self, squares, player):
        moves = []
        for square in squares:
            if self.gameboard.getPiece(square) == player:
                break
            elif self.gameboard.getPiece(square) == Gameboard.EMPTY:
                moves = []
                break
            elif self.gameboard.getPiece(square) == self.gameboard.opponent(player):
                moves.append(square)
            
        # If we've got to a boundary, and the piece is either empty or the opponent, it's not valid (clear the moves)
        if len(moves) > 0 and self.gameboard.getPiece(square) == self.gameboard.opponent(player):
            moves = []
            
        return moves
        
    # Return a list of valid moves for a player
    def validMoves(self, player):
        moves = []
        for letter_ascii in range(Gameboard.LETTER_A, Gameboard.LETTER_H + 1):
            letter = chr(letter_ascii)
            for i in range(1, 9):
                pos = letter + str(i)
                if self.isValid(pos, player):
                    moves.append(pos)
                    
        return moves
