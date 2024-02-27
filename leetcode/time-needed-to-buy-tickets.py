class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque([i , tickets[i]] for i in range(n))
        count = 0  

        while queue:
            for i in range(len(queue)):
                idx , val = queue.popleft()
                val -= 1
                if val >= 1:
                    queue.append((idx , val))
                count += 1
                if idx == k and val == 0:
                    return count