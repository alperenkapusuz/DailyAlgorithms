class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = 1
        if num <= 1:
            return False
        
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                ans += i + num//i
        
        return num == ans
#q10
        
        