import fileReading as fr
import adjacency_list as al
import isEulerian as ie 

graph = al.graph()

fr.readFiles("./enron-2016", graph)

#graph.print_adjacency_list()
print(graph.order)
print(graph.size)


fr.send_to_txt(graph)

#print("É Euleriano?", ie.is_eulerian_directed(graph))
#TO-DO LIST:
#supostamente a 3 esta correta, em caso de bug acahdo me avisar ps:simini