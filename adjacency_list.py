from collections import defaultdict
import copy
import heapq  # Add import for priority queue

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

    def add_edge(self, id_1, id_2):

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
        else:        
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
        print("*** Adjacency List ***\n")

        for key in self.adjacency_list.keys():
            print(f'{key}: ', end="")

            for id, value in self.adjacency_list[key]:
                print(f'({id}, {value})', end=" -> ")
                
            print("\n")
        print("*"*22)
        
    def vertices_within_distance(self, start_vertex, max_distance):
        """
        Retorna uma lista com todos os vértices que estão localizados até uma distância D
        de um vértice N, onde D é a soma dos pesos ao longo do caminho mais curto entre dois vértices.
        
        Esta implementação utiliza o algoritmo de Dijkstra com fila de prioridade para eficiência,
        tornando-a adequada para grafos com milhares de vértices e arestas.
        
        Args:
            start_vertex: O vértice inicial (N)
            max_distance: Distância máxima permitida (D), inclusive
            
        Returns:
            Uma lista com os IDs de todos os vértices que estão a uma distância menor ou igual a max_distance
            do vértice inicial (incluindo o próprio vértice inicial)
        
        Complexidade de Tempo: O((V + E) log V) onde V é o número de vértices e E é o número de arestas
        Complexidade de Espaço: O(V)
        """
        # Verifica se o vértice inicial existe no grafo
        if start_vertex not in self.adjacency_list:
            return []
            
        # Inicializa as distâncias com infinito para todos os vértices, exceto o inicial
        # O dicionário 'distances' armazena a menor distância conhecida até cada vértice
        distances = {vertex: float('infinity') for vertex in self.adjacency_list}
        distances[start_vertex] = 0
        
        # Conjunto para controlar vértices já visitados e evitar processamento redundante
        # Um vértice é considerado 'visitado' quando já encontramos o caminho mais curto até ele
        visited = set()
        
        # Fila de prioridade para o algoritmo de Dijkstra
        # Formato: (distância, vértice) - ordenada pela distância (menor primeiro)
        # Usamos heapq para implementar a fila de prioridade de forma eficiente
        priority_queue = [(0, start_vertex)]
        
        # Processa os vértices em ordem crescente de distância
        while priority_queue:
            # Extrai o vértice com menor distância atual da fila
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Pula se já processamos este vértice (já encontramos o caminho mais curto)
            if current_vertex in visited:
                continue
                
            # Marca como visitado, pois agora temos certeza do caminho mais curto até ele
            visited.add(current_vertex)
            
            # Se a distância atual excede a distância máxima, não é necessário explorar
            # os vizinhos deste vértice, pois todos estarão além da distância máxima
            if current_distance > max_distance:
                continue
                
            # Explora todos os vizinhos do vértice atual
            for neighbor, weight in self.adjacency_list[current_vertex]:
                # Pula vizinhos já visitados, pois já temos o caminho mais curto para eles
                if neighbor in visited:
                    continue
                    
                # Calcula a nova distância para este vizinho
                # É a soma da distância até o vértice atual mais o peso da aresta
                distance = current_distance + weight
                
                # Se encontramos um caminho mais curto para o vizinho, atualizamos
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Adiciona o vizinho à fila de prioridade com sua nova distância
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Coleta todos os vértices dentro da distância máxima permitida
        # Um vértice está dentro da distância se sua menor distância conhecida 
        # é menor ou igual à distância máxima especificada
        result = [vertex for vertex, distance in distances.items() 
                 if distance <= max_distance]
        
        return result