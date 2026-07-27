class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 1
        last_number = nums[0]
        is_max_double = True
        for read_index in range(len(nums)):
            if read_index == 0:
                continue
            if nums[read_index] > last_number:
                nums[write_index] =  nums[read_index]
                last_number = nums[read_index]
                write_index += 1
                is_max_double = True
            elif is_max_double :
                nums[write_index] =  nums[read_index]
                write_index += 1
                is_max_double = False

        return write_index