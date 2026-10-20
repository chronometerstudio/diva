#!/usr/bin/env python3
# граф (файл "n m" + рёбра) -> CNF 3-раскраски; опционально закрепление жадной клики (как в diva_par)
import sys
sys.argv.append('') if len(sys.argv)<3 else None
t=open(sys.argv[1]).read().split(); n,m=int(t[0]),int(t[1]); E=[(int(t[2+2*i]),int(t[3+2*i])) for i in range(m)]
adj=[set() for _ in range(n)]
for a,b in E: adj[a].add(b); adj[b].add(a)
units=[]
if sys.argv[2]=='fix':
    s=max(range(n),key=lambda v:len(adj[v])); cl=[s]; cand=set(adj[s])
    while len(cl)<3 and cand:
        b=max(cand,key=lambda v:len(adj[v])); cl.append(b); cand&=adj[b]
    units=[3*v+i+1 for i,v in enumerate(cl)]
x=lambda v,k:3*v+k+1; out=[[u] for u in units]
for v in range(n):
    out.append([x(v,k) for k in range(3)]); out+=[[-x(v,i),-x(v,j)] for i in range(3) for j in range(i+1,3)]
for a,b in E: out+=[[-x(a,k),-x(b,k)] for k in range(3)]
print(f"p cnf {3*n} {len(out)}"); print("\n".join(" ".join(map(str,c))+" 0" for c in out))
