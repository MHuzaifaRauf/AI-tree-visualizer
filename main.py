from graph_reader import read_graph
from a_star import a_star_search

def main():
    file_path = 'cities.txt'
    graph, heuristics = read_graph(file_path)
    
    start = input("Start node: ").strip()
    goal = input("Destination: ").strip()
    
    if start not in graph and goal not in graph:
        print("Invalid start and destination node.")
        return
    elif start not in graph:
        print("Invalid start node.")
        return
    elif goal not in graph:
        print("Invalid destination node.")
        return
    
    path, total_distance = a_star_search(graph, heuristics, start, goal)
    
    # print("DEBUG: Path:", path)
    # print("DEBUG: Total distance:", total_distance)
    
    if path:
        if path[0] is None or None in path[1:]:
            print("NO PATH FOUND")
        else:
            print(f"Path: {' -> '.join(path)}")
            print(f"Total distance: {total_distance} km")
    else:
        print("NO PATH FOUND")


if __name__ == "__main__":
    main()