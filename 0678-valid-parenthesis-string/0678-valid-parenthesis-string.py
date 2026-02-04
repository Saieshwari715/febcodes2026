class Solution:
    def checkValidString(self, s: str) -> bool:
        minio=0
        maxio=0
        c=0
        for i in s:
            if(i=='('):
                minio+=1
                maxio+=1
            elif(i==')'):
                minio-=1
                maxio-=1
            elif(i=='*'):
                minio-=1
                maxio+=1
            if minio<0:
                minio=0
            if maxio<0:
                return False
        return minio==0


            
