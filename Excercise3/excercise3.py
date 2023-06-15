ERROR_TREE_INSERT = 'Error al insertar el valor en el árbol:'
ERROR_EXIST_VALUE = 'El valor ya existe en el árbol:'
ERROR_SEARCH_VALUE = 'Error al buscar el valor en el árbol:'
ERROR_PRINT_TREE = 'Error al imprimir el árbol:'


class Node:
    """
        Node for the tree
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    """
        Class binary tree
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        try:
            if self.root is None:
                self.root = Node(value)
            else:
                self._insert(value, self.root)
        except Exception as error:
            print(ERROR_TREE_INSERT, error)
            return ValueError(ERROR_TREE_INSERT)

    def _insert(self, value, current_node):
        try:
            if value < current_node.value:
                if current_node.left_child is None:
                    current_node.left_child = Node(value)
                else:
                    self._insert(value, current_node.left_child)
            elif value > current_node.value:
                if current_node.right_child is None:
                    current_node.right_child = Node(value)
                else:
                    self._insert(value, current_node.right_child)
            else:
                return ValueError(ERROR_EXIST_VALUE)
        except Exception as error:
            return ValueError(error)

    def find(self, value):
        try:
            if self.root is not None:
                return self._find(value, self.root)
            else:
                return False
        except Exception as error:
            print(ERROR_SEARCH_VALUE, error)
            return ValueError(ERROR_SEARCH_VALUE, error)

    def _find(self, value, current_node):
        try:
            if value == current_node.value:
                return True
            elif value < current_node.value and current_node.left_child is not None:
                return self._find(value, current_node.left_child)
            elif value > current_node.value and current_node.right_child is not None:
                return self._find(value, current_node.right_child)
            else:
                return False
        except Exception as error:
            return ValueError(error)

    def print_tree(self):
        try:
            if self.root is not None:
                self._print_tree(self.root)
        except Exception as error:
            print(ERROR_PRINT_TREE, error)
            return ValueError(ERROR_PRINT_TREE, error)

    def _print_tree(self, current_node):
        try:
            if current_node is not None:
                self._print_tree(current_node.left_child)
                print(str(current_node.value))
                self._print_tree(current_node.right_child)
        except Exception as error:
            return ValueError(error)


def test_insert():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    assert binary_tree.root.value == 5


def test_find():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    assert binary_tree.find(5) == True
    assert binary_tree.find(3) == True
    assert binary_tree.find(7) == True
    assert binary_tree.find(10) == False


def test_print_tree(capsys):
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.print_tree()
    captured = capsys.readouterr()
    assert captured.out == "3\n5\n7\n"
