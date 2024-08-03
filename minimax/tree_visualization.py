from node import Node

def create_minimax_tree(depth):
    if depth == 0:
        return Node()
    node = Node()
    node.left = create_minimax_tree(depth - 1)
    node.right = create_minimax_tree(depth - 1)
    return node

def compute_minimax(node, is_max):
    if node.left is None and node.right is None:
        return node.value, None

    left_value, _ = compute_minimax(node.left, not is_max)
    right_value, _ = compute_minimax(node.right, not is_max)

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