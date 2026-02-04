class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''arr=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                arr[i]=max(arr[i],arr[i+1]+1)
        return sum(arr)'''
        n=len(ratings)
        i=1
        s=1
        while i<n:
            if ratings[i]==ratings[i-1]:
                s+=1
                i+=1
                continue
            peak=1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                s+=peak
                i+=1
            down=1
            while i<n and ratings[i]<ratings[i-1]:
                s+=down
                down+=1
                i+=1
            if down>peak:
                s+=down-peak
        return s


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        