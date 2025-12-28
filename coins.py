import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount) -> dict[int, int]:
    result = {}
    for coin in COINS:
        if amount <= 0:
            break
        count, amount = divmod(amount, coin)
        if count:
            result[coin] = count
    return result


def find_min_coins(amount) -> dict[int, int]:
    if amount <= 0:
        return {}

    max_val = amount + 1
    dp = [0] + [max_val] * amount
    prev = [0] * (amount + 1)

    for s in range(1, amount + 1):
        for coin in COINS:
            if coin <= s:
                cand = dp[s - coin] + 1
                if cand < dp[s]:
                    dp[s] = cand
                    prev[s] = coin

    result = {}
    while amount > 0:
        coin = prev[amount]
        if coin == 0:
            break
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


def _bench(amounts, iterations=10) -> None:
    header = f"{'Amount':<8} | {'Greedy':<12} | {'DP':<12} | {'DP/Greedy':<10}"
    print(header)
    print("-" * len(header))

    for amount in amounts:
        g = timeit.timeit(lambda: find_coins_greedy(amount), number=iterations)
        d = timeit.timeit(lambda: find_min_coins(amount), number=iterations)
        ratio = d / (g + 1e-10)
        print(f"{amount:<8} | {g:<12.6f} | {d:<12.6f} | {ratio:<10.1f}")


def main() -> None:
    amounts = [120, 700, 1500, 3000, 7000, 12000]
    _bench(amounts)


if __name__ == "__main__":
    main()