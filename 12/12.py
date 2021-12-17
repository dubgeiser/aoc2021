#!/usr/bin/env python3


START = 'start'
END = 'end'


def read_data_file(fn):
    # Read into a graph:
    #   cave_from : [caves_to]
    paths = {}

    def fill_paths(paths, start, end):
        if start in paths.keys():
            paths[start].append(end)
        else:
            paths[start] = [end]

    with open(fn) as data:
        for line in data:
            start, end = line.strip().split('-')
            fill_paths(paths, start, end)
            # Connections between caves are bidirectional, make sure we have
            # them all (they are not necessarily defined in the input.
            start, end = end, start
            fill_paths(paths, start, end)
    return paths


def find_all_paths(cavern, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not cavern.get(start):
        return []
    paths = []
    for cave in cavern[start]:
        # Upper cased caves can be visited multiple times.
        if (cave not in path) or (cave.upper() == cave):
            newpaths = find_all_paths(cavern, cave, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def solve(data):
    return len(find_all_paths(data, START, END))


if __name__ == "__main__":
    data = read_data_file("input")
    print(f"{data = }")
    answer = solve(data)
    print(f"{answer = }")
