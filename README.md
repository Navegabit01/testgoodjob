
# Simple Test Readme

This is a test for a great job




## Authors

- [@Navegabit01](https://github.com/Navegabit01)
(linkedin.com/in/luis-alberto-vidal-mesa-51113b272)


## Installation

Install my-project with pip

```bash
  Install Git or gh
  Install Node v16.16.0

  Clone the project
    git clone https://github.com/Navegabit01/testgoodjob.git 
      or
    gh repo clone Navegabit01/testgoodjob
  
  Linux Kubuntu:
    sudo apt install python3.10
  Windows:
    Download and install python3.10

  pip install -r requirements.txt

```

## Indications:
3 - Awnser: 
- Node.__init__(self, value): This operation has constant O(1) time complexity, since it simply assigns value to the variable self.value and sets self.left_child and self.right_child to None.

- BinaryTree.__init__(self): This operation also has O(1) constant time complexity, since it simply sets self.root to None.

- BinaryTree.insert(self, value): The complexity of this operation depends on the height of the tree. In the worst case, if the tree is completely unbalanced, the complexity would be O(n), where n is the number of nodes in the tree. However, on average, the complexity is O(log n) for balanced trees.

- BinaryTree._insert(self, value, current_node): This operation also has a complexity of O(log n) on average for balanced trees, since a binary search is performed to find the correct location to insert the new node.

- BinaryTree.find(self, value): The complexity of this operation also depends on the height of the tree. In the worst case, if the tree is completely unbalanced, the complexity would be O(n), where n is the number of nodes in the tree. However, on average, the complexity is O(log n) for balanced trees.

- BinaryTree._find(self, value, current_node): This operation also has a complexity of O(log n) on average for balanced trees, since a binary search is performed to find the node with the value value.

- BinaryTree.print_tree(self): This operation has a complexity of O(n), where n is the number of nodes in the tree, since the entire tree is recorded to print the values ​​of the nodes.

- BinaryTree._print_tree(self, current_node): This operation also has a complexity of O(n), where n is the number of nodes in the tree, since the entire tree is recorded to print the values ​​of the nodes.

4 - Awnser:
Binary search has the advantage that it significantly reduces the number of comparisons required to find an item in an ordered list. In a sequential search, each item in the list must be compared against the target until it finds a match or reaches the end of the list. In a binary search, the list is divided into two halves and the target is compared to the element in the middle. If the target is less than the element in the middle, the left half of the list is searched, and if it is greater, the right half is searched. In this way, half the list is discarded at each iteration, which significantly reduces the number of comparisons required.

In terms of computational complexity, binary search has a complexity of O(log n), while sequential search has a complexity of O(n). This means that binary search is much more efficient in terms of execution time for large lists, since the number of comparisons required grows much more slowly than in a sequential search.