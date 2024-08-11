from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from node import Node

class MinimaxTreeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cancel_flag = False  # Flag to indicate if the process should be canceled
        self.final_path = []  # List to store the final path

    def initUI(self):
        self.setWindowTitle('Minimax Tree Visualization')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.depthLayout = QHBoxLayout()
        self.depthLabel = QLabel('Depth:')
        self.depthInput = QLineEdit()
        self.depthLayout.addWidget(self.depthLabel)
        self.depthLayout.addWidget(self.depthInput)

        self.layout.addLayout(self.depthLayout)

        self.createButton = QPushButton('Create Minimax Tree')
        self.createButton.clicked.connect(self.createTree)
        self.layout.addWidget(self.createButton)

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)

        self.setLayout(self.layout)

    def createTree(self):
        self.scene.clear()
        self.cancel_flag = False  # Reset the cancel flag
        self.final_path = []  # Reset the final path
        depth = int(self.depthInput.text())
        self.root = self.createMinimaxTree(depth)
        self.getLeafValues(self.root)
        if not self.cancel_flag:
            _, self.path = self.computeMinimax(self.root, True)
            self.storeFinalPath(self.root)
            self.visualizeTree(self.root, depth)

    def createMinimaxTree(self, depth):
        if depth == 0:
            return Node()
        node = Node()
        node.left = self.createMinimaxTree(depth - 1)
        node.right = self.createMinimaxTree(depth - 1)
        return node

    def getLeafValues(self, node):
        if self.cancel_flag:
            return
        if node.left is None and node.right is None:
            value, ok = QInputDialog.getInt(self, 'Leaf Values', 'Value for leaf node left to right:')
            if ok:
                node.value = value
            else:
                self.cancel_flag = True
            return
        if node.left:
            self.getLeafValues(node.left)
        if node.right:
            self.getLeafValues(node.right)

    def computeMinimax(self, node, is_max):
        if node.left is None and node.right is None:
            return node.value, None

        left_value, _ = self.computeMinimax(node.left, not is_max)
        right_value, _ = self.computeMinimax(node.right, not is_max)

        if is_max:
            if left_value >= right_value:
                node.value = left_value
                return node.value, 'left'
            else:
                node.value = right_value
                return node.value, 'right'
        else:
            if left_value <= right_value:
                node.value = left_value
                return node.value, 'left'
            else:
                node.value = right_value
                return node.value, 'right'

    def storeFinalPath(self, node):
        if node is None:
            return
        if node.left and node.left.value == node.value:
            self.final_path.append(node.left)
            self.storeFinalPath(node.left)
        elif node.right and node.right.value == node.value:
            self.final_path.append(node.right)
            self.storeFinalPath(node.right)

    def visualizeTree(self, node, depth, x=400, y=50, dx=200):
        if node is None:
            return

        if depth % 2 == 0:
            item = QGraphicsEllipseItem(x, y, 30, 30)
        else:
            item = QGraphicsRectItem(x, y, 30, 30)

        pen = QPen(Qt.black)
        pen.setWidth(2)
        item.setPen(pen)

        self.scene.addItem(item)
        text = QGraphicsTextItem(str(node.value))
        text.setPos(x + 5, y + 5)
        self.scene.addItem(text)

        if node.left:
            line = QGraphicsLineItem(x + 15, y + 30, x - dx + 15, y + 80)
            if node.left in self.final_path:
                line.setPen(QPen(Qt.green))
            else:
                line.setPen(pen)
            self.scene.addItem(line)
            self.visualizeTree(node.left, depth - 1, x - dx, y + 80, dx // 2)

        if node.right:
            line = QGraphicsLineItem(x + 15, y + 30, x + dx + 15, y + 80)
            if node.right in self.final_path:
                line.setPen(QPen(Qt.green))
            else:
                line.setPen(pen)
            self.scene.addItem(line)
            self.visualizeTree(node.right, depth - 1, x + dx, y + 80, dx // 2)