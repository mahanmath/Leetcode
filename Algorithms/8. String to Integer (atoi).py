class Solution:
    def myAtoi(self, string: str) -> int:
        if(not string.split()):
            return 0
        INT_MIN = -2147483648
        INT_MAX = -INT_MIN - 1
        
        foundDig = False
        foundSign = False
        endSpace = False
        
        token = string[0]
        if(not (token.isdigit() or token == '+' or token == '-' or token == ' ')):
                return 0
        startSpace = (token == ' ')
        
        sign = 1
        num = []
        for i in range(len(string)):
            #print(1)
            token = string[i]
            if(token != ' '):
                #print(2)
                endSpace = True
            if(foundSign and not token.isdigit()):
                #print(3)
                break
            if(foundDig and not token.isdigit()):
                #print(4)
                break
            
            if(not foundSign and not foundDig and not token.isdigit() and not token == '-' and not token == '+' and startSpace and endSpace):
                #print(5)
                return 0
            
            if(foundSign and (token =='-' or token == '+')):
                #print(6)
                return 0
            if(not foundDig and not foundSign and (token == '-' or token == '+')):
                #print(7)
                if(token == '-'):
                    #print(8)
                    sign = -1
                foundSign = True

            if(token.isdigit()):
                #print(9)
                foundDig = True
                num.append(token)
        
        
        

        if(not len(num)):
            return 0
        
        while(num and num[0] == '0'):
            num.pop(0)

        numDig = len(num)
        
        if(numDig > 10):
            if(sign == -1):
                return INT_MIN
            else:
                return INT_MAX
        
        
        output = sum([int(num[::-1][i]) * (10 ** i) for i in range(numDig)])
        
        if(sign == 1):
            return min([output, INT_MAX])
        else:
            return max([-1 * output, INT_MIN])
        
                