class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(len(edges)+1)] #[range(n+1)]
        rank = [0] * (n + 1)
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[parent[x]]) #path compression
            return parent[x]
        def union(u , v):
            pu , pv = find(u) , find(v)
            if pu == pv:
                return False
            if rank[pu] > rank[pv]:
                parent[pu] = pv
            elif rank[pv] > rank[pu]:
                parent[pv] = pu
            else:
                parent[pv] = pu
                rank[pv] += 1
            return True
        for u , v in edges:
            if not union(u,v):
                return [u,v]
        
        