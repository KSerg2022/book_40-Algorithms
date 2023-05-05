"""BFS — поиск в ширину"""

from queue import Queue

graph = {'Amin': {'Wasim', 'Nick', 'Mike'},
         'Wasim': {'Imran', 'Amin'},
         'Imran': {'Wasim', 'Faras'},
         'Faras': {'Imran'},
         'Mike': {'Amin'},
         'Nick': {'Amin'}
         }


def bfs(graph, start):
    visited = []
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.append(node)
            naighbours = graph[node]
            for naighbour in naighbours:
                queue.put(naighbour)
    return visited


print(bfs(graph, 'Amin'))


