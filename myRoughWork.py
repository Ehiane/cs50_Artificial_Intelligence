"""
My attempt to follow along what was going on in the link shared in main
"""

from enum import Enum
class Action(Enum):
    """
    actions of a piece in a sliding puzzle
    """
    UP = 0
    DOWN = 1
    LEFT = 3
    RIGHT = 4
    STATIC = None

class State:
    def __init__(self, name):
        self.name = name if name else "empty"
        self.matrix = [[]] #this may not be needed all the time 

class Node:
    """
    The basic unit of a graph. 
    Keeps tracks of the state, parent, action, path_cost and next ptr
    """
    def __init__(self, state=State(name=""), parent=None, action=Action.STATIC, path_cost=0):
        self.state = state
        self.parent = parent if parent else None
        self.action = action
        self.path_cost = path_cost if path_cost else 0
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.state.name}"

    
class Graph:
    """
    The basic unit of a graph. 
    Keeps tracks of the state, parent, action, path_cost and next ptr
    """
    def __init__(self, headptr: Node):
        self.headptr = headptr if headptr else Node()

    def __repr__(self):
        nodes = []
        queue = [(self.headptr, "Root")]
        while queue:
            current, position = queue.pop(0)
            if current:
                nodes.append(f"{position}: {current}")
                queue.append((current.left, f"{current.state.name}'s Left"))
                queue.append((current.right, f"{current.state.name}'s Right"))
        return " -> ".join(nodes)
    

    def populateGraph(self, states):
        self.headptr = Node(state=State(name=states[0]))
        current = self.headptr
        for i, state_name in enumerate(states[1:], start=1):
            new_node = Node(state=State(name=state_name))
            if current.state.name == "B":
                if current.left is None:
                    current.left = new_node
                elif current.right is None:
                    current.right = new_node
                    current = current.right  # Move to the right node (D)
            else:
                current.left = new_node
                current = current.left
        return self



def main():
    path = Graph(headptr=Node()) 
    path.populateGraph([chr(i) for i in range(65,71)] ) #65- A & 71- F in ascii values 
    print(path)

main()