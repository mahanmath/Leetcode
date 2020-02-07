class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        length = len(arr)
        ans = 0
        
        for i in range(1, 2 ** length):
            
            subset_code = bin(i)[2:]
            subset_code = '0' * (length - len(subset_code)) + subset_code
            MyHash = {}
            possible = True
            count = 0
            
            for bit in range(length):
                if(subset_code[bit] == '1'):
                    for char in arr[bit]:
                        count += 1
                        if(char in MyHash):
                            possible = False
                            break
                        else:
                            MyHash[char] = True
                
                if not possible:
                    break
                
            if possible:
                ans = max([ans, count])
                
        return ans
