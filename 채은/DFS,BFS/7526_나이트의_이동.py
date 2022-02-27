from pprint import pprint

T = int(input())

dx = [-2, -2, 2, 2, -1, 1,-1, 1]
dy = [-1, 1,-1, 1, -2, -2, 2, 2]

for i in range(1, T+1):
    I = int(input())
    # 시작하는 좌표
    s, e = map(int, input().split())
    # 끝나는 좌표
    fs, fe = map(int, input().split())

    graph = [[0] * I for _ in range(I)]

    q = []
    q.append([s, e])

    while q:
        x, y = q.pop(0)
        # 구하려는 좌표가 동일하면 끝내기
        if x == fs and y == fe:
            break
        
        for h in range(8):
            nx = x + dx[h]
            ny = y + dy[h]

            if 0<= nx < I and 0<= ny < I and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    # pprint(graph)
    print(graph[fs][fe])

                        