
##1085. Sum of Digits in the Minimum Number
class Solution:
    def sumOfDigits(self, A):
        m=min(A)
        quotient=1
        r=[]
        while quotient>0:
#             quotient,remainder=divmod(m,10)
            quotient=m//10
            remainder=m%10
            r.append(remainder)
            m=quotient
        if sum(r)%2==0:
            return 1
        else:
            return 0
