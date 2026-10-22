class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        maxx=0
        curr=0
        left=0
        right=len(tokens)-1
        while left<=right:
            if power>=tokens[left]:
                power-=tokens[left]
                left+=1
                curr+=1
                maxx=max(maxx,curr)
            elif curr>0 and left<right:
                power+=tokens[right]
                right-=1
                curr-=1
            else: break
        return maxx
        