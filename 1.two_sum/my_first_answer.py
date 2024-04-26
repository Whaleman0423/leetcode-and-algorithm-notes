class Solution():

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        # 對清單中做迴圈
        for i in range(len(nums)):
            # 用 目標值 - 迴圈的值, 取出差
            difference = target - nums[i]
            nums[i] = None

            if difference in nums[i+1:]:
                # 如果差存在於後面的值, 則回傳
                return [i, nums.index(difference)]
            