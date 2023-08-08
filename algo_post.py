### 入力 ###

s = input()  # 文字列入力

n = int(input())  # 数字入力

x, y = map(int, input().split())  # 複数数値を入力

a = list(map(int, input().split()))  # 数値リスト作成

c = []
for i in range(3):
    row = list(map(int, input().split()))
    c.append(row)  # 2次元配列の作成

