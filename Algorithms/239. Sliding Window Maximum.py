class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deck = collections.deque()
        out = []
        for indx, num in enumerate(nums):
            while deck and nums[deck[-1]] < num:
                deck.pop()
            deck += indx,
            if deck[0] == indx - k:
                deck.popleft()
            if indx >= k - 1:
                out += nums[deck[0]],
        return out