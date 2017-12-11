class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # get the pivot idx
        get_pivot_idx = self.get_pivot(nums)


        start, end = 0, len(nums) - 1

        # if the partition is True, check for the target with the given pivotal index

        if get_pivot_idx[1] == True:
            # after getting idx, now do bin search!
            if get_pivot_idx[0] + 1 <= len(nums) - 1:
                if target > nums[get_pivot_idx[0] + 1] and target > nums[len(nums) - 1]:
                    start, end = 0, get_pivot_idx[0]
                else:
                    start, end = get_pivot_idx[0] + 1, len(nums) - 1

        while end >= start:

            mid = start + (end - start) // 2

            if nums[mid] < target:
                # continue right
                start = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                # continue left
                end = mid - 1
        return -1

    '''
    
    The get_pivot returns the idx and True if the array is rotated by x places 
    
    '''
    def get_pivot(self, nums):
        # first get the pivotal point
        idx = 0
        while idx + 1 <= len(nums) - 1:
            if nums[idx] > nums[idx + 1]:
                return [idx, True]
            else:
                idx += 1
        return [0, False]