def fibonacci_last_digit_sum(m, n):
    result = 0

    previous = 0
    current = 1

    for i in range(n + 1):
        if i >= m:
            result += previous

        previous, current = current, (previous + current) % 10

    return result % 10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_last_digit_sum(m, n))
