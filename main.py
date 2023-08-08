n, m, q = map(int, input().split())
graph = []
# N*Nの隣接行列を作成する
for i in range(n):
    row = []
    for j in range(n):
        row.append(False)
    graph.append(row)

# 隣接行列で辺が存在する箇所をTrueにする
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = True  # 隣接行列完成
    graph[v][u] = True

#頂点iにおける色の情報を入力
C = list(map(int, input().split()))

# クエリの処理
for i in range(q):
    query = list(map(int, input().split()))
    #スプリンクラーを起動する場合の処理
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        #頂点xと隣接する頂点の色を頂点xのものに変える
        for j in range(n):
            if graph[x][j]:
                C[j] = C[x]

    # 色を上書きするときの処理
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        #頂点xの色をyで上書きする
        C[x] = y