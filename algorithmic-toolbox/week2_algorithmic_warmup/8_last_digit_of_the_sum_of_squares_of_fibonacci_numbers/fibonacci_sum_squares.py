def fibonacci_sum_squares_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    result = 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
        result += (current ** 2) % 10

    return result % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_last_digit(n))
