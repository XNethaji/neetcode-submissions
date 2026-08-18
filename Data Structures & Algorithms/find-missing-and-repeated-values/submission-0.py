from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        hashmap = defaultdict(int)
        total = n*n
        output = [0] * 2
        for z in range(1,total+1):
            hashmap[z] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] in hashmap:
                    hashmap[grid[i][j]] -= 1
        for keys, values in hashmap.items():
            if values == 1:
                output[1] = keys
            elif values == -1:
                output[0] = keys
        return output





        