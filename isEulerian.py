def is_eulerian_directed(G):
    # Get all "active" nodes, meaning nodes with at least one incoming or outgoing edge
    active_nodes = [node for node in G.adjacency_list if G.out_degree(node) > 0 or G.in_degree(node) > 0]

    # Check if all active nodes have equal in-degree and out-degree
    # (required condition for an Eulerian circuit in directed graphs)
    unbalanced_nodes = [
        node for node in active_nodes 
        if G.in_degree(node) != G.out_degree(node)
    ]

    # Helper function to check if the graph is strongly connected
    # A directed graph is strongly connected if there is a path between every pair of nodes in both directions
    def is_strongly_connected():
        if not active_nodes:
            # If there are no active nodes, consider the graph trivially connected
            return True

        from collections import deque

        # Breadth-first search(bfs) to explore reachable nodes
        # reverse=True means we traverse the graph as if edges were reversed(basicamente ele percorre o grafo de traz pra frente sem ter q criar um grafo novo)
        def bfs(start_node, reverse=False): 
            visited = set()
            queue = deque([start_node])

            #FIFO Queue Management(First In First Out)
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    neighbors = []
                    if reverse:
                        # In reversed graph, we look for incoming edges
                        for node, edges in G.adjacency_list.items():
                            for neighbor, _ in edges:
                                if neighbor == current:
                                    neighbors.append(node)
                    else:
                        neighbors = [n for n, _ in G.adjacency_list[current]]
                    for n in neighbors:
                        if n not in visited:
                            queue.append(n)
            return visited

        # Choose any active node to start the traversal
        start = active_nodes[0]
        # Check which nodes are reachable from the start node
        forward_reach = bfs(start)
        # Check which nodes can reach the start node (i.e., graph transposed)
        reverse_reach = bfs(start, reverse=True)
        # Graph is strongly connected only if both forward and reverse reachabilities
        # cover all active nodes
        return set(active_nodes) == forward_reach == reverse_reach

    # Check if the graph is strongly connected
    connected = is_strongly_connected()
    # A directed graph has an Eulerian cycle if:
    # 1. It is strongly connected
    # 2. All nodes have equal in-degree and out-degree
    is_eulerian = connected and not unbalanced_nodes
    if not is_eulerian:
        # If the graph is not Eulerian, explain why and show the issues
        print("Conditions for an Eulerian cycle NOT satisfied:")
        if unbalanced_nodes:
            print(f"  - Number of nodes with unbalanced degree (in ≠ out): {len(unbalanced_nodes)}")
        if not connected:
            print("  - The graph is not strongly connected.")
    else:
        # All conditions are satisfied
        print("The graph is Eulerian: strongly connected with all degrees balanced.")

    return is_eulerian


# function like is_strongly_connected and bfs are defined inside is_eulerian_directed to avoid polluting the global namespace and to encapsulate the logic.