# Uses python3
import sys
import random


def partition3(a, left, right):
    x = a[left]
    j = left
    k = right

    for i in range(right + 1):
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
        if a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1

    return j


def partition2(a, left, right):
    x = a[left]
    j = left

    for i in range(left + 1, right + 1):
        if a[i] <= x:
            j += 1
            print("---", i, j)
            a[i], a[j] = a[j], a[i]
            print(a)

    print("+++", left, j)
    a[left], a[j] = a[j], a[left]
    print(a)

    return j


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]
    m = partition3(a, left, right)
    randomized_quick_sort(a, left, m - 1)
    randomized_quick_sort(a, m + 1, right)


if __name__ == '__main__':
    ll = [2, 1, 2, 2, 2, 2, 5, 6, 2]
    print(ll)
    partition3(ll, 0, len(ll) - 1)
    print(ll)
    print("-------------------------")
    ll = [2, 1, 2, 2, 2, 2, 5, 6, 2]
    partition2(ll, 0, len(ll) - 1)
    print("---------")
    print(ll)
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)

    # for x in a:
    #   # print(x, end=' ')
