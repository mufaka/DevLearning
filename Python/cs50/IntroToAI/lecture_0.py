import sys 
from maze import Maze

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    m = Maze(sys.argv[1])
    print("Maze:")
    m.print()
    print("Solving...")
    m.solve()
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image("maze.png", show_explored=True)

if __name__ == "__main__":
    main()

"""
Search. Agent looks for a solution to a problem.

Agent: entity that percieves environment and acts upon it
State: a configuration of the agent and it's environment
Intial State: The state where the agent begins (starting point for search algorithm)
Actions: Choices that can be made in any state    


Actions(s) returns the set of actions that can be executed in state s.

eg: 15 puzzle (tiles that need ordered). Actions can be slide righ, left, up, down.


Transistion Model: a description of what state results from performing any applicable action in any state. How actions relate to state.
    Result(s, a) returns the state resulting from performing action a in state s


State Space: The set of all states reachable from the initial state by any sequence of actions.
    State Graph; transitions. Finite State Machine ...

Goal Test: way to determine whether a given state is a goal state.

Path Cost: numerical cost associated with a given path. (many ways to reach goal state, which costs less)


Summary: Search Problems
    Initial State - beginning state
    Actions - actions that can be taken in the state
    Transistion Model - given a state and an action, what state is the result?
    Goal Test - Did we reach the goal
    Path Cost Function - how much did the path cost.

Solution: a sequence of actions that leads from the initial state to a goal state. 
Optimal Solution: The solution with the smallest cost.

Node:
    A state
    A parent (node that generated this node)
    An Action (action applied to parent to get node)
    A path cost (from initial state to node)

Approach:
    Start with a Frontier (contains nodes to explore) that contains initial state
    Start with an empty explored set
    Repeat:
        If the frontier is empty
            return no solution
        Else
            Remove a node from the Frontier

            If that node is goal state
                Return the solution
            Else
                Add node to the explored set

                Expand node (the possible destinations)

                Add resulting nodes to the frontier if they aren't already in the frontier or the explored set

*** Important how the frontier is structured.
    Stack: last-in first-out 
    Depth-first search with stack - Might not find the optimal solution

    Breadth-first search, use FIFO (Queue) - Will find optimal solution

    Uninformed Search: no problem specific knowledge
    DFS and BFS are uninformed searches

    Informed Search: Uses problem-specific knowledge to find solutions more efficiently
        Greedy Best First Search (GBFS)
            expands the node that (it thinks) is closest to the goal as estimated by a heuristic function h(n)
                Manhattan distance. Horizontal and Veritical steps to get to goal (ignoring barriors).

        A* Search: Expands node with lowest value of g(n) + h(n)
            g(n) = cost to reach node (steps taken)
            h(n) = estimated cost to goal (like GBFS)

            optimal if:
                h(n) is admissable (never overestimates the true cost)
                h(n) is consistent (for every node n and successor n' with step cost c, h(n) less or equal h(n') + c)
                    means: h(n) must always be less than or equal h(n) + cost

            The heuristic is often the challenge in finding the solution


    Adversarial Search
        Something has an opposite objective (like tic-tac-toe)

        Minimax algorithm
            tic-tac-toe outcomes:
            -1 o wins, 0 cats game, 1 x wins


        MAX (X player) aims to maximize score (ideally 1, if not then 0)
        MIN (O player) aims to minimize score (ideally -1, if not then 0)

        Game:
            S0: Initial State
            Player(s): returns which player to move in state s
            Action(s): returns legal moves in state s
            Result(s, a): returns state after action a taken in state s
            Terminal(s): checks if state s is a terminal state (game over)
            Utility(s): final numerical value for terminal state s (-1, 0, 1 for tic-tac-toe)
        
            S0: empty game board for initial state in tic-tac-toe

            minimax calculates outcome based on all possible moves. consider O is up:

                    _ X O
                    O X X
                    X _ O

            O X O          _ X O
            O X X          O X X
            X _ O          X O X

            O X O          O X O
            O X X          O X X
            X X O          X O X                     

            Util = 1       Util = 0

            O is trying to minimize Util (X is trying to max); so O would pick the second option for it's move

        
        function Max-Value(state):
            if Terminal(state):
                return Utility(state)
            
            v = -infinity (as low as possible)
            for action in Actions(state):
                v = Max(v, Min-Value(Result(state, action)))
            return v

        function Min-Value(state):
            if Terminal(state):
                return Utility(state)
            
            v = +infinity (as high as possible)
            for action in Actions(state):
                v = Min(v, Max-Value(Result(state, action)))
            return v


        Optimizations to minimax:
            Alpha-Beta Pruning (remove branches from the search tree)
                stop calculating a node if you know is already not optimal for you

            Depth-Limited Minimax
                stop calculating at a certain level of recursion

                Needs evaluation function that estimates the expected utility from a given game state
                    needed because if you don't traverse fully, you might not get a terminal state

"""
