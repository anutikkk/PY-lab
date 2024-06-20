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
