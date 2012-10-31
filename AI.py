import Gameboard

"""
The AI class is the brains of the entire operation. It's essentially the agent
(what this entire project is focused on).

It uses a minimax algorithm (http://en.wikipedia.org/wiki/Minimax) to pick the 
best suitable moves assuming optimal gameplay from both parties. Improvements
to the agent include:
    
    - Implementation of an alpha-beta pruning algorithm to refine the minimax.
    - Less reliance on OOP (degrades the performance). Creating so many parallel
      objects blows out the execution time.
    - Improve the evaluation function (I never really 'trained' it. Ideally I'd
      like to write something that evaluates the effectiveness of multiple
      evaluation functions against each other. That why, I could refine the 
      algorithm.
    - Database of opening moves.
    
"""

class AI:
    
    def __init__(self, nodes=3):
        """ Initialises the class and sets the node depth """
        self.nodes = nodes
        
    def run(self, gameboard, player):
        """ Runs the AI algorithm. Calls the minimax algorithm and then prunes the tree based on scores """
        tree = {
            "gameboard" : gameboard,
            "moves" : {},
        }
        self.createTree(gameboard, player, tree)
        
        # Let's now run through our tree and select the optimal path
        self.minimax(tree, player)
        
    def createTree(self, gameboard, player, tree, node=1):
        """ 
        This recursive createTree methods creates a tree of gameboards which we 
        can later use to find the optimal move to take.
        """
        # If we've reached a leaf node, it's time to exit out
        if self.reachedLeafNode(node):
            return
            
        # Let's iterate through all possible moves and add to our tree
        for move in self.rules.validMoves(player):
            gb = Gameboard.Gameboard(gameboard)
            gb.setPiece(move, player)

            tree["moves"][move] = {
                "gameboard" : gb, 
                "moves" : {}
            }
            
            self.createTree(gb, gb.opponent(player), tree["moves"][move], node + 1)
        
    def minimax(self, tree, player):
        """ Runs a minimax algorithm to select the best possible move """
    
    def reachedLeafNode(self, node):
        """ Returns true if we've reached a leaf node """
        if node > self.nodes:
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
        
        score = gameboard.score(player) - gameboard.score(gameboard.opponent(player))
        
        return score
        
    def setActivePlayer(self, player):
        """ Sets the active player (used in our minimax algorithm) """
        self.activePlayer = player
        
    def setRules(self, rules):
        """ Set the rules class """
        self.rules = rules