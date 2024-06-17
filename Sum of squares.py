# leecode link: https://leetcode.com/problems/sum-of-square-numbers/description/

def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    max = int(c**0.5)
    min =0
    
    while True :
        if min**2 + max**2 == c:
            return True 
        elif min**2 + max**2 <c:
            min+=1
        elif min**2 + max**2 > c:
            max-=1
            min = 0
        elif max<int(c**0.5)/2 or min<int(c**0.5)/2:
            return False
        
        
        







print(judgeSquareSum(5))
