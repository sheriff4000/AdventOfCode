import os
import pandas as pd
import numpy as np

with open('real_input.txt') as f:
    data = f.read().strip().split('\n')
    
# print(data)

# Assign numbers to nodes
nodes = {}
counter = 0
for line in data:
    base, children = line.split(':')
    if base not in nodes:
        nodes[base] = counter
        counter += 1
    for child in children.strip().split(' '):
        if child not in nodes:
            nodes[child] = counter
            counter += 1

print(len(nodes))
# Create graph as numpy array
graph = np.zeros((len(nodes), len(nodes)))
for line in data:
    base, children = line.split(':')
    for child in children.strip().split(' '):
        graph[nodes[base], nodes[child]] = 1
        graph[nodes[child], nodes[base]] = 1
        
# print(graph)

def num_edges_out_of_graph(graph, subgraph):
    num_edges  = 0.
    for node in subgraph:
        for idx, connection in enumerate(graph[node]):
            if connection == 1 and idx not in subgraph:
                num_edges += 1
    return num_edges

def connected_nodes(graph, subgraph):
    connected_nodes = set()
    for node in subgraph:
        for idx, connection in enumerate(graph[node]):
            if connection == 1 and idx not in subgraph:
                connected_nodes.add(idx)
    return connected_nodes

# print(num_edges_out_of_graph(graph, list(range(1))))

def depth_first_subgraph_search(graph, visited=list(), curr_subgraph=set([0]), search_criteria=lambda x: False):
    if search_criteria(curr_subgraph):
        return curr_subgraph
    visited.append(curr_subgraph)
    out = None

    for node in connected_nodes(graph, curr_subgraph):
        if set.union(curr_subgraph, [node]) not in visited:
            val = depth_first_subgraph_search(graph, visited, set.union(curr_subgraph, [node]), search_criteria)
            if val is not None:
                out = val
    
    return out

def depth_first_subgraph_search_iterative(graph, search_criteria=lambda x: False):
    visited = []
    stack = [set([0])]
    while stack:
        curr_subgraph = stack.pop(0)
        if search_criteria(curr_subgraph):
            return curr_subgraph
        visited.append(curr_subgraph)
        for node in connected_nodes(graph, curr_subgraph):
            if set.union(curr_subgraph, [node]) not in visited:
                stack.append(set.union(curr_subgraph, [node]))
    return None

def criteria(subgraph):
    return num_edges_out_of_graph(graph, subgraph) == 3.0

subgraph = depth_first_subgraph_search_iterative(graph, search_criteria=criteria) or set()

final = len(subgraph) * (len(nodes)-len(subgraph))
print(final)

# print(num_edges_out_of_graph(graph, set([12, 8, 0, 13, 1, 2])))
# print(connected_nodes(graph, set([0])))