n, q = map(int, input().split())

#N*Nの隣接行列を作る
graph = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(False)
    graph.append(row)

#ログを１行ずつ処理してgraphを更新する
for i in range(q):
    s = list(map(int, input().split()))
    # 頂点aの数字を配列の要素数に合わせる
    a = s[1] - 1
    # フォロー返しするとき
    if s[0] == 1:
        b = s[2] - 1
        graph[a][b] = True
    # フォロー全返しするとき
    if s[0] == 2:
        for j in range(n):
            if graph[j][a] and j != a:
                graph[a][j] = True
    if s[0] == 3:
        #フォローリストを作って、後でまとめて処理する
        to_follow = []
        for j in range(n):
            if graph[a][j] and j != a:
                for k in range(n):
                    if graph[j][k] and k != a:
                        to_follow.append(k)
        #まとめてフォローする
        for j in to_follow:
            graph[a][j] = True

# Trueを'Y', Falseを'N'に変換して出力する
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            print('Y', end='')
        else:
            print('N', end='')
    print()  # 改行のためにこれをつける