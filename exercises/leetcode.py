class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in nums:
            new_nums = nums[nums.index(num) + 1:]
            for number in new_nums:
                if num + number == target:
                    result = [num, number]
                    return (result)

if __name__ == '__main__':
    nums, target = input().split(',')


    solution = Solution(input())
    print(solution)