class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 1
        last_number = nums[0]
        for read_index in range(len(nums)):
            if nums[read_index] > last_number:
                nums[write_index] =  nums[read_index]
                write_index += 1
                last_number = nums[read_index]
        return write_index