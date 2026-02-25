from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        target=Counter(p)
        r=len(p)

        for i in range(len(s)):
            window=Counter(s[i:r])
            if target == window:
                ans.append(i)
            r+=1
        return ans





















        # result = []
        # p_count = Counter(p)
        # window_count = Counter()

        # for i in range(len(s)):
       
        #     window_count[s[i]] += 1

        
        #     if i >= len(p):
        #         if window_count[s[i - len(p)]] == 1:
        #             del window_count[s[i - len(p)]]
        #         else:
        #             window_count[s[i - len(p)]] -= 1

     
        #     if window_count == p_count:
        #         result.append(i - len(p) + 1)

        # return result
        