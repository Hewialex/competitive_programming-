class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)
        d = {num: i for i, num in enumerate(nums2)}
        for k , i in d.items():
            while stack and stack[-1] < nums2[i] :
                val = stack.pop()
                
                if val in nums1:
                    ans[nums1.index(val)] = nums2[i]
            stack.append(nums2[i])
        return ans