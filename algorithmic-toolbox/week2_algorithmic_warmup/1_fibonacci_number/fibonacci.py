memo = {
        0: 0,
        1: 1,
}


def calc_fib(n):
    if (n <= 1):
        return n

    try:
        return memo[n]
    except KeyError:
        memo[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return memo[n]


n = int(input())
print(calc_fib(n))
