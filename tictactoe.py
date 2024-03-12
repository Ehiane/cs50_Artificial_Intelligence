"""
Testing Adversarial Search
S0: initial state
Player(S): returns which player to move in state s
Actions: returns a legal moves in state s
Result(s, a): returns state after action a taken in state s
Terminal(s): checks if state s is a terminal state
Utility(s): final numerical value for terminal state s
"""


gameboard = [[0,0,0] for x in range(3)] # a 3x3 array
print(gameboard)
