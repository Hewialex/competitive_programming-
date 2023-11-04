class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        #return w2[:-1]
        #w1=w1[::-1]
        #w2=w2[::-1]
        
        def greedy(w1,w2,res):
            while w1 and w2:
                if w1>w2:
                    res+=w1[0]
                    w1=w1[1:]
                else:
                    res+=w2[0]
                    w2=w2[1:]
                #res+=cur
                #print(res)
            res+=w1
            res+=w2
            return res
        res1=greedy(w1,w2,'')
        return res1
                     
