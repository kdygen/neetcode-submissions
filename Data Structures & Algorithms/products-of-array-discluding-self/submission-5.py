class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        rightside = []
        leftside = []
        left = 1
        right = 1
        for n in range(len(nums)):
            leftside.append(left)
            left *= nums[n]

        for n in range(len(nums)-1, -1, -1):
            rightside.append(right)
            right *= nums[n]
        rightside.reverse()

        for n in range(len(nums)):
            result.append(leftside[n] * rightside[n])

        return result



            # [1, 1, 2, 8]
