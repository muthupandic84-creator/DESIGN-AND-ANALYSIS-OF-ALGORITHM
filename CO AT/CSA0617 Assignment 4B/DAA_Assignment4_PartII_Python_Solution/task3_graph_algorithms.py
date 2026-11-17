# TASK 3: Dijkstra, Bellman-Ford, Floyd-Warshall, Warshall
import heapq
INF=float("inf")
def dijkstra(g,s):
    d={v:INF for v in g}; p={v:None for v in g}; d[s]=0
    pq=[(0,s)]; order=[]
    while pq:
        dist,u=heapq.heappop(pq)
        if dist!=d[u]: continue
        order.append(u)
        for v,w in g[u]:
            if w<0: raise ValueError("Dijkstra requires non-negative edge weights.")
            if dist+w<d[v]:
                d[v]=dist+w;p[v]=u;heapq.heappush(pq,(d[v],v))
    return d,p,order
def bellman_ford(vertices,edges,s):
    d={v:INF for v in vertices};p={v:None for v in vertices};d[s]=0
    for _ in range(len(vertices)-1):
        changed=False
        for u,v,w in edges:
            if d[u]!=INF and d[u]+w<d[v]:
                d[v]=d[u]+w;p[v]=u;changed=True
        if not changed: break
    cycle=any(d[u]!=INF and d[u]+w<d[v] for u,v,w in edges)
    return d,p,cycle
def path(p,t):
    out=[]
    while t is not None: out.append(t);t=p[t]
    return list(reversed(out))
def floyd(vertices,edges):
    n=len(vertices); ix={v:i for i,v in enumerate(vertices)}
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for u,v,w in edges: d[ix[u]][ix[v]]=min(d[ix[u]][ix[v]],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
def warshall(vertices,edges):
    n=len(vertices);ix={v:i for i,v in enumerate(vertices)}
    r=[[False]*n for _ in range(n)]
    for i in range(n):r[i][i]=True
    for u,v,w in edges:r[ix[u]][ix[v]]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return r
if __name__=="__main__":
    V=list("ABCDEFGH")
    E=[("A","B",4),("A","C",2),("B","C",1),("B","D",5),("C","D",8),("C","E",10),("D","E",2),("D","F",6),("E","F",3),("E","G",5),("F","G",1),("G","H",2),("F","H",7)]
    G={v:[] for v in V}
    for u,v,w in E:G[u].append((v,w))
    d,p,o=dijkstra(G,"A")
    print("DIJKSTRA distances:",d,"predecessors:",p,"finalised:",o)
    for v in V:print("A to",v,":",path(p,v))
    neg=E+[("C","B",-4)]
    print("\\nNEGATIVE EDGE: Dijkstra is no longer guaranteed valid; Bellman-Ford is used.")
    bd,bp,cycle=bellman_ford(V,neg,"A")
    print("Bellman-Ford distances:",bd,"predecessors:",bp,"reachable negative cycle:",cycle)
    cyc=neg+[("D","C",-10)]
    _,_,has_cycle=bellman_ford(V,cyc,"A")
    print("Reachable negative cycle detected:",has_cycle)
    print("\\nFloyd-Warshall distance matrix:")
    for row in floyd(V,E):print(row)
    print("\\nWarshall reachability matrix:")
    for row in warshall(V,E):print([int(x) for x in row])
