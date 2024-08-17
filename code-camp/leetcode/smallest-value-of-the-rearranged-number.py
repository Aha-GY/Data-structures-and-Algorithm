class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(str(num)) == 1 or num == 0:
            return num
        elif num > 0:
            small_num = list(str(num))
            small_num.sort()
            if small_num[0] == "0":
                for i in range(1, len(small_num)):
                    if small_num[i] != "0":
                        small_num[0], small_num[i] = small_num[i], small_num[0]
                        break
            return int("".join(small_num))
        else:
            small_num = list(str(num))
            small_num.pop(0)
            small_num.sort()
            small_num = small_num[::-1]
            return int("".join(small_num)) *-1