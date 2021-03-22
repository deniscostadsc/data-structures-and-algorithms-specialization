import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        middle = int(left + ((right - left) / 2))

        print(left, middle, right)
        if x == a[middle]:
            return middle
        elif x < a[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def linear_search(a, x):
    for i, number in enumerate(a):
        if number == x:
            return i

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]

    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
