#!/usr/bin/env python
"""23b-walk.py: Advent of Code Day 23: A long walk"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import sys
sys.setrecursionlimit(1000000)


def is_straight(grid, pos):
    nbs = [grid[pos[0]-1][pos[1]], grid[pos[0]+1][pos[1]],
           grid[pos[0]][pos[1]-1], grid[pos[0]][pos[1]+1]]
    if len([x for x in nbs if x == '#']) == 3:
        return False
    if (nbs[0], nbs[1]) == ('#', '#'):
        return True
    if (nbs[2], nbs[3]) == ('#', '#'):
        return True
    return False


def collapse_graph(graph):
    removes = []
    for k in graph.keys():
        if len(graph[k]) == 2:
            [node_a, node_b] = graph[k]

            (pos_a, dist_a, pos_b, dist_b) = (node_a[:-1], node_a[-1], node_b[:-1], node_b[-1])

            graph[pos_a].append(pos_b+tuple([dist_a+dist_b]))
            graph[pos_a].remove(k+tuple([dist_a]))
            graph[pos_b].append(pos_a+tuple([dist_a+dist_b]))
            graph[pos_b].remove(k+tuple([dist_b]))
            removes += [k]

    for k in removes:
        graph.pop(k)
    return graph


def create_graph(grid):
    graph = {}
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            pos = (x, y)
            if grid[x][y] == '#' or is_straight(grid, pos):
                continue
            nodes = []
            if grid[pos[0]][pos[1]+1] != '#':
                for y2 in range(y+1, len(grid[0])-1):
                    if not is_straight(grid, (x, y2)):
                        nodes += [(x, y2, y2-y)]
                        break
            if grid[pos[0]][pos[1]-1] != '#':
                for y2 in range(y-1, 0, -1):
                    if not is_straight(grid, (x, y2)):
                        nodes += [(x, y2, y-y2)]
                        break

            if grid[pos[0]+1][pos[1]] != '#':
                for x2 in range(x+1, len(grid)-1):
                    if not is_straight(grid, (x2, y)):
                        nodes += [(x2, y, x2-x)]
                        break
            if grid[pos[0]-1][pos[1]] != '#':
                for x2 in range(x-1, 0, -1):
                    if not is_straight(grid, (x2, y)):
                        nodes += [(x2, y, x-x2)]
                        break
            graph[pos] = nodes

    graph_out = collapse_graph(graph)
    return graph_out


def walk_dfs(pos, graph, dist, visited):
    if pos == end_pos:
        return dist

    res_best = None
    for neighbor in graph[pos]:
        if neighbor[:-1] in visited:
            continue
        visited += [neighbor[:-1]]
        delta = neighbor[-1]
        res_temp = walk_dfs(neighbor[:-1], graph, dist+delta, visited)
        if res_best is None or (res_temp is not None and res_temp > res_best):
            res_best = res_temp

        visited.remove(neighbor[:-1])
    return res_best


input_list = u.import_data('23')
start_pos = (1, 1)
end_pos = (len(input_list)-2, len(input_list[0])-2)
visited_init = [start_pos]
input_graph = create_graph(input_list)
final_dist = walk_dfs(start_pos, input_graph, 2, visited_init)
print(final_dist)
