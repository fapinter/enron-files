import heapq


def dijkstra(grafo, inicio):
    """
    Calcula o menor caminho a partir do vértice 'inicio' até todos os outros vértices usando Dijkstra.
    Retorna dois dicionários: distâncias mínimas e predecessores.
    """
    dist = {v: float('inf') for v in grafo}
    anterior = {v: None for v in grafo}
    dist[inicio] = 0
    heap = [(0, inicio)]

    while heap:
        atual_dist, atual_vertice = heapq.heappop(heap)

        if atual_dist > dist[atual_vertice]:
            continue

        for vizinho, peso in grafo.get(atual_vertice, []):
            nova_dist = atual_dist + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                anterior[vizinho] = atual_vertice
                heapq.heappush(heap, (nova_dist, vizinho))

    return dist, anterior

def reconstruir_caminho(anterior, fim):
    """
    Reconstrói o caminho mais curto até o vértice 'fim' usando os predecessores.
    """
    caminho = []
    while fim:
        caminho.append(fim)
        fim = anterior[fim]
    return list(reversed(caminho))

def calcular_diametro(grafo):
    """
    Calcula o diâmetro do grafo: o maior caminho mínimo entre qualquer par de vértices.
    Retorna o valor do diâmetro e o caminho correspondente.
    """
    diametro = 0
    maior_caminho = []

    for origem in grafo:
        distancias, anteriores = dijkstra(grafo, origem)

        for destino in grafo:
            if origem != destino and distancias[destino] != float('inf'):
                if distancias[destino] > diametro:
                    diametro = distancias[destino]
                    maior_caminho = reconstruir_caminho(anteriores, destino)

    return diametro, maior_caminho