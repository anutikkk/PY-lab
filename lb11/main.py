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
