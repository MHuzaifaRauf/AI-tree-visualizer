import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from node import Node
from tree_visualization import create_minimax_tree, compute_minimax

class MinimaxTreeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cancel_flag = False

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
        self.cancel_flag = False
        depth = int(self.depthInput.text())
        self.root = create_minimax_tree(depth)
        self.getLeafValues(self.root)
        if not self.cancel_flag:
            _, self.path = compute_minimax(self.root, True)
            self.visualizeTree(self.root, depth, path=self.path)

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

    def visualizeTree(self, node, depth, x=400, y=50, dx=200, path=''):
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
            if path == 'left':
                line.setPen(QPen(Qt.red, 2))
            else:
                line.setPen(pen)
            self.scene.addItem(line)
            self.visualizeTree(node.left, depth - 1, x - dx, y + 80, dx // 2, 'left' if path == 'left' else '')

        if node.right:
            line = QGraphicsLineItem(x + 15, y + 30, x + dx + 15, y + 80)
            if path == 'right':
                line.setPen(QPen(Qt.red, 2))
            else:
                line.setPen(pen)
            self.scene.addItem(line)
            self.visualizeTree(node.right, depth - 1, x + dx, y + 80, dx // 2, 'right' if path == 'right' else '')