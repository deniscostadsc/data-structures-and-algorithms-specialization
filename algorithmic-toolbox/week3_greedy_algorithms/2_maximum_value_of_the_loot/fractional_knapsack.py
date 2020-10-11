import sys


def sort_items(values, weights):
    return sorted(
        zip(values, weights),
        key=lambda x: x[0] / x[1],
        reverse=True
    )


def get_optimal_value(capacity, values, weights):
    sorted_items = sort_items(values, weights)
    total_value = 0.0
    for value, weight in sorted_items:
        if not capacity:
            break

        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += (value * capacity) / weight
            capacity = 0

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, values, weights)
    print("{:.10f}".format(opt_value))
