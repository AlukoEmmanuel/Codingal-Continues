def count_components(n, edges):
    # Create adjacency list representation of the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Since it's an undirected graph
    
    def dfs(vertex, visited):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor, visited)
    
    components = 0
    # Process vertices from 1 to n, removing them one by one
    for vertex in range(1, n + 1):
        # Remove vertex by clearing its connections
        for neighbor in graph[vertex]:
            graph[neighbor] = [x for x in graph[neighbor] if x != vertex]
        graph[vertex] = []
        
        # Count connected components in remaining graph
        visited = [False] * (n + 1)
        components = 0
        for i in range(1, n + 1):
            if i != vertex and not visited[i]:
                dfs(i, visited)
                components += 1
    
    return components

# Read input
def solve():
    # Read N and M
    n, m = map(int, input().split())
    
    # Read edges
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Get and print result
    result = count_components(n, edges)
    print(result)

# For the coding platform, you might need to use this format
if __name__ == "__main__":
    solve()