from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in nums_set:
                return [nums_set[complement], i]
            nums_set[num] = i


if __name__ == '__main__':
    s = Solution()

    for arr, target, exp, name in [
        ([2, 7, 11, 15], 9, [0, 1], "case 1"),
        ([3, 2, 4],      6, [1, 2], "case 2"),
        ([3, 3],         6, [0, 1], "case 3"),
    ]:
        res = s.twoSum(arr, target)
        if res != exp:
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
