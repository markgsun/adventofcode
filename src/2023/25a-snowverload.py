#!/usr/bin/env python
"""25a-snowverload.py: Advent of Code Day 25: Snowverload"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import networkx as nx


def get_graph(raw):
    graph = {}
    for row in raw:
        k = row.split(': ')[0]
        nxt = set(row.split(': ')[1].split())
        if k in graph.keys():
            node = graph[k].union(nxt)
        else:
            node = nxt
        graph[k] = node
        for n in nxt:
            if n in graph.keys():
                node2 = graph[n].union({k})
            else:
                node2 = {k}
            graph[n] = node2

    return graph


def min_cut(graph):
    g = nx.from_dict_of_lists(input_graph)
    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)
    return len(a)*len(b)


input_list = u.import_data('25')
input_graph = get_graph(input_list)
res = min_cut(input_graph)
print(res)
