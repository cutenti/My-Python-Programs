class Graph:
    def __init__(self):
        """
        Инициализация пустого графа, в виде словаря.
        Ключ - вершина, значение - список смежных вершин.
        """
        self.conection_list = {}

    def add_vertex(self, vertex):
        """Добавление новой вершины в граф."""
        if vertex not in self.conection_list:
            self.conection_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавление ребра между 2 вершинами"""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.conection_list[vertex1].append(vertex2)
        self.conection_list[vertex2].append(vertex1)

    def dfs(self, start_vertex=None):
        """
        Обход графа в глубину.
        start_vertex: вершина, с которой начинается обход
        return: список посещенных вершин в порядке обхода DFS
        """
        if not self.conection_list:
            return []

        if start_vertex is None:  # Начинаем с первой добавленной вершины
            start_vertex = next(iter(self.conection_list))

        if start_vertex not in self.conection_list:
            raise ValueError(f"Вершины {start_vertex} не существует")

        visited = set()
        stack = [start_vertex]
        result = []

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                neighbors = []
                for neighbor in self.conection_list[vertex]:
                    if neighbor not in visited:
                        neighbors.append(neighbor)
                stack.extend(reversed(neighbors))  # Чтобы идти слева направо

        return result

    def __iter__(self):
        """Возвращает итератор, который проходит по вершинам в порядке DFS"""
        return iter(self.dfs())
