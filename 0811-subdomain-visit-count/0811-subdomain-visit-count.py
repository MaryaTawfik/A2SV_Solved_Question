from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_dict=defaultdict(int)
        for i in cpdomains:
            count , domain= i.split()
            count=int(count)
            fragment= domain.split(".")
            for j in range (len(fragment)):
                dom_dict[".".join(fragment[j:])]+=count
                
        return [f"{count} {domain}" for domain , count in dom_dict.items()]

        