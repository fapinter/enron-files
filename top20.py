def top20_outdegree(G):
    outDegrees = {}
    #Adds all the nodes of the graph into a dictionary
    for key, value in G.adjacency_list.items():
        outDegrees[key] = len(value)

    #Sorts the dictionary based on the OutDegree value on Decreasing order
    sorted_outdegrees = sorted(outDegrees.items(), key=lambda x: x[1], reverse=True)

    #Gets the first 20 nodes
    top_20 = sorted_outdegrees[:20]

    for node, degree in top_20:
        print(f'Node {node} : Out Degree {degree}')

def top20_indegree(G):
    inDegrees = {}
    #Addds all the nodes of the graph into a dictionary
    for key in G.adjacency_list.keys():
        inDegrees[key] = G.in_degree(key)

    #Sorts the dictionary based on the inDegree value on Decreasing order
    sorted_indegrees = sorted(inDegrees.items(), key=lambda x: x[1], reverse=True)

    #Gets the first 20 nodes
    top_20 = sorted_indegrees[:20]

    for node, degree in top_20:
        print(f'Node {node} : In Degree {degree}')