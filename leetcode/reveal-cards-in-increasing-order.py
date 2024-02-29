class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque()
        result = []
        queue.append(deck[0])
        
        for card in deck[1:]:
            
            last_card = queue.pop()
            queue.appendleft(last_card)
            
            queue.appendleft(card)
            
        while queue:
            result.append(queue.popleft())
        
        return result

