from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom comparison function
        def custom_compare(num1, num2):
            return (num1 + num2) > (num2 + num1) - (num2 + num1) > (num1 + num2)

        # Sort the strings using the custom comparison function
        nums.sort(key=cmp_to_key(custom_compare), reverse=True)

        # Join the sorted strings to create the largest number
        largest_num = ''.join(nums)

        # Handle the case where the result is '0' (all zeros in input)
        if largest_num[0] == '0':
            return '0'

        return largest_num
