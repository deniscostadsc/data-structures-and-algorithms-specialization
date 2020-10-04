def fibonacci_last_digit_sum(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    result = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        result += current

    return result % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit_sum(n))
