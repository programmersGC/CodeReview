from pprint import pprint
# 1. 입력값 받기
graph = []
home_cnt = []
home = 0

N = int(input())
for i in range(N):
    graph.append(list(map(int, input())))


# 2. 4방탐색 좌표, graph, visited
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
visited = [[0] * N for _ in range(N)]

# 3. q 선언
q = []

# 3. for문 두개
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and not visited[r][c]:
            cnt = 0
            q.append([r,c])
            cnt += 1
            visited[r][c] = 1

            home += 1
            # 4. while문 시작
            while q:
                x, y = q.pop(0)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        cnt += 1
            
            home_cnt.append(cnt)

home_cnt.sort()
print(home)
for i in home_cnt:
    print(i)