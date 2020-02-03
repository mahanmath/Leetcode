class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        from math import ceil, log
        return (ceil(log(buckets, 1 + minutesToTest//minutesToDie)))