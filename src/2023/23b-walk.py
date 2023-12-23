#!/usr/bin/env python
"""23b-walk.py: Advent of Code Day 23: A long walk"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import sys
sys.setrecursionlimit(1000000)


def is_node(grid, pos):
    nbs = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
    res = not len([a for a in nbs if grid[a[0]][a[1]] == '#']) == 2 and grid[pos[0]][pos[1]] != '#'
    return


def create_graph(grid):
    graph = {}
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            if is_node(grid, (x, y)):
                next_nodes = []
                temp_pos = (x, y)
                while True:
                    for temp in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if grid[temp[0]][temp[1]] != '#':
                            temp_pos = temp
                            if is_node(grid, temp_pos):
                                next_nodes += [temp_pos]
                                break

            graph[(x, y)] = 0
    return graph


def walk_dfs(pos, graph, dist, visited):
    if pos == end_pos:
        return dist

    res_best = None
    for neighbor in graph[pos]:
        if neighbor in visited:
            continue
        visited += [neighbor]
        delta = abs(neighbor[0]-pos[0])+abs(neighbor[1]-pos[1])
        res_temp = walk_dfs(neighbor, graph, dist+delta, visited)
        if res_best is None or (res_temp is not None and res_temp > res_best):
            res_best = res_temp

        visited.remove(neighbor)
    return res_best


input_list = u.import_data('23ex')
start_pos = (1, 1)
end_pos = (len(input_list)-2, len(input_list[0])-2)
visited_init = [start_pos]
input_graph = create_graph(input_list)
# final_dist = walk_dfs(start_pos, input_graph, 2, visited_init)
# print(final_dist)

# Attempt: 5075 too low
# Answer: 6262
