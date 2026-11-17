# TASK 4: Two-line assembly scheduling with route reconstruction
def solve(a1,a2,t1,t2,e1,e2,x1,x2,verbose=True):
    n=len(a1); f1=[0]*n;f2=[0]*n;prev1=[None]*n;prev2=[None]*n
    f1[0]=e1+a1[0];f2[0]=e2+a2[0]
    for j in range(1,n):
        stay1=f1[j-1]+a1[j]; transfer1=f2[j-1]+t2[j-1]+a1[j]
        stay2=f2[j-1]+a2[j]; transfer2=f1[j-1]+t1[j-1]+a2[j]
        f1[j]=min(stay1,transfer1);prev1[j]=1 if stay1<=transfer1 else 2
        f2[j]=min(stay2,transfer2);prev2[j]=2 if stay2<=transfer2 else 1
        if verbose: print(f"Station {j+1}: L1 stay={stay1}, transfer={transfer1}, choose={prev1[j]}; L2 stay={stay2}, transfer={transfer2}, choose={prev2[j]}")
    end1=f1[-1]+x1;end2=f2[-1]+x2
    line=1 if end1<=end2 else 2
    total=min(end1,end2);route=[0]*n
    route[-1]=line
    for j in range(n-1,0,-1):
        route[j-1]=prev1[j] if route[j]==1 else prev2[j]
    print("Route:", " -> ".join(f"Line {ln} Station {i+1}" for i,ln in enumerate(route)))
    print("Transfer points:",[i+1 for i in range(1,n) if route[i]!=route[i-1]])
    print("Minimum production time:",total)
    return total,route
if __name__=="__main__":
    a1=[7,9,3,4,8,4];a2=[8,5,6,4,5,7]
    t1=[2,3,1,3,4];t2=[2,1,2,2,1]
    print("BASE CASE");solve(a1,a2,t1,t2,2,4,3,2)
    print("\\nTRANSFER DISRUPTION: increase transfer L1->L2 at station 3")
    t1b=t1.copy();t1b[2]=20;solve(a1,a2,t1b,t2,2,4,3,2)
    print("\\nMACHINE DISRUPTION: Line 1 station 3 becomes slower")
    a1b=a1.copy();a1b[2]=30;solve(a1b,a2,t1,t2,2,4,3,2)
    print("\\nThree-line extension: state becomes f[line][station]; at each station compare staying on each line and transfers from every other line. Store predecessor line for each state to reconstruct route.")
