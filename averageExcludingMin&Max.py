class Solution(object):
    def average(self, salary):
        salary.sort()

        counter = 0
        sum = 0.00

        for i in range(len(salary)):
            if i == 0 or i == len(salary) - 1:
                pass
            else:
                sum += salary[i]
                counter += 1
        
        return sum / counter