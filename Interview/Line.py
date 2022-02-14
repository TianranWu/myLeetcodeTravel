from collections import deque
from collections import defaultdict
import itertools

# east: [0, 1]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(gird, start):
    row, col = len(gird), len(gird[0])
    seen = set()
    que = deque()
    que.append(start)
    ans = 0
    while que:
        x, y = que.popleft()
        seen.add((x, y))
        for dx, dy in dirs:
            cx = x + dx
            cy = y + dy
            if -1 < cx < row and -1 < cy < col and (cx, cy) not in seen and gird[cx][cy] != '#':
                que.append((cx, cy))
                seen.add((cx, cy))
                if gird[cx][cy] == 'D':
                    ans += 1
    return ans


def solve(grid, positions):
    row, col = len(grid), len(grid[0])
    nodes = row * col
    distances = [[float('inf') for _ in range(nodes)] for _ in range(nodes)]

    # convert (x, y) into int
    def mapping(x, y):
        return x * col + y

    # record minimux distance from (x, y) to any target position
    def min_distances(x, y):
        idx = mapping(x, y)
        distances[idx][idx] = 0
        que = deque()
        que.append((x, y, 0))
        seen = set()
        while que:
            x, y, dis = que.popleft()
            seen.add((x, y))
            for dx, dy in dirs:
                cx = x + dx
                cy = y + dy
                if -1 < cx < row and -1 < cy < col and (cx, cy) not in seen and gird[cx][cy] != '#':
                    tmp = mapping(cx, cy)
                    que.append((cx, cy, dis + 1))
                    seen.add((cx, cy))
                    distances[idx][tmp] = dis + 1
                    distances[tmp][idx] = dis + 1

    for i in range(row):
        for j in range(col):
            if gird[i][j] != '#':
                min_distances(i, j)

    dangers = []
    for p in positions['D']:
        dangers.append([*p, 0])

    def next_state(x, y, dir_idx):
        dx, dy = dirs[dir_idx]
        cx = x + dx
        cy = y + dy
        if cx < 0 or cx >= row or cy < 0 or cy >= col or gird[cx][cy] == '#':
            return [x, y, (dir_idx + 1) % 4]
        return [cx, cy, dir_idx]

    def solve_impl(order,org_x, org_y, dangers):
        idx = 0
        l = len(order)
        all_t = 0
        cur_dangers = dangers
        while idx < l:
            t = 0
            while True:
                cur_dangers = [next_state(*t) for t in cur_dangers]
                select_idx = order[idx]
                select_danger = cur_dangers[select_idx]
                if distances[mapping(select_danger[0], select_danger[1])][mapping(org_x, org_y)] <= t:
                    idx += 1
                    all_t += t
                    org_x, org_y = select_danger[0], select_danger[1]
                    break
                t += 1
        return all_t
    ans = float('inf')
    for order in itertools.permutations(list(range(len(dangers))), len(dangers)):
        ans = min(ans, solve_impl(order, positions['H'][0][0], positions['H'][0][1], dangers))
    return ans


if __name__ == '__main__':
    row, col = map(int, input().split())
    gird = []
    for _ in range(row):
        gird.append(input())
    positions = defaultdict(list)
    for i in range(row):
        for j in range(col):
            if gird[i][j] in ['H', 'D']:
                positions[gird[i][j]].append((i, j))
    if bfs(gird, positions['H'][0]) != len(positions['D']):
        print(-1)
    else:
        print(solve(gird, positions))
