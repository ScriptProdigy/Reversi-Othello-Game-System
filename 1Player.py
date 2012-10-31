#!/usr/bin/env python

import Reversi
import AI as ReversiAI

print "REVERSI AI ENGINE - 1 PLAYER MODE"
print "By Alex Berriman 2012\n"

reversi = Reversi.Reversi()

# Starting player is black
player = Reversi.Gameboard.BLACK
reversi.ai.setActivePlayer(player)

print reversi.ai.run(reversi.gameboard, reversi.gameboard.opponent(player))
