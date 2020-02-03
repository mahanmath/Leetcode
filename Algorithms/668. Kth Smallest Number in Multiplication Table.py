class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        [m, n] = sorted([m, n])
        
        def Counter(x):
            count = 0
            for j in range(1, m + 1):
                count += min([x//j, n])
            return count
        
        left = 1
        right = m*n
        
        while(left < right):
            mid = (left + right)//2
            if (Counter(mid) < k):
                left = mid + 1
            else:
                right = mid
        return left
