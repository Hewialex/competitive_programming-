class Solution:
    def largestOddNumber(self, num: str) -> str:
        # var = 0

        # for i in range(len(num)):
        #     for j in range(i,len(num)):
        #         if int(num[i:j+1])%2 != 0:
        #             var = max(var,int(num[i:j+1]))

        # return "" if var == 0 else str(var)

        # finding an odd number with max index
        # max_index = -1
        # for index in range(len(num)):
        #     if int(num[index])%2 != 0:
        #         max_index = index
        
        # return "" if max_index == -1 else str(num[0:max_index+1]) 



        # starting from the end and searching for an odd number
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 != 0:
                return num[:i+1]
        return "" 


                
        