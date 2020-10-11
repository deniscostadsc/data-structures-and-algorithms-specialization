def compute_min_refills(distance, tank, stops):
    refill = 0
    last_gas_station = 0
    stops.append(distance)
    fuel_limit = tank

    for stop in stops:
        fuel_limit -= stop
        if fuel_limit < stop:
            fuel_limit = last_gas_station + tank - (stop - last_gas_station)
            refill += 1

        if not fuel_limit:
            return -1

        last_gas_station = stop

    return refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
