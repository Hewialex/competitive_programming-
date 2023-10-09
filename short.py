class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            d[char] = d.get(char,0) + 1

        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = ''
        for pair in sorted_d:
            # key = pair[0]
            # value = pair[1]
            ans += (pair[0] * pair[1])

        return ans

#
