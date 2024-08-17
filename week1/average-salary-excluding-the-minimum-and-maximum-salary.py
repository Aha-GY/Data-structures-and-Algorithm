class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary.sort()
        aver_salary = sum(salary[1:-1])/(len(salary)-2)
        return aver_salary
        