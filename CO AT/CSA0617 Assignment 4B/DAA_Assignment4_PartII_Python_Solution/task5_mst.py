# TASK 5: Kruskal, Prim, Boruvka MST
import heapq
class DSU:
    def __init__(self,n):self.p=list(range(n));self.rank=[0]*n
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a);b=self.find(b)
        if a==b:return False
        if self.rank[a]<self.rank[b]:a,b=b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:self.rank[a]+=1
        return True
def kruskal(n,edges):
    d=DSU(n);out=[];cost=0
    for u,v,w in sorted(edges,key=lambda e:e[2]):
        if d.union(u,v):out.append((u,v,w));cost+=w;print("Kruskal accepts",u,v,w)
    return out,cost
def prim(n,edges):
    g=[[] for _ in range(n)]
    for u,v,w in edges:g[u].append((w,u,v));g[v].append((w,v,u))
    seen={0};pq=g[0][:];heapq.heapify(pq);out=[];cost=0
    while pq and len(seen)<n:
        w,u,v=heapq.heappop(pq)
        if v in seen:continue
        seen.add(v);out.append((u,v,w));cost+=w;print("Prim accepts",u,v,w)
        for e in g[v]:
            if e[2] not in seen:heapq.heappush(pq,e)
    return out,cost
def boruvka(n,edges):
    d=DSU(n);out=[];cost=0;components=n
    while components>1:
        cheapest=[None]*n
        for u,v,w in edges:
            a=d.find(u);b=d.find(v)
            if a==b:continue
            if cheapest[a] is None or w<cheapest[a][2]:cheapest[a]=(u,v,w)
            if cheapest[b] is None or w<cheapest[b][2]:cheapest[b]=(u,v,w)
        added=False
        for e in cheapest:
            if e and d.union(e[0],e[1]):
                out.append(e);cost+=e[2];components-=1;added=True;print("Boruvka accepts",e)
        if not added:break
    return out,cost
if __name__=="__main__":
    n=6;edges=[(0,1,4),(0,2,3),(1,2,1),(1,3,2),(2,3,4),(2,4,5),(3,4,2),(3,5,7),(4,5,3),(1,5,8)]
    for name,fn in [("Kruskal",kruskal),("Prim",prim),("Boruvka",boruvka)]:
        print("\\n",name);tree,c=fn(n,edges);print("MST:",tree,"cost:",c)
    print("\\nEqual-weight stress test: change edges (0,1) and (0,2) to weight 1; multiple equal-cost MST edge sets may exist.")
