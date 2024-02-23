class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        next = [len(arr)] * len(arr)
        prev = [-1] * len(arr)
        stack = []
        summ = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                var = stack.pop()
                next[var] = i
            stack.append(i)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                var = stack.pop()
                prev[var] = i
            stack.append(i)
        for i in range(len(arr)):
            next[i] -= i
            prev[i] = i - prev[i]
            summ += arr[i]*next[i]*prev[i]
        return summ % mod