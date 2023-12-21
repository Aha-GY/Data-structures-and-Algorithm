class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        for row in image:
            left = 0
            right =len(row)-1
            while left <= right:
                if row[left] == row[right] :
                    row[left] = (row[left] +1)%2
                    if left != right:
                        row[right] = (row[right] +1)%2
                left +=1
                right -=1
        return image
                    