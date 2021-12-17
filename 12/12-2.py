#!/usr/bin/env python3


START = 'start'
END = 'end'
MAX_VISITED = 2


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


def is_visitable(cave: str, path: list, visited: str) -> bool:
    if cave.upper() == cave: return True
    if cave not in path: return True
    if cave not in (START, END):
        return visited == cave and path.count(cave) < MAX_VISITED
    return False


def find_all_paths(cavern: dict, start: str, end: str, visited: str, path=[]) -> list:
    path = path + [start]
    if start == end:
        return [path]
    if not cavern.get(start):
        return []
    paths = []
    for cave in cavern[start]:
        if is_visitable(cave, path, visited):
            newpaths = find_all_paths(cavern, cave, end, visited, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def solve(data):
    unique_paths = []
    for i in data.keys():
        paths = []
        if i in (START, END):
            continue
        elif i.lower() == i:
            paths = find_all_paths(data, START, END, i)
        else:
            paths = find_all_paths(data, START, END, '')
        for p in paths:
            if p not in unique_paths:
                unique_paths.append(p)
    return len(unique_paths), unique_paths


def print_paths(paths: set) -> None:
    for p in paths:
        print(",".join(p))


if __name__ == "__main__":
    data = read_data_file("input")
    answer, paths = solve(data)
    print(f"{answer = }")
