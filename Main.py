from Generate_graph import *
from Algo import *
from time import process_time


# vertex = [100, 200]
# edges = [2, 3, 4, 5, 99]
# num = 5
vertex = [1000, 2000, 3000, 4000, 5000, 10000]
edges = [5, 100, 999]
num = 5
time_matrix = {}
time_list = {}
for i in vertex:
    for i2 in edges:
        # generate_graph(i, i2, num)
        matrix_time = 0
        adj_list_time = 0
        for i3 in range(num):
            matrix = load_graph_matrix(i, i2, i3)
            adj_list = load_graph_list(i, i2, i3)

            start = process_time()
            dijkstra_matrix_array(matrix)
            stop = process_time()
            matrix_time += stop - start

            start = process_time()
            dijkstra_list_heap(adj_list)
            stop = process_time()
            adj_list_time += stop - start
        print(f"Matrix time: {matrix_time}")
        print(f"Adj time: {adj_list_time}")
        time_matrix[f"{i}_{i2}"] = matrix_time
        time_list[f"{i}_{i2}"] = adj_list_time
with open(f"matrix_time.json", "w") as file:
    json.dump(time_matrix, file)
with open(f"list_time.json", "w") as file:
    json.dump(time_list, file)
