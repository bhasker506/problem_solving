from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        minimum_candies = 0
        if not ratings:
            return minimum_candies
        candies = [1] * len(ratings)
        right_to_left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] :
                candies[i] = candies[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            current = 1
            if ratings[i] > ratings[i+1] :
                current = right_to_left[i+1]+1
            minimum_candies += max(current, candies[i])
            candies[i] = current
        
        for i, j in zip(candies, right_to_left):
            minimum_candies += max(i, j)
        
        return minimum_candies



if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,3,2,2,1]))