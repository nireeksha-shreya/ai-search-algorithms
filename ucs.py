import heapq

def ucs(graph, start):
    visited = set()
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node not in visited:
            print(node, "Cost:", cost)
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 1)],
    'D': [],
    'E': []
}

ucs(graph, 'A')
