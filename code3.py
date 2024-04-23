def dfs(g, a):
    t = set()
    def f2(z):
        t.add(z)
        print(z)
        for b in g[z]:
            if b not in t:
                f2(b)
    f2(a)
g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs(g, 'A')
