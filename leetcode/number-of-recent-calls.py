class RecentCounter:

    def __init__(self):
        self.val = []
        

    def ping(self, t: int) -> int:
        self.val.append(t)
        while self.val[0] < t - 3000:
            self.val.pop(0)
        return  len(self.val) 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)