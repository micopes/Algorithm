class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        stones = list(stones)

        cnt = 0
        for s in stones:
            if s in jewels:
                cnt += 1

        return cnt
