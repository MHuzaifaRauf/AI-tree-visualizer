# AI Algorithm Visualizer

This project implements and visualizes three important AI algorithms: A* search for route finding, Minimax for decision making, and Alpha-Beta Pruning for optimized decision making in game trees. All algorithms are equipped with graphical user interfaces (GUIs) for enhanced user interaction and visualization.

## Features

### A* Route Finder
- Reads city data and distances from a text file.
- Constructs a graph-like network representing cities and their connections.
- Implements the A* search algorithm with straight-line distance heuristics.
- Finds the most optimal route from a starting city to a destination city.
- Displays the total distance of the route and the sequence of cities traversed.
- Provides a GUI for easy input and visualization of results.

### Minimax Decision Tree
- Implements the Minimax algorithm for decision making in a tree structure.
- Allows users to create and manipulate decision trees.
- Provides a GUI for tree creation, visualization, and algorithm execution.
- Displays the Minimax values and optimal decisions at each node.

### Alpha-Beta Pruning
- Implements the Alpha-Beta Pruning algorithm to optimize the Minimax decision-making process.
- Reduces the number of nodes evaluated in the decision tree.
- Provides a GUI for tree creation, visualization, and algorithm execution.
- Displays the Minimax values and optimal decisions at each node with pruning.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/MHuzaifaRauf/AI-tree-visualizer.git
```

2. Navigate to the project directory:

```bash
cd AI-tree-visualizer
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## A* Route Finder

### Preparing the City Data File

Prepare your city data file (`cities.txt`) in the `astar_route_finder` directory. The file format should be as follows:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
...
```

### Running the A* Route Finder GUI

Navigate to the `astar_route_finder` directory and run:

```bash
python main.py
```

Use the GUI to select start and destination cities, and visualize the optimal path.

## Minimax Decision Tree

### Running the Minimax GUI

Navigate to the `minimax` directory and run:

```bash
python main.py
```

Use the GUI to create a decision tree, set node values, and visualize the Minimax algorithm's execution.

## Alpha-Beta Pruning

### Running the Alpha-Beta Pruning GUI

Navigate to the `alpha-beta-pruning` directory and run:

```bash
python main.py
```

Use the GUI to create a decision tree, set node values, and visualize the Alpha-Beta Pruning algorithm's execution.

## File Structure

- `astar_route_finder/`
  - `a_star.py`: Implements the A* search algorithm.
  - `graph_reader.py`: Reads city data and constructs the graph.
  - `gui.py`: Provides the GUI for the A* route finder.
  - `main.py`: Entry point for the A* route finder.
  - `cities.txt`: Sample city data file.

- `minimax/`
  - `main.py`: Entry point for the Minimax GUI.
  - `minimax_tree.py`: Implements the GUI for the Minimax tree and Handles tree visualization
  - `node.py`: Defines the tree node structure.


- `alpha-beta-pruning/`
  - `main.py`: Entry point for the Alpha-Beta Pruning GUI.
  - `node.py`: Defines the tree node structure.
  - `alpha_beta_tree_gui.py`: Implements the Alpha-Beta Pruning algorithms.

- `requirements.txt`: List of Python dependencies.

## Dependencies

- Python 3.x
- PyQt5
- simpleai

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.