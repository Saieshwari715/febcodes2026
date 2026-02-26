class Solution:
    def addDigits(self, num: int) -> int:


        if num>=10:
            return 1+(num-1)%9
        else:
            return num
        '''while num>=10:#for double digit
            temp=0
            while num>0:
                temp+=num%10
                num=num//10
            num=temp
        return num'''


        