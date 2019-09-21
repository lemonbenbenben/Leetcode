class Solution:
    def sortedSquares(self,A):
        a=[]
        for m in A:
            if m>=0:
                a.append(m)
            else:
                n=m*(-1)
                a.append(n)
        i=0
        j=len(a)-1
        out=[]
        while i<=j:
            if a[i]<=a[j]:
                out.append(a[j])
                j-=1
            else:
                out.append(a[i])
                i+=1
        return [n**2 for n in out[::-1]] 
