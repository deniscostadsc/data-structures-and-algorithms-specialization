def pisano_period(m):
    previous, current = 0, 1

    for i in range(m ** 2):
        previous, current = current, (previous + current) % m

        if (previous == 0 and current == 1):
            return i + 1

    return 1


def get_fibonacci_mod(n, m):
    pisano_period_length = pisano_period(m)

    previous, current = 0, 1

    n = n % pisano_period_length

    if n <= 1:
        return n

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_mod(n, m))
