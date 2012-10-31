import Gameboard

"""

"""

class AI:
    def __init__(self, nodes=3):
        self.nodes = nodes
        
    def run(self, gameboard, player):
        tree = {
            "gameboard" : gameboard,
            "moves" : {},
        }
        self.minmax(gameboard, player, tree)
        
    def minmax(self, gameboard, player, tree, node=1):
        """ 
        The minimax algorithm creates a tree of gameboards which we can use to find
        the optimal move to take.
        """
        # If we've reached a leaf node, it's time to exit out
        if self.reachedLeafNode(node):
            print "reached leaf node"
            sys.exit(0)
            
        # Let's iterate through all possible moves and add to our tree
        for move in self.rules.validMoves(player):
            gb = Gameboard.Gameboard(gameboard)
            gb.setPiece(move, player)

            tree["moves"][move] = {
                "gameboard" : gb, 
                "moves" : {}
            }
        
        print tree
        
    def reachedLeafNode(self, node):
        if node >= self.nodes:
            return True
            
        return False
        
    def score(self, gameboard, player):
        """ 
        Returns the score of a current gameboard (the evaluation function)
        
        This is perhaps the most important method of the entire AI class. The stronger the
        evaluation function, the more intelligently the agent will be able to play. It considers
        the following set of factors:
            
            - Score differential: 
                while not enough of an indicator by itself, the amount of pieces occupied on the
                board is important (particularly in an endgame scenario where the amount of
                available squares is less than or equal to our amount of tree nodes).
                
            - Mobility:
                The amount of moves a player can make. The more moves (greater mobility), the more
                options they'll have and better position they'll be in.
                
            - Edge/corner pieces:
                In optimal Reversi gameplayer (though I'm not expert in Reversi strategy) occupying
                corner positions is beneficial. 
        """
        
        print "test"
        score = gameboard.score(player) - gameboard.score(gameboard.opponent(player))
        
        return score
        
    def setActivePlayer(self, player):
        self.activePlayer = player
        
    def setRules(self, rules):
        self.rules = rules