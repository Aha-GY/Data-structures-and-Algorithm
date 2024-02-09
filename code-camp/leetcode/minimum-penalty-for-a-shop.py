class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        count_y = customers.count("Y")
        num_y , num_n = 0,0
        penalty =[]
        for custmer in customers:
            if custmer == "Y":
                penalty.append(count_y - num_y + num_n)
                num_y += 1
            else:
                penalty.append(num_n+ count_y-num_y)
                num_n += 1
        penalty.append(num_n)
        return penalty.index(min(penalty))