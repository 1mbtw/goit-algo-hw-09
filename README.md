# Coin Change Homework

I made two algorithms to give change with coins [50, 25, 10, 5, 2, 1]. The task is to
return a dict with how many coins we use.

## Greedy algorithm
Greedy takes the biggest coin first, then repeat with the rest amount. It is very fast
because it goes one time through the coin list.

- Time: O(k), where k is count of coin types.
- For big amounts it is still fast, because k is always 6.
- Works good for this coin set, but for other sets it can be not optimal.

## Dynamic programming
DP builds the best result for every sum from 0 to the target. It always finds minimum
number of coins, but it does much more work.

- Time: O(amount * k)
- Memory: O(amount)
- For big amounts it becomes slower and uses more memory.

## Big amounts: why one is faster
Greedy almost does not care about amount size. It only depends on how many coin types we
have. DP depends on amount, so when amount grows, the work also grows. That is why DP is
much slower for large numbers.

## Conclusion
If the coin system is standard (like real cash), greedy is enough and much faster. If the
coin system is unusual and you must guarantee minimum number of coins, DP is safer, but
slower.