def get_change(m):
    coins = [10, 5, 1]
    coin_count = 0
    i = 0

    while m > 0:
        coin_count += m // coins[i]
        m %= coins[i]
        i += 1

    return coin_count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
