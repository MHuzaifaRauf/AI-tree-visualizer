# A* Route Finder

This project implements the A* search algorithm to find the most optimal route between two cities in a graph-like network. It assists in finding the optimal path for a flight journey from a starting city to a destination city. The program reads data from a text file, constructs a graph representing the cities and their connections, and then utilizes the A* algorithm with straight-line distance heuristics to determine the most optimal route.

## Features

- Reads city data and distances from a text file.
- Constructs a graph-like network representing cities and their connections.
- Implements the A* search algorithm with straight-line distance heuristics.
- Finds the most optimal route from a starting city to a destination city.
- Displays the total distance of the route and the sequence of cities traversed.

## Getting Started

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

4. Prepare your city data file. The file should list each node followed by the destinations it can reach, along with the corresponding distances and heuristics. The format should be as follows:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Oradea 380 Zerind 71 Sibiu 151
...
Bucharest 0 Pitesti 101 Fagaras 211 Giurgiu 90 Urziceni 85
Giurgiu 77 Bucharest 90
...
```

5. Run the main script:

```bash
python main.py
```

6. Follow the prompts to input the start node and destination node.

## Example

```bash
Start node: Arad
Destination node: Bucharest

Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Total distance: 418 km
```

## File Structure

- `main.py`: The main script to run the program.
- `graph_reader.py`: Module to read city data from a text file and construct a graph.
- `a_star.py`: Module implementing the A* search algorithm using the `simpleai` library.
- `cities.txt`: Sample data file containing city and distance information.
- `README.md`: Documentation providing an overview of the project and instructions for use.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- Python 3.x
- `simpleai` library

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.