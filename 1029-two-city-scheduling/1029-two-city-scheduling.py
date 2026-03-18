class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost=0
        costb_a=[]
        for i in range (len(costs)):
            costb_a.append(costs[i][1] - costs[i][0])
            min_cost+=costs[i][0]
        costb_a.sort()
        for i in range(len(costs)//2):
            min_cost+=costb_a[i]
        return min_cost
        