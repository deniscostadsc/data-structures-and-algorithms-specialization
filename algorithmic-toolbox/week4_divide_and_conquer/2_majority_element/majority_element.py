# Uses python3
import sys


def get_majority_element(a, left, right):
    count = {}
    for number in a:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    for i, number in enumerate(a):
        if count[number] > int(len(a) / 2):
            return i

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
