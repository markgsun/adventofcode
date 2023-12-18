#!/usr/bin/env python
"""17b-crucible.py: Advent of Code Day 17: Clumsy crucible"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = [list(map(int, x)) for x in u.import_data('17')]


def dijkstra(grid, start):
    # initialize visited and unvisited
    visited = {}
    # node: [i, j, n/e/s/w, consecutive moves]
    unvisited = {(start[0], start[1], '', 0): {'distance': 0}}

    while len(unvisited) > 0:
        # pop current based on smallest known distance
        min_dist = min([x['distance'] for x in unvisited.values()])
        current_node = [x for x in unvisited.keys() if unvisited[x]['distance'] == min_dist][0]
        current = {current_node: unvisited.pop(current_node)}

        # determine neighbors
        neighbors = []
        if (current_node[0] < len(grid)-1 and current_node[2] != 's' and
                not (current_node[2] == 'n' and current_node[3] == 10)):
            if current_node[2] == 'n':
                if (current_node[0]+1, current_node[1], 'n', current_node[3] + 1) not in visited.keys():
                    neighbors += [(current_node[0]+1, current_node[1], 'n', current_node[3] + 1)]
            else:
                if current_node[0] < len(grid)-4:
                    if (current_node[0]+4, current_node[1], 'n', 4) not in visited.keys():
                        neighbors += [(current_node[0]+4, current_node[1], 'n', 4)]

        if (current_node[0] > 0 and current_node[2] != 'n' and
                not (current_node[2] == 's' and current_node[3] == 10)):
            if current_node[2] == 's':
                if (current_node[0]-4, current_node[1], 's', current_node[3] + 1) not in visited.keys():
                    neighbors += [(current_node[0]-1, current_node[1], 's', current_node[3] + 1)]
            else:
                if current_node[0] > 3:
                    if (current_node[0]-4, current_node[1], 's', 4) not in visited.keys():
                        neighbors += [(current_node[0]-4, current_node[1], 's', 4)]

        if (current_node[1] < len(grid[0])-1 and current_node[2] != 'e' and
                not (current_node[2] == 'w' and current_node[3] == 10)):
            if current_node[2] == 'w':
                if (current_node[0], current_node[1]+1, 'w', current_node[3] + 1) not in visited.keys():
                    neighbors += [(current_node[0], current_node[1]+1, 'w', current_node[3] + 1)]
            else:
                if current_node[1] < len(grid[0])-4:
                    if (current_node[0], current_node[1]+4, 'w', 4) not in visited.keys():
                        neighbors += [(current_node[0], current_node[1]+4, 'w', 4)]

        if (current_node[1] > 0 and current_node[2] != 'w' and
                not (current_node[2] == 'e' and current_node[3] == 10)):
            if current_node[2] == 'e':
                if (current_node[0], current_node[1]-1, 'e', current_node[3] + 1) not in visited.keys():
                    neighbors += [(current_node[0], current_node[1]-1, 'e', current_node[3] + 1)]
            else:
                if current_node[1] > 3:
                    if (current_node[0], current_node[1]-4, 'e', 4) not in visited.keys():
                        neighbors += [(current_node[0], current_node[1]-4, 'e', 4)]

        # update info for neighbors if new distance is shorter
        for neighbor_node in neighbors:
            new_distance = current[current_node]['distance']
            if current_node[0] == neighbor_node[0]:
                diff = neighbor_node[1]-current_node[1]
                step = diff//abs(diff)
                for x in range(current_node[1], neighbor_node[1], step):
                    new_distance += grid[current_node[0]][x+step]
            if current_node[1] == neighbor_node[1]:
                diff = neighbor_node[0]-current_node[0]
                step = diff//abs(diff)
                for x in range(current_node[0], neighbor_node[0], step):
                    new_distance += grid[x+step][current_node[1]]

            if neighbor_node in unvisited.keys():
                if new_distance < unvisited[neighbor_node]['distance']:
                    unvisited[neighbor_node]['distance'] = new_distance
            else:
                unvisited.update({neighbor_node: {'distance': new_distance}})

        # add current to visited
        visited.update(current)
    return visited


start_pt = (0, 0)
end_pt = (len(input_list)-1, len(input_list[0])-1)
result = dijkstra(input_list, start_pt)

min_path = 1E100
for x in result.keys():
    if (x[0], x[1]) == end_pt:
        min_path = min(result[x]['distance'], min_path)

print(min_path)
