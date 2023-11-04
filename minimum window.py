class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT,hm={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        
        have,need=0,len(countT)
        res=[-1,-1]
        reslen=float('infinity')
        l=0
        for r in range(len(s)):
            c=s[r]
            hm[c]=1+hm.get(c,0)

            if c in countT and hm[c]==countT[c]:
                have+=1

            while have==need:
                if r-l+1 <reslen:
                    res=[l,r]
                    reslen=r-l+1

                hm[s[l]]-=1
                if s[l] in countT and hm[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen != float('infinity') else ""
