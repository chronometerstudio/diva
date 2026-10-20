#!/usr/bin/env python3
# fresh random graph G(n, m = c*n) with a seed of your choice -> the same text format as graphs/
# usage: python3 gengraph.py <n> <c> <seed> > my_graph.txt      e.g.  python3 gengraph.py 600 2.35 424242
import sys, random
n,c,seed=int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]); R=random.Random(seed); E=set()
while len(E)<int(c*n):
    a,b=R.randrange(n),R.randrange(n)
    if a!=b: E.add((min(a,b),max(a,b)))
E=sorted(E); print(n,len(E)); print("\n".join(f"{a} {b}" for a,b in E))
