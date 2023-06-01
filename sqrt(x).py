class Solution:
    def mySqrt(self, x: int) -> int:
        #using the repeated subtracted method
        # article https://www.cuemath.com/algebra/squares-and-square-roots/
        count = 0
        i = 1 #first odd number
        while x >= 0:
            x -= i
            if x >= 0:
                count += 1
            else:
                pass
            i += 2
        return count