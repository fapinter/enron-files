from collections import defaultdict
import copy

class graph:
    def __init__(self):
        self.size = 0
        self.order = 0
        #Dict of key value
        #(Node, list of tuple(node, weight))
        self.adjacency_list = defaultdict(list)
    
    def add_node(self, id):
        if id not in self.adjacency_list.keys():
            self.adjacency_list[id]
            self.order +=1
        else:
            print(f"node {id} already in the list")

    def add_edge(self, id_1, id_2):
        if id_1 == id_2:
            print("loops not supported")
            return

        #Verifying if the nodes are added to the graph already
        if id_1 not in self.adjacency_list.keys():
            self.add_node(id_1)
        if id_2 not in self.adjacency_list.keys():
            self.add_node(id_2)

        #Updating the weight of the existing edge
        if self.has_edge(id_1, id_2):

            for i, (id_, weight) in enumerate(self.adjacency_list[id_1]):
                if id_2 == id_:
                    self.adjacency_list[id_1][i] = (id_, weight+1)
                    return
        
        self.adjacency_list[id_1].append((id_2, 1))
        self.size +=1
        
    
    def remove_edge(self, id_1, id_2):
        if id_1 in self.adjacency_list.keys() and id_2 in self.adjacency_list.keys():
            copy_list = copy.deepcopy(self.adjacency_list[id_1])
            self.adjacency_list[id_1] = [k for k in self.adjacency_list[id_1] if k[0] != id_2]
            if copy_list != self.adjacency_list[id_1]:
                self.size -= 1
        

    def remove_node(self, id):
        if id in self.adjacency_list.keys():

            #Removing edges connected to the node
            for key in self.adjacency_list.keys():
                self.remove_edge(key, id)
            
            count = len(self.adjacency_list[id])
            self.adjacency_list.pop(id)
            self.size -= count
            self.order -= 1
        else:
            print(f'Node {id} is not in the list')
    
    
    def has_edge(self, id_1, id_2):
        if id_1 in self.adjacency_list.keys() and id_2 in self.adjacency_list.keys():
            #Only verifies in the direction id_1 -> id_2
            temp_list = [k for k in self.adjacency_list[id_1] if  k[0] == id_2]
            if len(temp_list) > 0:
                return True
            return False

    def in_degree(self, id):
        count = 0
        for key in self.adjacency_list.keys():
            temp_list = [k for k in self.adjacency_list[key] if k[0] == id]
            count += len(temp_list)
        return count
    
    def out_degree(self, id):
        count = len(self.adjacency_list[id])
        return count
    
    def degree(self, id):
        count = 0
        count += self.in_degree(id)
        count += self.out_degree(id)
        return count

    def get_weight(self, id_1, id_2):
        if self.has_edge(id_1, id_2):
            temp_list = [t[1] for t in self.adjacency_list[id_1] if t[0] == id_2]
            return temp_list[0]
    
    def print_adjacency_list(self):
        print("*** Adjacency List ***")

        for key in self.adjacency_list.keys():
            print(f'{key}: ', end="")

            for id, value in self.adjacency_list[key]:
                print(f'({id}, {value})', end=" -> ")
                
            print()
        print("*"*22)


#Coisas para alterar:
#1. adicionar as funcoes a mais do tde-3
#---criar vertice no read files
#---alterar add_edge, tirar peso de parametro, caso a aresta exista aumentar em +1