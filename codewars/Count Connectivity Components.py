import re


def components(grid):

    split = list(filter(lambda x: len(x) != 0, grid.split('\n')))
    length = len(re.findall(r'\+', split[0])) - 1
    links_dict = {i: [] for i in range(length * (length - 1))}

    def dfs(v, visited):
        visited[v] = 1
        number = 1
        for v in links_dict.get(v):
            if visited[v] != 1:
                number += dfs(v, visited)
        return number

    horizontal, vertical = [], []
    for i in range(1, len(split) - 1):
        if i % 2 == 1:
            horizontal.append(split[i])
        else:
            vertical.append(split[i])
    horizontal_link, vertical_link = lambda x: [x, x + 1], lambda x: [x, x + 3]
    links = [horizontal_link(3 * i + j)
             for i in range(len(horizontal))
             for j in range(length)
             if horizontal[i][3 + 3 * j] == ' '] + \
            [vertical_link(j)
             for i in range(len(vertical))
             for j in range(length)
             if vertical[i][3 * j + 1] == ' ']
    for link in links:
        links_dict[link[0]].append(link[1])
        links_dict[link[1]].append(link[0])

    visited = [0 for _ in range(length * (length - 1))]
    answer = {}
    while visited.__contains__(0):
        a = visited.index(0)
        i = dfs(a, visited)
        answer[i] = answer.get(i, 0) + 1
    return sorted(list(answer.items()), key=lambda x: x[0], reverse=True)


'''
+--+--+--+--+--+--+--+--+--+--+
|1 |2 |  |3 |  |4 |5 |     |6 |
+--+--+  +--+  +--+--+--+--+--+
|7 |8 |  |  |  |           |9 |
+--+--+--+  +--+--+  +  +  +--+
|  |10|11|  |12|           |13|
+  +--+--+--+--+--+--+--+--+--+
|     |     |  |14|15|16|  |17|
+  +--+  +--+  +--+--+--+  +--+
|  |18|     |     |        |  |
+--+--+--+  +--+--+--+  +--+  +
|19|20|21|  |     |22|  |     |
+--+--+--+  +  +--+--+--+--+--+
|     |     |     |     |     |
+  +  +--+--+--+--+--+--+--+  +
|  |        |           |  |  |
+  +--+--+--+--+  +  +--+  +--+
|     |23|  |24|  |        |25|
+  +  +--+  +--+  +  +--+  +--+
|26|  |27|     |     |     |28|
+--+--+--+--+--+--+--+--+--+--+
'''

grid = '''
+--+--+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |     |  |
+--+--+  +--+  +--+--+--+--+--+
|  |  |  |  |  |           |  |
+--+--+--+  +--+--+  +  +  +--+
|  |  |  |  |  |           |  |
+  +--+--+--+--+--+--+--+--+--+
|     |     |  |  |  |  |  |  |
+  +--+  +--+  +--+--+--+  +--+
|  |  |     |     |        |  |
+--+--+--+  +--+--+--+  +--+  +
|  |  |  |  |     |  |  |     |
+--+--+--+  +  +--+--+--+--+--+
|     |     |     |     |     |
+  +  +--+--+--+--+--+--+--+  +
|  |        |           |  |  |
+  +--+--+--+--+  +  +--+  +--+
|     |  |  |  |  |        |  |
+  +  +--+  +--+  +  +--+  +--+
|  |  |  |     |     |     |  |
+--+--+--+--+--+--+--+--+--+--+
'''

print(components(grid))
