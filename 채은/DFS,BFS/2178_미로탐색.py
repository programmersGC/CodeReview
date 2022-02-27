from pprint import pprint

# 시작이 (1, 1)
graph = []

N, M = map(int, input().split())
for i in range(N):
    graph.append(list(map(int, input())))

# 뒤에가 몇 줄인지, 세로
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []

for x in range(N):
    for y in range(M):
        if graph[x][y] != 0 and not visited[x][y]:
            q.append([x, y])
            visited[x][y] = 1

            while q:
                r, c = q.pop(0)

                for k in range(4):
                    nx = r + dx[k]
                    ny = c + dy[k]
                    if 0 <= nx < N and 0<= ny < M and not visited[nx][ny] and graph[nx][ny] != 0:
                        q.append([nx, ny])
                        # 내 위치 + 1
                        graph[nx][ny] = graph[r][c] + 1
                        visited[nx][ny] = 1
   

pprint(graph)