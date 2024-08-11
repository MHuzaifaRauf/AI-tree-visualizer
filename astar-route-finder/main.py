import sys
from PyQt5.QtWidgets import QApplication
from graph_reader import read_graph
from gui import AStarGUI

def main():
    file_path = 'cities.txt'
    graph, heuristics = read_graph(file_path)

    app = QApplication(sys.argv)
    ex = AStarGUI(graph, heuristics)
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()