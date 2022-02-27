from ntpath import join
from pprint import pprint

# 4방탐색, graph, visited
M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 0
width_list = []
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그래프 색칠
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[j][k] = 1

# 2중 for문
q = []

for k in range(N):
    for h in range(M):
        if graph[k][h] == 0 and not visited[k][h]:
            width = 0
            q.append([k, h])
            width += 1
            visited[k][h] = True

            cnt += 1

            while q:
                x, y = q.pop(0)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                        q.append([nx, ny])
                        width += 1
                        visited[nx][ny] = True
            width_list.append(width)

width_list.sort()
print(cnt)
# int형 join 하기
# str형으로 바꿔서 mapping 해서 join
# print(" ".join(map(str, width_list)))

# unpacking
print(*width_list)