class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_l = nums[0]
        l = [pre_l]
        pre_r = nums[len(nums)-1]
        r = [pre_r]
        for i in range(1,len(nums)):
            pre_l *= nums[i]
            l.append(pre_l)
           
        for i in range(len(nums)-2,-1,-1):
            pre_r *= nums[i]
            r.append(pre_r)
        r.reverse()
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(r[i+1])
            elif i == len(nums)-1:
                ans.append(l[i-1])
            else:
                ans.append( r[i+1] * l[i-1])

           
            
        return ans



            