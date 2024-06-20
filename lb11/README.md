Лабораторна робота №11: Advanced Working with Arrays of Numbers in Python
___
Мета роботи:
Ця лабораторна робота дозволяє ознайомитися з різноманітними алгоритмами та структурами даних у Python, що є ключовими для розробників усіх рівнів. Виконання цих завдань допоможе поглибити розуміння алгоритмів та підготувати підґрунтя для подальшого вивчення складніших концепцій програмування.
___
Опис завдання:
Task 1: Sum of Squares
Create a function sum_of_squares that accepts an array of numbers and returns the sum of the squares of each number.
Example of function usage:
print(sum_of_squares([1, 2, 3])) # Output: 14 

Task 2: Filter and Sum
Create a function filter_and_sum that accepts an array of numbers and returns the sum of all the elements that are greater or equal than the average of the array.
Example of function usage:
print(filter_and_sum([1, 2, 3, 4, 10])) # Output: 14 

Task 3: Sort by Frequency
Create a function sort_by_frequency that sorts an array of numbers based on the frequency of each element from highest to lowest. If two numbers have the same frequency, the smaller number should come first.
Example of function usage:
print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6])) # Output: [4, 4, 4, 6, 6, 6, 2] 

Task 4: Find Missing Number
Create a function find_missing_number that finds the missing number in an array containing all integers from 1 to n except one. Assume the array has no duplicates.
Example of function usage:
print(find_missing_number([1, 2, 4, 5])) # Output: 3 

Task 5: Longest Consecutive Sequence
Create a function longest_consecutive that finds the length of the longest consecutive elements sequence in an unsorted array.
Example of function usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2])) # Output: 4 
Task 6: Rotate Array

Create a function rotate_array that rotates the array to the right by k steps, where k is non-negative.
Example of function usage:
print(rotate_array([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3] 
Task 7: Array of Products
Create a function array_of_products that calculates an array of products of all numbers except the one at the current index without using division.
Example of function usage:
print(array_of_products([1, 2, 3, 4])) # Output: [24, 12, 8, 6]
 
Task 8: Maximum Subarray Sum
Create a function max_subarray_sum that finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
Example of function usage:
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6 

Task 9: Spiral Order Matrix
Create a function spiral_order that returns all elements of a 2D matrix in spiral order.
Example of function usage:
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5] 

Task 10: K Closest Points to Origin
Create a function k_closest_points that finds the k closest points to the origin (0, 0) in a 2D plane, given an array of coordinate points.
Example of function usage:
print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2)) # Output: [(1, 1), (1, 2)] :
___
Виконання роботи:
```Python
from collections import Counter


def task1(a):
    return sum(x ** 2 for x in a)

def task2(ar):
    avg= sum(ar) / len(ar)
    return sum(x for x in ar if x >= avg)

def task3(arr):
    counts = Counter(arr)
    sorteda = sorted(arr, key=lambda x: (-counts[x], x))
    return sorteda

def task4(arrr):
    n = len(arrr) +1
    totals = n * (n+1) // 2
    sumarr = sum(arrr)
    return totals - sumarr

def task5(number):
    nums = set(number)
    ls = 0
    for num in nums:
        if num - 1 not in nums:
            curent = num
            current = 1
            while curent + 1 in nums:
                curent += 1
                current += 1
            ls = max(ls,current)
    return ls

def task6(arrrr, s):
    s %= len(arrrr)
    arrrr[:] = arrrr[-s:] + arrrr[:-s]
    return arrrr

def task7(numbs):
    x = len(numbs)
    leftp = [1] * x
    rightp = [1] * x
    result = [1] * x
    for i in range(1, x):
        leftp[i] = leftp[i - 1] * numbs[i - 1]
    for i in range(x - 2, -1, -1):
        rightp[i] = rightp[i + 1] * numbs[i + 1]
    for i in range(x):
        result[i] = leftp[i] * rightp[i]
    return result

def task8(numbes):
    maxsu = float('-inf')
    currents= 0
    for num in numbes:
        currents = max(num, currents + num)
        maxsu = max(maxsu, currents)
    return maxsu

def task9(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def task10(point, n):
    dis = [(x ** 2 + y ** 2, (x, y)) for x, y in point]

    dis.sort()

    return [point for _, point in dis[:n]]

```
___
Результати:
```Python
30
9
[4, 4, 5, 5, 3, 6]
3
4
[4, 5, 1, 2, 3]
[24, 12, 8, 6]
6
[1, 2, 3, 6, 9, 8, 7, 4, 5]
[(1, -1), (1, 2)]

```
___
Висновки:
Ця лабораторна робота була спрямована на вивчення основних алгоритмів та структур даних в мові програмування Python. Кожне завдання мало свої унікальні цілі і дозволило краще розібратися з різними аспектами програмування.
___