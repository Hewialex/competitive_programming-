class Solution:
    def simplifyPath(self, path: str) -> str:
        #.. implies go a directory before, or pop.
        #. implies continue or do nothing
        #"" implies it was a trailing /, which means we have to do nothing
        # anything other is a directory, so we append it
        stack=[]
        path=path.split("/")
        for i in path:
            if(i=="" or i=="."):
                continue
            elif(i==".."):
                if(len(stack)>0):
                    stack.pop()
                else:
                    continue
            else:
                stack.append("/"+i)
        if(len(stack)==0):
            return "/"
        return "".join(stack)
