class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs=[0]*k
        max_unfairness = float('inf')
        def backtrack(i):
            nonlocal childs,max_unfairness
            if i == len(cookies):
                max_unfairness = min(max_unfairness,max(childs))
                return
            
            for j in range(k):
                childs[j] += cookies[i]
                if max(childs) >= max_unfairness:
                    childs[j] -= cookies[i]
                    continue
                backtrack(i+1)
                childs[j] -= cookies[i]
        backtrack(0)
        return max_unfairness