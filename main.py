import fileReading as fr  # Importa módulo para leitura de arquivos
import adjacency_list as al  # Importa módulo de implementação da lista de adjacência
import isEulerian as ie  # Importa módulo para verificar se o grafo é euleriano
import top20 as tp
import dijkstra as dg  # Importa módulo para calcular o diâmetro do grafo
# Cria uma instância de grafo utilizando a estrutura de lista de adjacência
graph = al.graph()

# Carrega os dados do grafo a partir dos arquivos na pasta enron-2016
# Isso construirá o grafo com os emails da base de dados Enron
fr.readFiles("./enron-2016", graph)

# Imprime estatísticas básicas do grafo
#graph.print_adjacency_list()  # Comentado para não sobrecarregar a saída
print(f"Número de vértices: {graph.order}")  # Exibe a quantidade de vértices (ordem do grafo)
print(f"Número de arestas: {graph.size}")  # Exibe a quantidade de arestas (tamanho do grafo)

# Salva o grafo em um arquivo de texto para análise posterior
fr.send_to_txt(graph)

# Verificação da função vertices_within_distance com o grafo enron-2016
if graph.order > 0:  # Verifica se o grafo não está vazio
    # Seleciona um vértice existente no grafo para usar como ponto de partida
    exemplo_vertice = next(iter(graph.adjacency_list.keys()))
    
    print(f"\nTestando vertices_within_distance a partir do vértice: {exemplo_vertice}")
    
    # Testa a função com diferentes distâncias máximas para analisar o comportamento
    for distancia_maxima in [1, 2, 3, 5]:
        # Chama a função que encontra todos os vértices até a distância máxima especificada
        vertices_proximos = graph.vertices_within_distance(exemplo_vertice, distancia_maxima)
        
        # Exibe os resultados da busca
        print(f"\nVértices a uma distância máxima de {distancia_maxima} a partir de {exemplo_vertice}:")
        print(f"Total de vértices encontrados: {len(vertices_proximos)}")
        
        # Para não sobrecarregar a saída, mostra apenas os primeiros 5 vértices encontrados
        if vertices_proximos:
            print(f"Primeiros 5 vértices (de {len(vertices_proximos)}): {vertices_proximos[:5]}")

#print("É Euleriano?", ie.is_eulerian_directed(graph))  # Comentado, verificação se o grafo é euleriano
#TO-DO LIST:
#supostamente a 3 esta correta, em caso de bug acahdo me avisar ps:simini

tp.top20_outdegree(graph)

print("\nCalculando o diâmetro do grafo, aguarde...")   
diametro, caminho = dg.calcular_diametro(graph.adjacency_list)

print("\nDiâmetro do grafo:", diametro)
print("Caminho correspondente:")
for i, v in enumerate(caminho):
    print(f"{i+1}. {v}")