"""
input_data = [["1", "11,1", "10,3", "5,7", "9,6"],["2", "8,11", "5,10", "9,12"],
                ["3", "6,5", "13,5"],["4", "13,1"],["5", "1,7", "11,9", "9,5", "7,2", "6,7", "2,10"],
                ["6", "3,5", "5,7"],["7", "5,2", "9,11"],["8", "12,5", "2,11", "13,6"],
                ["9", "1,6", "11,8", "5,5", "2,12", "7,11"],["10", "1,3"],
                ["11", "1,1", "9,8", "5,9"],["12", "8,5"],["13", "8,6", "4,1", "3,5"]]
"""
f = open("PathInput.txt", "r")
input_data = []
for line in f:
    string_entries = line.split()
    row = [n for n in string_entries]
    input_data.append(row)


#create table 
n = int(input_data[-1][0])
path_graph = [None] * (n + 1)
for i in range(len(input_data)):
    vertex = int(input_data[i][0])
    path_graph[vertex] = []
    for j in range(1, len(input_data[i])):
        edge = input_data[i][j].split(",")
        edge[0], edge[1] = int(edge[0]), int(edge[1])
        path_graph[vertex].append(edge)



#initialize list of solved vertices with source (vertex 1) and its values (distance 0)
solved_vertices = [1]
solved_distances = [1000000] * (n + 1)
solved_distances[1] = 0

#create function for finding next vertex
def next_vertex(vertices, distances, graph):
    minimum = 1000000
    next = 0
    for i in range(len(vertices)):
        vertex = vertices[i]
        for j in range(len(graph[vertex])):
            if graph[vertex][j][0] not in vertices:
                if distances[vertex] + graph[vertex][j][1] < minimum:
                    minimum = distances[vertex] + graph[vertex][j][1]
                    next = graph[vertex][j][0]
    vertices.append(next)
    distances[next] = minimum

for i in range(n - 1):
    next_vertex(solved_vertices, solved_distances, path_graph)

print("\n\n")
print(solved_vertices)
print("\n\n")
print(solved_distances[7])
print(solved_distances[37])
print(solved_distances[59])
print(solved_distances[82])
print(solved_distances[99])
print(solved_distances[115])
print(solved_distances[133])
print(solved_distances[165])
print(solved_distances[188])
print(solved_distances[197])

