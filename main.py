import fileReading as fr
import adjacency_list as al

graph = al.graph()

fr.readFiles("enron-2016", graph)

graph.print_adjacency_list()
print(graph.order)
print(graph.size)


