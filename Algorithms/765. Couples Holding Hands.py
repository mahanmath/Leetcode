class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        def MyNeigh(x):
            return x - 2*(x%2) + 1
        L = len(row)
        
        row_enum = {}
        
        for loc, person in enumerate(row):
            row_enum[person] = loc

        visited = [False for _ in range(L)]
        
        ans = 0
        
        for i in range(L):
            if(not visited[row[i]]):
                visited[row[i]] = True
                cycle_len = 1
                next_ver = row_enum[MyNeigh(row[i])]
                couple_turn = False
                while(not visited[row[next_ver]]):
                    visited[row[next_ver]] = True
                    cycle_len += 1
                    if(couple_turn):
                        next_ver = row_enum[MyNeigh(row[next_ver])]
                    else:
                        next_ver = MyNeigh(next_ver)
                    couple_turn ^= 1
                ans += (cycle_len//2) - 1
        
        
        return ans