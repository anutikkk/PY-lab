Лабораторна робота №12: Using nested lists to create and manipulate two-dimensional data structures
___
Мета роботи:
Ця лабораторна робота має на меті ознайомити з основами роботи з матрицями у мові програмування Python, використовуючи класи і методи. Кожне завдання спрямоване на розширення знань щодо створення, модифікації та операцій з матрицями, що є важливим аспектом для розуміння алгоритмів обробки даних та математичних обчислень.
___
Опис завдання:
Task 1: Create a Matrix
Create a Python class Matrix that initializes a two-dimensional list with zeros.
The constructor should accept two parameters: rows and columns, indicating the
dimensions of the matrix.
Example of class usage:matrix = Matrix(2, 3)
print(matrix.data) # [[0, 0, 0], [0, 0, 0]]
Task 2: Add Elements to Matrix
Extend the Matrix class by adding a method add_element that adds an element
at a specific position (row, column).
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(1, 2, 10)
print(matrix.data) # [[0, 0, 10], [0, 0, 0]]
Task 3: Sum of Rows
Add a method sum_of_rows to the Matrix class that returns a list of sums of
each row in the matrix.
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows()) # [15, 20]
Task 4: Matrix Transposition
Create a method transpose in the Matrix class that returns a new Matrix
object, which is the transpose of the original matrix.
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data) # [[0, 0], [1, 0], [0, 2]]
Task 5: Multiply Matrices
Implement a method multiply_by in the Matrix class that accepts another
Matrix object and returns a new Matrix object that is the result of the multiplication
of the two matrices.
Example of class usage:matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data) # [[14, 0], [0, 0]]
Task 6: Check Symmetric Matrix
Add a method is_symmetric to the Matrix class that checks if the matrix is
symmetric (i.e., the matrix is equal to its transpose).
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric()) # True
Task 7: Rotate Matrix
Implement a method rotate_right in the Matrix class that rotates the matrix
90 degrees to the right.
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data) # [[3, 1], [4, 2]]
Task 8: Flatten Matrix
Create a method flatten in the Matrix class that returns a single list containing
all elements of the matrix.
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten()) # [1, 2, 3, 4]
Task 9: Matrix from List
Add a static method from_list to the Matrix class that creates a matrix object
from a given list of lists.
Example of class usage:
python
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]
Task 10: Extract Diagonal
Create a method diagonal in the Matrix class that extracts the diagonal of a
square matrix as a list.
Example of class usage:matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal()) # [1, 2, 3]
___
Виконання роботи:
```Python
from typing import List

class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0] * cols for _ in range(rows)]
        else:
            self.data = data

    def add_element(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise ValueError("Invalid position.")

    def sum_of_rows(self):
        return [sum(self.data[row]) for row in range(self.rows)]

    def transpose(self):
        transpose_data = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return Matrix(self.cols, self.rows, transpose_data)

    def multiply_by(self, other):
        if self.cols != other.rows:
            raise ValueError("Cannot multiply matrices: incompatible dimensions.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for x in range(self.cols):
                    result.data[i][j] += self.data[i][x] * other.data[x][j]
        return result

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.data = rotated_data
        self.rows, self.cols = self.cols, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0])
        matrix = Matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square.")
        return [self.data[i][i] for i in range(self.rows)]

```
___
Результати:
```Python
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[0, 5, 0]
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[[0, 0], [15, 20], [0, 0]]
True
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[0, 0, 0, 0, 5, 0, 0, 0, 0]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 5, 9]

```
___
Висновки:
У ході цієї лабораторної роботи ми успішно вивчили основні операції з матрицями у мові програмування Python, використовуючи класи і методи. Кожне завдання надало можливість поглибити знання про ініціалізацію матриці, додавання елементів, обчислення сум рядків, транспонування, множення матриць, перевірку на симетричність, поворот на 90 градусів та згладжування. Ці операції є ключовими для розв'язання різних завдань у сферах обробки даних, математичних обчислень та алгоритміки. Розуміння цих концепцій дозволить ефективніше працювати з матрицями у майбутніх проектах, що вимагають аналізу та обробки структурованих даних.