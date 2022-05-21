class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        sums, sums_temp = [0], []
        n_coins, visited = 0, [False]*(amount + 1)
        visited[0] = True
        while sums:
            n_coins += 1
            for value in sums:
                for coin in coins:
                    newval = value + coin
                    if newval == amount:
                        return n_coins
                    elif newval > amount:
                        continue
                    else:
                        if not visited[newval]:
                            visited[newval] = True
                            sums_temp.append(newval)
            sums, sums_temp = sums_temp, []
            
        return -1