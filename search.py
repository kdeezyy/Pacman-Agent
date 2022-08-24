# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

# code so autograder can run on python 3.9
import cgi, html

cgi.escape = html.escape


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]




def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #Following the DFS Algorithm pseudo code provided in Slide 25 of L02 StateSpaceSearch

    #open: = [Start];
    # Stores the nodes that we will transverse in provided stack
    # Grabs start state and pushed it onto stack( we don't know direction so its blank, and action cost is 0
    # since we are starting from it.
    states = util.Stack()
    states.push([(problem.getStartState(), "", 0)])

    # closed : = [];
    # Will store the  nodes that we have visited
    visited = []


    #while open  != [] do
    #loops while states is not empty
    while not states.isEmpty():
        #remove leftmost state from open
        path = states.pop()
        x = path[len(path)-1]
        x = x[0]

        # if X is goal, then return SUCCESS(in our case we also return the steps/direction needed to get there)
        if problem.isGoalState(x):
            directionList = []
            for direction in path[1:]:
                directionList.append(direction[1])
            return directionList


        #Else
        elif x not in visited:

            #generate children of x(get successor)
            for successor in problem.getSuccessors(x):
                if successor[0] not in visited:
                    successorPath = []
                    for y in path:
                        successorPath.append(y)
                    successorPath.append(successor)
                    states.push(successorPath)

            #put X on closed(Check if coordinate/node has been visited already, if not, we append it to our visit list)
            visited.append(x)

    return visited

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    #CODE DIRECTLY SAME AS DFS EXCEPT util.Stack() is changed to util.Queue()


    # open: = [Start];
    # Stores the nodes that we will transverse in provided stack
    # Grabs start state and pushed it onto stack( we don't know direction so its blank, and action cost is 0
    # since we are starting from it.
    states = util.Queue()
    states.push([(problem.getStartState(), "", 0)])

    # closed : = [];
    # Will store the  nodes that we have visited
    visited = []

    # while open  != [] do
    # loops while states is not empty
    while not states.isEmpty():
        # remove leftmost state from open
        path = states.pop()
        x = path[len(path) - 1]
        x = x[0]

        # if X is goal, then return SUCCESS(in our case we also return the steps/direction needed to get there)
        if problem.isGoalState(x):
            directionList = []
            for direction in path[1:]:
                directionList.append(direction[1])
            return directionList


        # Else
        elif x not in visited:

            # generate children of x(get successor)
            for successor in problem.getSuccessors(x):
                if successor[0] not in visited:
                    successorPath = []
                    for y in path:
                        successorPath.append(y)
                    successorPath.append(successor)
                    states.push(successorPath)

            # put X on closed(Check if coordinate/node has been visited already, if not, we append it to our visit list)
            visited.append(x)

    return visited


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Stores the nodes that we will transverse in provided stack
    # Grabs start state and pushed it onto stack( we don't know direction so its blank, and action cost is 0
    # since we are starting from it.
    states = util.PriorityQueue()
    states.push((problem.getStartState(), [], 0), 0)


    # closed : = [];
    # Will store the  nodes that we have visited
    visited = []

    # while open  != [] do
    # loops while states is not empty
    while not states.isEmpty():

        #explores the first node in the states Priority Queue
        state, actions, cost = states.pop()


        #since we are exploring the first node, we then put it in our visited node list
        currentNode = (state, cost)
        visited.append((state, cost))

        # if the currentNode is the goal, then return SUCCESS/actions
        if problem.isGoalState(state):
            return actions

        #else we continue until we find our goal
        else:

            # stores the successors of the first node in "successors" variable
            successors = problem.getSuccessors(state)

            # Examine each successor
            for successorState, successorAction, successorCost in successors:
                newAction = actions + [successorAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (successorState, newAction, newCost)

                # check if this successor has been explored
                explored_already = False
                for explored in visited:
                    exploredState, exploredCost = explored

                    #sets boolean value to true if our successor has been explored already
                    if (successorState == exploredState) and (newCost >= exploredCost):
                        explored_already = True

                #If the successor was not explored already, we then add it to our visited list after we have explored it
                if not explored_already:
                    states.push(newNode, newCost + heuristic(successorState, problem))
                    visited.append((successorState, newCost))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
