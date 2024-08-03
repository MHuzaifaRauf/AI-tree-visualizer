import random
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QBrush
from PyQt5.QtCore import Qt, QPointF
from a_star import a_star_search

class AStarGUI(QWidget):
    def __init__(self, graph, heuristics):
        super().__init__()
        self.graph = graph
        self.heuristics = heuristics
        self.path = None
        self.total_distance = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('A* Search Visualization')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Input fields
        input_layout = QHBoxLayout()
        self.start_input = QLineEdit()
        self.goal_input = QLineEdit()
        input_layout.addWidget(QLabel('Start:'))
        input_layout.addWidget(self.start_input)
        input_layout.addWidget(QLabel('Goal:'))
        input_layout.addWidget(self.goal_input)
        layout.addLayout(input_layout)

        # Search button
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        # Result display
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Generate random positions for nodes
        self.generate_positions()

    def generate_positions(self):
        self.positions = {}
        width = self.width() - 100
        height = self.height() - 100
        for node in self.graph:
            while True:
                x = random.randint(100, width + 700)
                y = random.randint(100, height + 500)
                if not any(abs(x - px) < 100 and abs(y - py) < 100 for px, py in self.positions.values()):
                    self.positions[node] = (x, y)
                    break

    def perform_search(self):
        start = self.start_input.text().strip().capitalize()
        goal = self.goal_input.text().strip().capitalize()

        if start not in self.graph or goal not in self.graph:
            self.result_label.setText("Invalid start or goal node.")
            return

        self.path, self.total_distance = a_star_search(self.graph, self.heuristics, start, goal)

        if self.path:
            result_text = f"Path: {' -> '.join(self.path)}\nTotal distance: {self.total_distance} km"
            self.result_label.setText(result_text)
            self.update()
        else:
            self.result_label.setText("NO PATH FOUND")
            self.path = None
            self.total_distance = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the graph
        self.draw_graph(painter)

        # Draw the path if available
        if self.path:
            self.draw_path(painter)

    def draw_graph(self, painter):
        # Center the graph
        self.center_graph()

        # Draw edges
        painter.setPen(QPen(Qt.black, 0.5))
        for node, neighbors in self.graph.items():
            x1, y1 = self.positions[node]
            for neighbor, distance in neighbors.items():
                x2, y2 = self.positions[neighbor]
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))
                # Draw the distance
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                painter.drawText(int(mid_x), int(mid_y), str(distance))

        # Draw nodes
        for node, (x, y) in self.positions.items():
            painter.setBrush(QColor(200, 200, 255))
            painter.setPen(Qt.black)
            painter.drawEllipse(QPointF(x, y), 30, 30)
            painter.drawText(int(x - 10), int(y + 5), node)

    def draw_path(self, painter):
        if not self.path or len(self.path) < 2:
            return

        # Draw path
        painter.setPen(QPen(Qt.red, 3))
        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]
            x1, y1 = self.positions[start]
            x2, y2 = self.positions[end]
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Highlight start and end nodes
        start = self.path[0]
        end = self.path[-1]
        
        # Start node (green)
        x, y = self.positions[start]
        painter.setBrush(QColor(0, 255, 0, 100))
        painter.setPen(Qt.green)
        painter.drawEllipse(QPointF(x, y), 35, 35)
        painter.drawText(int(x - 15), int(y + 5), "Start")

        # End node (red)
        x, y = self.positions[end]
        painter.setBrush(QColor(255, 0, 0, 100))
        painter.setPen(Qt.red)
        painter.drawEllipse(QPointF(x, y), 35, 35)
        painter.drawText(int(x - 15), int(y + 5), "End")

    def center_graph(self):
        # Calculate the bounding box of the graph
        min_x = min(pos[0] for pos in self.positions.values())
        max_x = max(pos[0] for pos in self.positions.values())
        min_y = min(pos[1] for pos in self.positions.values())
        max_y = max(pos[1] for pos in self.positions.values())

        # Calculate the center of the bounding box
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        # Calculate the center of the widget
        widget_center_x = self.width() / 2
        widget_center_y = self.height() / 2

        # Calculate the offset to center the graph
        offset_x = widget_center_x - center_x
        offset_y = widget_center_y - center_y

        # Apply the offset to all positions
        for node in self.positions:
            x, y = self.positions[node]
            self.positions[node] = (x + offset_x, y + offset_y)