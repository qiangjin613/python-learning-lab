#https://leetcode.cn/problems/hqCnmP/

from typing import List

class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        m = len(supplies) // 2
        while len(supplies) > m:
            idx = 1
            for i in range(1, len(supplies)):
                if supplies[i - 1] + supplies[i] < supplies[idx - 1] + supplies[idx]:
                    idx = i
            supplies[idx - 1] += supplies[idx]
            supplies.pop(idx)
        return supplies