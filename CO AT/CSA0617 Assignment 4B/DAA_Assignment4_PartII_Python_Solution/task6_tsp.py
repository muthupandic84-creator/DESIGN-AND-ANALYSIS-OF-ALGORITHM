# TASK 6: Travelling Salesperson using Held-Karp Dynamic Programming
from itertools import permutations
from time import perf_counter
def held_karp(cost):
    n=len(cost); full=(1<<n)-1
    # State (mask,last): minimum cost from hub 0, visiting mask, ending at last.
    dp={(1,0):0};parent={}
    for mask in range(1<<n):
        if not(mask&1):continue
        for last in range(n):
            key=(mask,last)
            if key not in dp:continue
            for nxt in range(1,n):
                if mask&(1<<nxt):continue
                nm=mask|(1<<nxt);nk=(nm,nxt);val=dp[key]+cost[last][nxt]
                if val<dp.get(nk,float("inf")):dp[nk]=val;parent[nk]=last
    best=float("inf");lastbest=None
    for last in range(1,n):
        val=dp.get((full,last),float("inf"))+cost[last][0]
        if val<best:best=val;lastbest=last
    route=[lastbest];mask=full;last=lastbest
    while last!=0:
        prev=parent[(mask,last)];mask^=1<<last;last=prev
        if last!=0:route.append(last)
    route=[0]+route[::-1]+[0]
    return best,route,len(dp)
def exhaustive(cost):
    n=len(cost);best=float("inf");br=None
    for p in permutations(range(1,n)):
        r=(0,)+p+(0,);v=sum(cost[r[i]][r[i+1]] for i in range(n))
        if v<best:best=v;br=r
    return best,br
if __name__=="__main__":
    names=["Hub","A","B","C","D","E","F"]
    cost=[[0,10,15,20,12,18,9],[10,0,9,10,8,15,11],[15,9,0,8,7,14,12],[20,10,8,0,6,9,13],[12,8,7,6,0,10,5],[18,15,14,9,10,0,8],[9,11,12,13,5,8,0]]
    best,route,states=held_karp(cost)
    print("Minimum cost:",best);print("Route:"," -> ".join(names[i] for i in route));print("DP states stored:",states)
    small=[row[:5] for row in cost[:5]]
    dpr,dproute,_=held_karp(small);exr,exroute=exhaustive(small)
    print("\\nValidation (hub + 4 locations): DP",dpr,"exhaustive",exr,"match:",dpr==exr)
    print("\\nScaling observations:")
    for k in range(4,9):
        sub=[row[:k+1] for row in cost[:k+1]]
        st=perf_counter();val,r,s=held_karp(sub);elapsed=perf_counter()-st
        print(f"{k} locations: states={s}, time={elapsed:.6f}s, cost={val}")
    print("\\n200 locations: exact DP is impractical because subset states grow exponentially. Investigate heuristic/metaheuristic or approximation approaches; trade-off is speed for loss of guaranteed optimality.")
