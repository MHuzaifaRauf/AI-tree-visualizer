# A* Route Finder

This project implements the A* search algorithm to find the most optimal route between two cities in a graph-like network. It assists in finding the optimal path for a flight journey from a starting city to a destination city. The program reads data from a text file, constructs a graph representing the cities and their connections, and then utilizes the A* algorithm with straight-line distance heuristics to determine the most optimal route.

## Features

- Reads city data and distances from a text file.
- Constructs a graph-like network representing cities and their connections.
- Implements the A* search algorithm with straight-line distance heuristics.
- Finds the most optimal route from a starting city to a destination city.
- Displays the total distance of the route and the sequence of cities traversed.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/MHuzaifaRauf/astar-route-finder.git
```

2. Navigate to the project directory:

```bash
cd astar-route-finder
```

3. Install the required dependencies. Ensure you have Python installed on your system:

```bash
pip install -r requirements.txt
```

### Preparing the City Data File

Prepare your city data file (`cities.txt`). The file should list each node followed by the destinations it can reach, along with the corresponding distances and heuristics. The format should be as follows:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Oradea 380 Zerind 71 Sibiu 151
...
Bucharest 0 Pitesti 101 Fagaras 211 Giurgiu 90 Urziceni 85
Giurgiu 77 Bucharest 90
...
```

Each line starts with a node followed by its heuristic value. Then, the neighboring nodes and the distances from the parent node are given as pairs.

### Running the Program

Run the main script and follow the prompts:

```bash
python main.py
```

When prompted, input the start node and the destination node. For example:

```
Start node: Arad
Destination node: Bucharest
```

The program will then output the most optimal path and the total distance:

```
Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Total distance: 418 km
```

## File Structure

- `main.py`: The main script to run the program. It prompts the user for input, invokes the A* search, and prints the results.
- `graph_reader.py`: Module to read city data from a text file and construct a graph. It defines the `read_graph` function, which parses the input file and returns the graph and heuristics.
- `a_star.py`: Module implementing the A* search algorithm using the `simpleai` library. It defines the `FlightProblem` class and the `a_star_search` function.
- `cities.txt`: Sample data file containing city and distance information.
- `requirements.txt`: List of Python dependencies.

## Detailed Description of Project Working

### Step 1: Reading the Graph Data

The `graph_reader.py` module reads the city data from a text file and constructs a graph representation. The `read_graph` function processes the file and constructs two dictionaries:

- `graph`: A dictionary where each key is a city, and the value is another dictionary containing neighboring cities and distances.
- `heuristics`: A dictionary where each key is a city, and the value is the straight-line distance to Bucharest.

### Step 2: Defining the Search Problem

The `a_star.py` module defines the `FlightProblem` class, which inherits from `simpleai.search.SearchProblem`. This class overrides several methods to define the problem:

- `actions`: Returns a list of possible actions (neighboring cities) from a given state (current city).
- `result`: Returns the resulting state (next city) after taking an action (moving to a neighboring city).
- `is_goal`: Checks if the current state (city) is the goal (Bucharest).
- `cost`: Returns the cost (distance) of moving from one city to another.
- `heuristic`: Returns the heuristic value (straight-line distance to Bucharest) for a given state (city).

### Step 3: Performing the A* Search

The `a_star_search` function sets up the search problem and performs the A* search using the `simpleai.search.astar` function.

#### A* Algorithm Overview

The A* search algorithm is a popular pathfinding and graph traversal algorithm. It combines the strengths of Dijkstra's Algorithm and Greedy Best-First-Search by considering both the cost to reach the node and the estimated cost to reach the goal from the node. The formula used in A* is:

```
f(n) = g(n) + h(n)
```

Where:
- `g(n)` is the cost to reach the node `n` from the start node.
- `h(n)` is the estimated cost from node `n` to the goal (heuristic).
- `f(n)` is the total estimated cost of the cheapest solution through node `n`.

#### Using `simpleai` Library

The `simpleai` library simplifies the implementation of the A* algorithm. Here's how it works in this project:

1. **Defining the Problem**:
   - The `FlightProblem` class inherits from `simpleai.search.SearchProblem`.
   - It overrides the required methods to define the problem-specific details.
   - `actions(state)`: Returns a list of neighboring cities from the current city.
   - `result(state, action)`: Returns the next city after moving to a neighboring city.
   - `is_goal(state)`: Checks if the current city is the destination (Bucharest).
   - `cost(state1, action, state2)`: Returns the distance between two cities.
   - `heuristic(state)`: Returns the straight-line distance from the current city to Bucharest.

2. **Performing the Search**:
   - The `a_star_search` function initializes the `FlightProblem` class with the graph, heuristics, start node, and goal node.
   - It then calls `simpleai.search.astar` with this problem instance.
   - The `astar` function from `simpleai` handles the search process:
     - It uses a priority queue to explore nodes, prioritizing those with the lowest `f(n)` value.
     - It expands nodes by considering all possible actions (neighboring cities).
     - It calculates the cost to reach each neighboring city (`g(n)`) and the heuristic for each neighboring city (`h(n)`).
     - It continues exploring nodes until the goal node (Bucharest) is reached or all possible paths are exhausted.

3. **Handling the Result**:
   - The result of the search is a solution object containing the path and the total cost.
   - The path is extracted, and the start node is prepended to it to ensure the full path is displayed.

### Step 4: Running the Program

The `main.py` script is the entry point of the program. It:

1. Reads the city data file and constructs the graph and heuristics.
2. Prompts the user for the start and destination cities.
3. Calls the `a_star_search` function to find the optimal path.
4. Prints the path and the total distance if a path is found, or an error message if no path is found.

## Dependencies

- Python 3.x
- `simpleai` library

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
