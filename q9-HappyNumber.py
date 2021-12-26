class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while(1):
            val=0
            while(n):
                index=n%10
                val+=index*index
                n//=10
                
            if val==1:
                return 1
            elif val in s:
                return 0
            else:
                s.add(val)
            n=val
