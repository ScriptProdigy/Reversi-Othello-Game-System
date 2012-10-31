## Reversi/Othello Game System
### By Alex Berriman <alexb@bezz.com.au>

A very simple Reversi game created in Python which shows a bit of intelligence. It uses a revised [minimax](http://en.wikipedia.org/wiki/Minimax) algorithm (though more of an implementation of a [negamax](http://en.wikipedia.org/wiki/Negamax) algorithm) with a (rather greedy) evaluation function to select the best possible subset of moves. The AI algorithm is able to build a decision tree with a configurable depth, the idea being the deeper the decision tree the more intelligent the decision.

### Invoking the AI object
First and foremost, you need to instantiate an instance of the Reversi class:

```python
import reversi.Reversi as Reversi
reversi = Reversi.Reversi()
```