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

    def add_edge(self, id_1, id_2, weight):
        if id_1 == id_2:
            print("loops not supported")
            return
        
        if weight < 0:
            print("Negative weights not supported")
            return

        #Verifying if the nodes are added to the graph already
        if id_1 not in self.adjacency_list.keys():
            self.add_node(id_1)
        if id_2 not in self.adjacency_list.keys():
            self.add_node(id_2)

        #Updating the weight of the existing edge
        for i, (id_, _) in enumerate(self.adjacency_list[id_1]):
            if id_2 == id_:
                self.adjacency_list[id_1][i] = (id_, weight)
                return
        
        self.adjacency_list[id_1].append((id_2, weight))
        self.size +=1
        
    
    def remove_edge(self, id_1, id_2):
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
        #Only verifies in the direction id_1 -> id_2
        temp_list = [k for k in self.adjacency_list[id_1] if  k[0] == id_2]
        if len(temp_list) > 0:
            return True
        else: return False

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
                
        

def test1():
    print('\nTEST 1')
    graph1 = graph()
    graph1.add_node('A')
    graph1.add_node('B')
    
    graph1.add_edge('A', 'B', 3)
    graph1.add_edge('A', 'C', 1)
    graph1.add_edge('B', 'C', 7)
    graph1.add_edge('C', 'D', 2)
    graph1.add_edge('D', 'A', 4)
    print(f'Order: {graph1.order}')
    print(f'Size: {graph1.size}')
    graph1.print_adjacency_list()
    print('Graph 1 has an edge A and B?', graph1.has_edge('A', 'B'))
    print('Graph 1 has an edge B and A?', graph1.has_edge('B', 'A'))
    print('A node InDegree: ', graph1.in_degree('A'))
    print('A node OutDegree: ', graph1.out_degree('A'))
    print('A node Degree: ', graph1.degree('A'))

    print('\nREMOVING NODE A FROM THE GRAPH')
    graph1.remove_node('A')
    print(f'Order: {graph1.order}')
    print(f'Size: {graph1.size}')
    graph1.print_adjacency_list()


def test2():
    print('\nTEST 2')
    graph2 = graph()
    graph2.add_edge('X', 'Y', 5)
    graph2.add_edge('X', 'Z', 2)
    graph2.add_edge('Y', 'Z', 4)
    graph2.add_edge('Y', 'W', 3)
    graph2.add_edge('Z', 'W', 6)
    graph2.add_edge('W', 'X', 1)

    print(f'Order: {graph2.order}')
    print(f'Size: {graph2.size}')
    graph2.print_adjacency_list()

    print('Weight of edge Y -> Z: ', graph2.get_weight('Y', 'Z'))
    print('Weight of edge W -> X: ', graph2.get_weight('W', 'X'))



def test3():
    print('\nTEST 3')
    graph3 = graph()
    graph3.add_edge('P', 'R', 8)
    graph3.add_edge('P', 'Q', 2)
    graph3.add_edge('Q', 'S', 5)
    graph3.add_edge('R', 'S', 3)
    graph3.add_edge('R', 'T', 1)
    graph3.add_edge('S', 'T', 7)
    graph3.add_edge('T', 'P', 6)
    graph3.add_edge('T', 'Q', 4)
    graph3.add_node('P')

    print(f'Order: {graph3.order}')
    print(f'Size: {graph3.size}')
    graph3.print_adjacency_list()

    print('\nRemoving edge T')
    graph3.remove_node('T')

    print(f'Order: {graph3.order}')
    print(f'Size: {graph3.size}')
    graph3.print_adjacency_list()

    print('Graph 3 has edge T -> Q ?', {graph3.has_edge('T', 'Q')})

test1()
test2()
test3()


