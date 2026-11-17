# TASK 2: Fractional Greedy vs 0/1 Dynamic Programming
def fractional_knapsack(items, capacity):
    # items: (id, weight, value)
    ranked=sorted(items,key=lambda x:x[2]/x[1],reverse=True)
    remaining=capacity; value=0; chosen=[]
    print("\\nFRACTIONAL GREEDY DECISIONS")
    for ident,w,v in ranked:
        if remaining<=0: break
        fraction=min(1,remaining/w)
        remaining-=fraction*w; value+=fraction*v
        chosen.append((ident,fraction,w*fraction,v*fraction))
        print(f"{ident}: ratio={v/w:.2f}, take {fraction:.2f}")
    print("Selected:",chosen,"Total value:",round(value,2))
    return value,chosen

def zero_one_knapsack(items,capacity):
    n=len(items); dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i,(_,w,v) in enumerate(items,1):
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if w<=c: dp[i][c]=max(dp[i][c],dp[i-1][c-w]+v)
    c=capacity; chosen=[]
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]:
            ident,w,v=items[i-1]; chosen.append((ident,w,v)); c-=w
    chosen.reverse()
    print("\\n0/1 DP SELECTED:",chosen,"Total value:",dp[n][capacity])
    print("DP table:")
    for row in dp: print(row)
    return dp[n][capacity],chosen

if __name__=="__main__":
    normal=[("A",10,60),("B",20,100),("C",30,120)]
    print("Normal dataset, capacity=50")
    fractional_knapsack(normal,50); zero_one_knapsack(normal,50)
    print("\\nGreedy counterexample, capacity=50")
    counter=[("A",10,60),("B",20,100),("C",30,120)]
    print("Greedy ratio order takes A then B (value 160), but optimal 0/1 choice is B+C (value 220).")
    zero_one_knapsack(counter,50)
    print("\\nEngineering: fractional greedy sorts O(n log n), uses O(n) selection storage; 0/1 DP uses O(nW) time and O(nW) table memory. Fractional is optimal for divisible items; 0/1 DP is exact for integer capacity.")
