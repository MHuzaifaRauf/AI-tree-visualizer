class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.pruned = False  # Flag to indicate if the node was pruned