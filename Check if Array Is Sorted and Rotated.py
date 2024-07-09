class Solution:
    def check(self, nums):
        n = len(nums)
        count_rotations = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_rotations += 1
        
        return count_rotations <= 1


nums = [3, 4, 5, 1, 2]
solution = Solution()
print(solution.check(nums))  
