class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # 取出清單的長度
        n = len(nums)

        # 第一次迴圈取第一個值
        for i in range(n - 1):
            # 在每次迴圈中, 再次迴圈後面的值
            for j in range(i+1, n):
                # 將值一一加總, 確認是否為目標值
                if nums[i] + nums[j] == target:
                    # 是目標值, 則返回索引
                    return [i, j]
        
        # no solution found
        return []