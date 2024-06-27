from simpleai.search import astar, SearchProblem

class FlightProblem(SearchProblem):
    def __init__(self, graph, heuristics, start, goal):
        self.graph = graph
        self.heuristics = heuristics
        self.initial_state = start
        self.goal = goal

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return self.graph[state][action]

    def heuristic(self, state):
        return self.heuristics[state]


def a_star_search(graph, heuristics, start, goal):
    problem = FlightProblem(graph, heuristics, start, goal)
    result = astar(problem)
    
    if result is not None:
        path = [state for state, action in result.path() if state is not None]
        return [start] + path, result.cost
    else:
        return None, float('inf')