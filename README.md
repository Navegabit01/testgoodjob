
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
    
## Run Locally

Go to the project directory

```bash
  cd my-project
```
```bash
  ./start.sh
```


## Indications:
3 - Response: 
- Node.__init__(self, value): Esta operación tiene una complejidad de tiempo constante O(1), ya que simplemente asigna el valor value a la variable self.value y establece self.left_child y self.right_child en None.

- BinaryTree.__init__(self): Esta operación también tiene una complejidad de tiempo constante O(1), ya que simplemente establece self.root en None.

- BinaryTree.insert(self, value): La complejidad de esta operación depende de la altura del árbol. En el peor de los casos, si el árbol está completamente desequilibrado, la complejidad sería O(n), donde n es el número de nodos en el árbol. Sin embargo, en promedio, la complejidad es O(log n) para árboles balanceados.

- BinaryTree._insert(self, value, current_node): Esta operación también tiene una complejidad de O(log n) en promedio para árboles balanceados, ya que se realiza una búsqueda binaria para encontrar la ubicación correcta para insertar el nuevo nodo.

- BinaryTree.find(self, value): La complejidad de esta operación también depende de la altura del árbol. En el peor de los casos, si el árbol está completamente desequilibrado, la complejidad sería O(n), donde n es el número de nodos en el árbol. Sin embargo, en promedio, la complejidad es O(log n) para árboles balanceados.

- BinaryTree._find(self, value, current_node): Esta operación también tiene una complejidad de O(log n) en promedio para árboles balanceados, ya que se realiza una búsqueda binaria para encontrar el nodo con el valor value.

- BinaryTree.print_tree(self): Esta operación tiene una complejidad de O(n), donde n es el número de nodos en el árbol, ya que se recorre todo el árbol para imprimir los valores de los nodos.

- BinaryTree._print_tree(self, current_node): Esta operación también tiene una complejidad de O(n), donde n es el número de nodos en el árbol, ya que se recorre todo el árbol para imprimir los valores de los nodos.

4 - Response:
La búsqueda binaria tiene la ventaja de que reduce significativamente el número de comparaciones necesarias para encontrar un elemento en una lista ordenada. En una búsqueda secuencial, se debe comparar cada elemento de la lista con el objetivo hasta encontrar una coincidencia o llegar al final de la lista. En una búsqueda binaria, se divide la lista en dos mitades y se compara el objetivo con el elemento en el medio. Si el objetivo es menor que el elemento en el medio, se busca en la mitad izquierda de la lista, y si es mayor, se busca en la mitad derecha. De esta manera, se descarta la mitad de la lista en cada iteración, lo que reduce significativamente el número de comparaciones necesarias.

En cuanto a la complejidad computacional, la búsqueda binaria tiene una complejidad de O(log n), mientras que la búsqueda secuencial tiene una complejidad de O(n). Esto significa que la búsqueda binaria es mucho más eficiente en términos de tiempo de ejecución para listas grandes, ya que el número de comparaciones necesarias crece mucho más lentamente que en una búsqueda secuencial.


