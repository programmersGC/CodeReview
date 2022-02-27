from pprint import pprint

# 1. 사방탐색, map, visited

# 사방탐색 좌표
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


T = int(input())
for i in range(1, T+1):
    cnt = 0
    M, N, K = map(int, input().split())
    # 세로/가로
    graph = [[0] * N for _ in range(M)]

    # visited
    visited = [[0] * N for _ in range(M)]

    # Q
    q = []


    for j in range(K):
        r, c = map(int, input().split())
        graph[r][c] = 1

    # 2. for문 두번 돌기

    for k in range(M):
        for h in range(N):
            if graph[k][h] == 1 and visited[k][h] == 0:
                q.append([k,h])
                visited[k][h] = 1

                cnt += 1
    # 3. while 문 돌기
                while q:
                    x, y = q.pop(0)
                    # 4방탐색하면서 새로운 좌표 뽑기, 조건에 맞으면
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        # 3가지 조건
                        # 범위를 안벗어나고, 방문한적없어야해, 1이여야대
                        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
    
    print(cnt)

