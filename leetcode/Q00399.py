class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    

        def build_graph(equations, values):
            graph = defaultdict(dict)
            for (A, B), value in zip(equations, values):
                graph[A][B] = value
                graph[B][A] = 1 / value
            return graph
        
        # def dfs(graph, start, end, visited):
        #     if start not in graph or end not in graph:
        #         return -1.0
        #     if start == end:
        #         return 1.0
        #     visited.add(start)
        #     for node, value in graph[start].items():
        #         if node in visited:
        #             continue
        #         temp_result = dfs(graph, node, end, visited)
        #         if temp_result != -1.0:
        #             return value * temp_result
        #     return -1.0
        
        def bfs(graph, start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            queue = deque([(start, 1.0)])
            visited = set()

            while queue:
                node, product = queue.popleft()
                if node == end:
                    return product
                visited.add(node)
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            return -1.0

        graph = build_graph(equations, values)
        results = []
        for (C, D) in queries:
            # results.append(dfs(graph=graph, start=C, end=D, visited=set()))
            results.append(bfs(graph=graph, start=C, end=D))
        return results
